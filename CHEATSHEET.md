# 🚀 Quick Start Cheat Sheet

## One-Line Setup

```bash
# Install Ollama, pull model, create env, install deps, run app
ollama serve & ollama pull gpt-oss:20b & conda create -n pdf-qa python=3.11 -y & conda activate pdf-qa & pip install -r requirements.txt & streamlit run main.py
```

## Essential Commands

### Ollama
```bash
ollama serve                    # Start server
ollama pull gpt-oss:20b        # Download model
ollama list                     # List models
ollama run gpt-oss:20b "test"  # Test model
```

### Environment
```bash
# Conda
conda create -n pdf-qa python=3.11 -y
conda activate pdf-qa

# venv
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Unix
```

### Application
```bash
pip install -r requirements.txt
streamlit run main.py
```

## Quick Config (.env)

```plaintext
OLLAMA_MODEL=gpt-oss:20b           # Change model
CHUNK_SIZE=1000                    # Adjust chunking
CHUNK_OVERLAP=200                  # Context overlap
```

## Model Recommendations

| Model | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| gpt-oss:20b | ~12GB | ⚡ | ⭐⭐⭐⭐⭐ | High quality (default) |
| llama3.2 | 4.7GB | ⚡⚡ | ⭐⭐⭐ | Balanced |
| mistral | 4.1GB | ⚡⚡ | ⭐⭐⭐ | Technical docs |
| phi3 | 3.8GB | ⚡⚡⚡ | ⭐⭐ | Low-end hardware |

## Troubleshooting Quick Fixes

```bash
# Ollama not running
ollama serve

# Model not found
ollama pull gpt-oss:20b

# Dependencies issue
pip install --upgrade pip
pip install -r requirements.txt

# Clear cache
rm -rf chroma_db/
```

## Useful Directories

```
resources/          # Put PDFs here
chroma_db/          # Vector database (auto-generated)
.env                # Your configuration
```

## Development Workflow

```bash
# 1. Switch to dev branch
git checkout -b my-feature

# 2. Make changes
# Edit files...

# 3. Test locally
streamlit run main.py

# 4. Commit
git add .
git commit -m "Add feature"
git push origin my-feature

# 5. Create PR
```

## Performance Tuning

### Faster Response
```plaintext
OLLAMA_MODEL=phi3
CHUNK_SIZE=500
```

### Better Quality
```plaintext
OLLAMA_MODEL=llama3.1
CHUNK_SIZE=1500
CHUNK_OVERLAP=300
```

## Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| "Ollama not running" | `ollama serve` |
| "No PDFs found" | Add PDFs to `resources/` |
| Slow responses | Use smaller model or reduce chunk size |
| Out of memory | Use phi3 or reduce chunk size |
| Connection refused | Check Ollama is on port 11434 |

## Environment Variables

```bash
OLLAMA_BASE_URL=http://localhost:11434    # Ollama server
OLLAMA_MODEL=llama3.2                     # Model name
EMBEDDING_MODEL=all-MiniLM-L6-v2          # Embeddings
CHUNK_SIZE=1000                           # Text chunk size
CHUNK_OVERLAP=200                         # Overlap tokens
```

## Keyboard Shortcuts (Streamlit)

- `Ctrl + R` - Reload app
- `Ctrl + C` - Stop server (terminal)
- `R` - Rerun (when focused on app)

## Quick Testing

```bash
# Test Ollama
ollama run gpt-oss:20b "Hello"

# Test Python
python -c "import streamlit; print('OK')"

# Check PDFs
ls resources/

# Verify .env
cat .env
```

## Support Links

- 📚 [Full Setup Guide](SETUP_GUIDE.md)
- 🔄 [Migration Guide](MIGRATION_GUIDE.md)
- 📖 [README](README.md)
- 🐛 [Report Issues](https://github.com/WalkingDevFlag/PDF-QA-Chatbot/issues)

---

**Need Help?** Check [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions!
