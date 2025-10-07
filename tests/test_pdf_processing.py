"""
Unit tests for PDF processing functionality
"""

import os
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from langchain.text_splitter import RecursiveCharacterTextSplitter


class TestPDFProcessing:
    """Test PDF loading and processing"""
    
    def test_check_pdf_files_exists(self, tmp_path):
        """Test checking for PDF files in directory"""
        # Create a temporary PDF file
        pdf_file = tmp_path / "test.pdf"
        pdf_file.write_text("test content")
        
        import glob
        pdf_files = glob.glob(os.path.join(tmp_path, "*.pdf"))
        
        assert len(pdf_files) == 1
        assert pdf_files[0].endswith("test.pdf")
    
    def test_check_pdf_files_empty_directory(self, tmp_path):
        """Test checking for PDF files in empty directory"""
        import glob
        pdf_files = glob.glob(os.path.join(tmp_path, "*.pdf"))
        
        assert len(pdf_files) == 0
    
    def test_text_splitter_configuration(self):
        """Test text splitter with configuration"""
        chunk_size = 1000
        chunk_overlap = 200
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        assert text_splitter._chunk_size == chunk_size
        assert text_splitter._chunk_overlap == chunk_overlap
    
    def test_text_splitter_creates_chunks(self):
        """Test that text splitter creates appropriate chunks"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
        )
        
        long_text = "This is a test. " * 50  # Create text longer than chunk size
        chunks = text_splitter.split_text(long_text)
        
        assert len(chunks) > 1
        for chunk in chunks:
            assert len(chunk) <= 120  # Some flexibility for overlap


class TestResourceDirectory:
    """Test resource directory handling"""
    
    def test_resources_directory_path(self):
        """Test resources directory path construction"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        resources_dir = os.path.join(parent_dir, 'resources')
        
        assert 'resources' in resources_dir
        assert os.path.isabs(resources_dir)
    
    def test_vector_db_directory_path(self):
        """Test vector DB directory path construction"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        vector_db_dir = os.path.join(parent_dir, 'chroma_db')
        
        assert 'chroma_db' in vector_db_dir
        assert os.path.isabs(vector_db_dir)
