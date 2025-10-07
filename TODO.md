# 📝 TODO List

## 🧪 Testing

- [ ] Add unit tests for core functionality
  - [ ] Test PDF loading and parsing
  - [ ] Test text chunking logic
  - [ ] Test embeddings generation
  - [ ] Test vector store operations
  - [ ] Test QA chain responses
- [ ] Add integration tests
  - [ ] Test end-to-end RAG pipeline
  - [ ] Test Ollama integration
  - [ ] Test Streamlit UI components
- [ ] Set up CI/CD pipeline
  - [ ] Configure GitHub Actions for automated testing
  - [ ] Add linting (flake8, black, pylint)
  - [ ] Add type checking (mypy)
  - [ ] Add code coverage reporting

## 💾 Resource Management

- [ ] Implement vector database persistence check
  - [ ] Check if `chroma_db` exists before recreating
  - [ ] Compare PDF file modification times with DB timestamp
  - [ ] Only rebuild DB when PDFs have changed
  - [ ] Add "Force Rebuild" option in UI
- [ ] Add database versioning/metadata
  - [ ] Store list of indexed PDFs
  - [ ] Store indexing timestamp
  - [ ] Track embedding model version
- [ ] Optimize memory usage
  - [ ] Add cleanup for old vector stores
  - [ ] Implement lazy loading for large PDFs

## ⚠️ Error Handling Gaps

- [ ] Add Ollama model availability check
  - [ ] Verify model is pulled before attempting to use it
  - [ ] Provide helpful error message with pull command
  - [ ] List available models if requested model not found
- [ ] Add PDF content validation
  - [ ] Check for empty PDFs
  - [ ] Handle password-protected PDFs
  - [ ] Validate PDF format and readability
  - [ ] Handle corrupted PDF files gracefully
- [ ] Improve network timeout handling
  - [ ] Add retry logic for Ollama API calls
  - [ ] Implement exponential backoff
  - [ ] Add timeout configuration options
  - [ ] Better error messages for network issues
- [ ] Add comprehensive error logging
  - [ ] Log errors to file
  - [ ] Add debug mode
  - [ ] User-friendly error messages in UI

## 🏗️ Code Organization

- [ ] Refactor into modular structure
  - [ ] Create `config.py` for configuration management
  - [ ] Create `rag.py` for RAG logic (embeddings, vector store, QA chain)
  - [ ] Create `pdf_processor.py` for PDF loading and chunking
  - [ ] Create `ui.py` for Streamlit interface
  - [ ] Create `utils.py` for helper functions
  - [ ] Keep `main.py` as entry point only
- [ ] Improve code organization
  - [ ] Add type hints throughout
  - [ ] Create classes for major components (RAGSystem, PDFProcessor)
  - [ ] Implement proper dependency injection
  - [ ] Add constants file for magic numbers
- [ ] Documentation improvements
  - [ ] Add inline code documentation
  - [ ] Create architecture documentation
  - [ ] Add API documentation for functions/classes

---

## 📊 Priority Levels

**High Priority:** Testing, Resource Management  
**Medium Priority:** Error Handling Gaps  
**Low Priority:** Code Organization (can be done incrementally)

## 🎯 Suggested Implementation Order

1. Implement vector database persistence check (quick win, big impact)
2. Add Ollama model availability check (prevents common user errors)
3. Add PDF content validation (improves user experience)
4. Set up basic unit tests (foundation for reliability)
5. Refactor into modules (improves maintainability)
6. Add CI/CD pipeline (automates quality checks)
7. Improve error handling and logging (better debugging)
