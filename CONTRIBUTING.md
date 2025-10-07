# 🤝 Contributing to PDF-QA-Chatbot

Thank you for your interest in contributing! This project welcomes contributions from everyone.

## 🎯 Getting Started

We welcome contributions of all kinds - from bug fixes to new features!

### Good First Issues

Look for issues labeled:
- `good first issue` - Perfect for beginners
- `help wanted` - We need community help
- `documentation` - Documentation improvements
- `enhancement` - New features or improvements

## 🚀 Quick Start for Contributors

### 1. Fork & Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/PDF-QA-Chatbot.git
cd PDF-QA-Chatbot
```

### 2. Set Up Development Environment

```bash
# Create environment
conda create -n pdf-qa python=3.11 -y
conda activate pdf-qa

# Install dependencies
pip install -r requirements.txt

# Install Ollama and pull a model
ollama pull gpt-oss:20b
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 4. Make Your Changes

- Write clean, readable code
- Follow existing code style
- Add comments for complex logic
- Test your changes thoroughly

### 5. Test Locally

```bash
# Start Ollama
ollama serve

# Run the app
streamlit run main.py

# Test your changes
```

### 6. Commit & Push

```bash
git add .
git commit -m "feat: Add awesome feature"
git push origin feature/your-feature-name
```

### 7. Create Pull Request

- Go to your fork on GitHub
- Click "New Pull Request"
- Fill out the PR template
- Wait for review

## 📋 Development Guidelines

### Code Style

- Use descriptive variable names
- Add docstrings to functions
- Keep functions focused and small
- Follow PEP 8 for Python code

### Commit Messages

Follow conventional commits format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

Examples:
```
feat: Add file upload functionality
fix: Resolve Ollama connection timeout
docs: Update installation instructions
refactor: Improve error handling in PDF loader
```

### Testing

Before submitting:

1. **Test the app locally**
   ```bash
   streamlit run main.py
   ```

2. **Test with different models**
   ```bash
   # In .env
   OLLAMA_MODEL=phi3
   # Test again
   ```

3. **Test with various PDFs**
   - Small PDFs (< 10 pages)
   - Large PDFs (> 100 pages)
   - Different formats/encodings

4. **Test error cases**
   - No PDFs in resources/
   - Ollama not running
   - Invalid configuration

## 🎨 Areas for Contribution

### 🌟 High Priority

1. **File Upload Feature**
   - Allow PDF upload through Streamlit UI
   - Multiple file upload support
   - File validation and error handling

2. **Additional Document Formats**
   - Support for DOCX files
   - Support for TXT files
   - Support for Markdown files

3. **Conversation Memory**
   - Remember previous questions
   - Context-aware responses
   - Chat session management

4. **Performance Optimization**
   - Caching improvements
   - Faster embedding generation
   - Reduced memory usage

### 💡 Medium Priority

5. **Enhanced UI/UX**
   - Dark/light theme toggle
   - Better mobile responsiveness
   - Custom styling options

6. **Model Management**
   - Model comparison feature
   - Easy model switching in UI
   - Model performance metrics

7. **Export Features**
   - Export chat history
   - Export as PDF/Markdown
   - Save conversations

8. **Advanced RAG**
   - Hybrid search (keyword + semantic)
   - Re-ranking strategies
   - Custom prompt templates

### 🔧 Nice to Have

9. **Developer Experience**
   - Unit tests
   - Integration tests
   - CI/CD pipeline

10. **Deployment Options**
    - Docker support
    - Docker Compose setup
    - Cloud deployment guides

11. **API Endpoint**
    - REST API for queries
    - API documentation
    - Rate limiting

12. **Multi-language Support**
    - Interface internationalization
    - Multi-language document support

## 🐛 Bug Reports

### Before Reporting

1. Check if the issue already exists
2. Test with the latest version
3. Try with a clean environment

### What to Include

```markdown
**Environment:**
- OS: [e.g., Windows 11, Ubuntu 22.04]
- Python Version: [e.g., 3.11.5]
- Ollama Version: [e.g., 0.1.29]
- Model: [e.g., llama3.2]

**Steps to Reproduce:**
1. Start the app
2. Upload PDF
3. Ask question "..."
4. See error

**Expected Behavior:**
Should return relevant answer

**Actual Behavior:**
Returns error: [paste error]

**Screenshots:**
[if applicable]

**Additional Context:**
Any other relevant information
```

## 💡 Feature Requests

### What Makes a Good Feature Request

- **Clear description** of the feature
- **Use case** explaining why it's needed
- **Examples** of how it would work
- **Alternatives** you've considered

### Template

```markdown
**Feature Description:**
A clear description of the feature

**Problem it Solves:**
What problem does this solve?

**Proposed Solution:**
How would this work?

**Alternatives:**
Other approaches considered

**Additional Context:**
Mockups, examples, etc.
```

## 📚 Documentation Contributions

Documentation is just as important as code!

- Fix typos and grammar
- Improve clarity
- Add examples
- Create tutorials
- Translate documentation

## 🔍 Code Review Process

### What We Look For

1. **Functionality** - Does it work as intended?
2. **Code Quality** - Is it clean and maintainable?
3. **Testing** - Has it been tested?
4. **Documentation** - Is it documented?
5. **Style** - Does it follow conventions?

### Review Timeline

- Simple PRs: 1-3 days
- Complex PRs: 3-7 days
- Large features: 1-2 weeks

We'll try to provide feedback quickly!

## 🎓 Learning Resources

### Python & Streamlit
- [Python Official Docs](https://docs.python.org/3/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)

### LangChain & RAG
- [LangChain Documentation](https://python.langchain.com/)
- [RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Vector Stores Guide](https://python.langchain.com/docs/integrations/vectorstores/)

### Ollama
- [Ollama Documentation](https://github.com/ollama/ollama/tree/main/docs)
- [Ollama Models](https://ollama.ai/library)
- [Ollama Python](https://github.com/ollama/ollama-python)

## 💬 Community

### Where to Get Help

- **GitHub Issues** - Bug reports and features
- **Discussions** - General questions
- **Pull Requests** - Code contributions

### Code of Conduct

Be respectful and inclusive:
- Welcome newcomers
- Be patient with questions
- Give constructive feedback
- Respect different opinions

## 🏆 Recognition

Contributors are recognized in:
- README.md (Contributors section)
- Release notes
- GitHub contributors page

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Every contribution helps make this project better. Thank you for taking the time to contribute!

---

**Questions?** Open an issue or start a discussion!

**Ready to contribute?** Pick an issue and let us know you're working on it!
