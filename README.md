# 📚 PDF QA Chatbot with Ollama

A local RAG (Retrieval-Augmented Generation) application for PDF question answering using Ollama and LangChain.

## ✨ Features

- 🔒 100% Local & Private - No API keys needed
- 📄 Multi-PDF Support
- 💬 Interactive Chat Interface
- 📊 Source Document Attribution
- ⚙️ Configurable via .env file

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai/) installed

### Installation

1. **Install Ollama and pull a model:**
   ```bash
   # Download from https://ollama.ai/
   ollama pull gpt-oss:20b
   ```

2. **Clone and setup:**
   ```bash
   git clone https://github.com/WalkingDevFlag/PDF-QA-Chatbot
   cd PDF-QA-Chatbot
   ```

3. **Create environment and install dependencies:**
   ```bash
   # Using conda
   conda create -n pdf-qa python=3.11 -y
   conda activate pdf-qa
   pip install -r requirements.txt

   # Or using venv
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

4. **Configure (optional):**
   ```bash
   copy .env.example .env  # Windows
   # Edit .env to change model or settings
   ```

5. **Add PDFs to `resources/` folder**

## 💻 Usage

1. **Start Ollama:**
   ```bash
   ollama serve
   ```

2. **Run the app:**
   ```bash
   streamlit run main.py
   ```

3. **Open browser:** `http://localhost:8501`

4. **Ask questions about your PDFs!**

## ⚙️ Configuration

Edit `.env` file:

```plaintext
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gpt-oss:20b        # Change model here
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

### Available Models

- `gpt-oss:20b` - High quality (default)
- `llama3.2` - Fast and efficient
- `mistral` - Balanced
- `phi3` - Lightweight

Pull any model: `ollama pull <model-name>`

## 🔧 Troubleshooting

**Ollama not running:** `ollama serve`

**No PDFs found:** Add PDFs to `resources/` folder

**Model not found:** `ollama pull gpt-oss:20b`

**Slow performance:** Use a smaller model or reduce `CHUNK_SIZE` in `.env`

## 📝 License

MIT License

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) - Local LLM runtime
- [LangChain](https://github.com/langchain-ai/langchain) - RAG framework
- [Streamlit](https://streamlit.io/) - UI framework
- [ChromaDB](https://www.trychroma.com/) - Vector database

