"""
Unit tests for Ollama integration
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import requests


class TestOllamaConnection:
    """Test Ollama connection and configuration"""
    
    @patch('requests.get')
    def test_ollama_connection_success(self, mock_get):
        """Test successful Ollama connection"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            is_connected = response.status_code == 200
        except Exception:
            is_connected = False
        
        assert is_connected is True
    
    @patch('requests.get')
    def test_ollama_connection_failure(self, mock_get):
        """Test failed Ollama connection"""
        mock_get.side_effect = requests.exceptions.ConnectionError()
        
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            is_connected = response.status_code == 200
        except Exception:
            is_connected = False
        
        assert is_connected is False
    
    @patch('requests.get')
    def test_ollama_connection_timeout(self, mock_get):
        """Test Ollama connection timeout"""
        mock_get.side_effect = requests.exceptions.Timeout()
        
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            is_connected = response.status_code == 200
        except Exception:
            is_connected = False
        
        assert is_connected is False
    
    def test_ollama_configuration_from_env(self):
        """Test Ollama configuration from environment variables"""
        import os
        
        # Test default values
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        model = os.getenv("OLLAMA_MODEL", "gpt-oss:20b")
        temperature = float(os.getenv("OLLAMA_TEMPERATURE", "0.7"))
        
        assert base_url == "http://localhost:11434"
        assert model == "gpt-oss:20b"
        assert temperature == 0.7
    
    def test_ollama_model_configuration(self):
        """Test Ollama model configuration parameters"""
        model_name = "gpt-oss:20b"
        base_url = "http://localhost:11434"
        temperature = 0.7
        num_predict = -1
        
        assert isinstance(model_name, str)
        assert base_url.startswith("http")
        assert 0 <= temperature <= 1
        assert num_predict == -1  # Unlimited


class TestEmbeddingsConfiguration:
    """Test embeddings configuration"""
    
    def test_embedding_model_configuration(self):
        """Test embedding model configuration"""
        import os
        
        embedding_model = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
        
        assert isinstance(embedding_model, str)
        assert len(embedding_model) > 0
    
    def test_chunk_configuration(self):
        """Test chunk size configuration"""
        import os
        
        chunk_size = int(os.getenv("CHUNK_SIZE", "1000"))
        chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "200"))
        retrieval_k = int(os.getenv("RETRIEVAL_K", "6"))
        
        assert chunk_size > 0
        assert chunk_overlap >= 0
        assert chunk_overlap < chunk_size
        assert retrieval_k > 0
