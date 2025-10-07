# 📚 PDF QA Chatbot with Ollama

A local, privacy-focused RAG (Retrieval-Augmented Generation) application for PDF question answering using Ollama and LangChain.

## ✨ Features

- 🔒 **100% Local & Private** - No API keys, no cloud services
- 💰 **Zero Cost** - Run unlimited queries without API costs
- 📄 **Multi-PDF Support** - Query multiple documents simultaneously
- 🎯 **Context-Aware Answers** - Uses RAG for accurate responses
- 💬 **Interactive Chat Interface** - Streamlit chat UI with history
- 📊 **Source Attribution** - View source documents for each answer

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai/) installed
- Git

### Installation

1. **Install Ollama**
   ```bash
   # Download from https://ollama.ai/
   ```

2. **Pull a model**
   ```bash
   ollama pull gpt-oss:20b
   # Or: ollama pull llama3.2
   ```

3. **Clone repository**
   ```bash
   git clone https://github.com/WalkingDevFlag/PDF-QA-Chatbot
   cd PDF-QA-Chatbot
   ```

4. **Create environment**
   ```bash
   conda create -n pdf-qa python=3.11
   conda activate pdf-qa
   # Or use: python -m venv venv
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure (optional)**
   ```bash
   cp .env.example .env
   # Edit .env to change OLLAMA_MODEL or other settings
   ```

7. **Add PDFs**
   ```bash
   # Place PDF files in resources/ folder
   ```

## 💻 Usage

1. **Start Ollama**
   ```bash
   ollama serve
   ```

2. **Run the app**
   ```bash
   streamlit run main.py
   ```

3. **Open browser** → `http://localhost:8501`

4. **Ask questions** about your PDFs!

## ⚙️ Configuration

Edit `.env` to customize:

```plaintext
OLLAMA_MODEL=gpt-oss:20b    # Change model
CHUNK_SIZE=1000             # Text chunk size
CHUNK_OVERLAP=200           # Context overlap
```

### Available Models

- `gpt-oss:20b` - High quality (default)
- `llama3.2` - Fast and efficient
- `mistral` - Great balance
- `phi3` - Lightweight

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Ollama not running" | Run `ollama serve` |
| "No PDFs found" | Add PDFs to `resources/` folder |
| "Model not found" | Run `ollama pull gpt-oss:20b` |
| Slow performance | Use smaller model (`llama3.2` or `phi3`) |
| Out of memory | Reduce `CHUNK_SIZE` in `.env` |

## 📝 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) - Local LLM runtime
- [LangChain](https://github.com/langchain-ai/langchain) - RAG framework
- [Streamlit](https://streamlit.io/) - UI framework
- [ChromaDB](https://www.trychroma.com/) - Vector storage

---

⭐ Star this repo if you find it helpful!

