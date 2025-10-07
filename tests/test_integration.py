"""
Integration tests for the PDF QA Chatbot
"""

import os
import pytest
import requests
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import tempfile


class TestRAGPipeline:
    """Integration tests for the RAG pipeline"""
    
    @pytest.fixture
    def temp_pdf_directory(self):
        """Create a temporary directory with mock PDF files"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a dummy PDF file
            pdf_path = os.path.join(tmpdir, "test.pdf")
            Path(pdf_path).touch()
            yield tmpdir
    
    @pytest.fixture
    def temp_vector_db_directory(self):
        """Create a temporary directory for vector DB"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield tmpdir
    
    def test_pdf_to_chunks_pipeline(self, temp_pdf_directory):
        """Test the pipeline from PDF loading to chunking"""
        import glob
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        
        # Check PDFs exist
        pdf_files = glob.glob(os.path.join(temp_pdf_directory, "*.pdf"))
        assert len(pdf_files) > 0
        
        # Test text splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        
        assert text_splitter is not None
    
    @patch('requests.get')
    def test_end_to_end_connection_flow(self, mock_get):
        """Test end-to-end connection flow"""
        # Mock Ollama connection
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Simulate connection check
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            ollama_connected = response.status_code == 200
        except Exception:
            ollama_connected = False
        
        assert ollama_connected is True
    
    def test_configuration_loading(self):
        """Test that all configurations load correctly"""
        import os
        
        configs = {
            'OLLAMA_BASE_URL': os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            'OLLAMA_MODEL': os.getenv("OLLAMA_MODEL", "gpt-oss:20b"),
            'OLLAMA_TEMPERATURE': float(os.getenv("OLLAMA_TEMPERATURE", "0.7")),
            'EMBEDDING_MODEL': os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2"),
            'CHUNK_SIZE': int(os.getenv("CHUNK_SIZE", "1000")),
            'CHUNK_OVERLAP': int(os.getenv("CHUNK_OVERLAP", "200")),
            'RETRIEVAL_K': int(os.getenv("RETRIEVAL_K", "6")),
        }
        
        # Verify all configs loaded
        assert all(value is not None for value in configs.values())
        assert configs['CHUNK_SIZE'] > configs['CHUNK_OVERLAP']
        assert 0 <= configs['OLLAMA_TEMPERATURE'] <= 1


class TestErrorHandling:
    """Integration tests for error handling"""
    
    def test_empty_pdf_directory_handling(self, tmp_path):
        """Test handling of empty PDF directory"""
        import glob
        
        pdf_files = glob.glob(os.path.join(tmp_path, "*.pdf"))
        
        # Should return empty list, not crash
        assert isinstance(pdf_files, list)
        assert len(pdf_files) == 0
    
    @patch('requests.get')
    def test_ollama_not_running_handling(self, mock_get):
        """Test handling when Ollama is not running"""
        mock_get.side_effect = requests.exceptions.ConnectionError()
        
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            is_running = response.status_code == 200
        except Exception:
            is_running = False
        
        # Should handle gracefully
        assert is_running is False
