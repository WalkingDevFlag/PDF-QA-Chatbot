# 📚 PDF QA Chatbot with Ollama

A **local, privacy-focused** RAG (Retrieval-Augmented Generation) application for PDF question answering using Ollama and LangChain. Run powerful AI models completely locally without API costs or privacy concerns!

## ✨ Features

- **🔒 100% Local & Private**: No API keys, no cloud services, complete data privacy
- **💰 Zero Cost**: Run unlimited queries without API costs
- **📄 Multi-PDF Support**: Load and query multiple PDF documents simultaneously
- **🧮 Smart Chunking**: Optimized text splitting with configurable chunk size and overlap
- **🎯 Context-Aware Answers**: Uses RAG to provide accurate, source-based responses
- **💬 Interactive Chat Interface**: Beautiful Streamlit chat UI with message history
- **📊 Source Attribution**: View the source documents used for each answer
- **⚙️ Highly Configurable**: Easy configuration through environment variables

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** (Python 3.11 recommended)
- **Ollama** installed and running locally
- **Git** (for cloning the repository)

### Step 1: Install Ollama

Download and install Ollama from [ollama.ai](https://ollama.ai/)

**Windows:**
```powershell
# Download from https://ollama.ai/download/windows
```

**macOS/Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Step 2: Pull an Ollama Model

```bash
# Pull the default model (GPT-OSS 20B)
ollama pull gpt-oss:20b

# Or try other models
ollama pull llama3.2
ollama pull mistral
ollama pull phi3
```

### Step 3: Start Ollama Server

```bash
ollama serve
```
Leave this terminal running in the background.

### Step 4: Clone the Repository

```bash
git clone https://github.com/WalkingDevFlag/PDF-QA-Chatbot
cd PDF-QA-Chatbot
```

### Step 5: Create Python Environment

**Using Conda (Recommended):**
```bash
conda create --name pdf-qa python=3.11
conda activate pdf-qa
```

**Using venv:**
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 7: Configure Environment

Copy the example environment file and customize if needed:

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

Edit `.env` to change default settings (optional):
```plaintext
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gpt-oss:20b
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

### Step 8: Add PDF Files

Place your PDF files in the `resources/` directory:
```bash
# Windows
copy your-document.pdf resources\

# macOS/Linux
cp your-document.pdf resources/
```

## 💻 Usage

### Start the Application

```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`

### Using the Chatbot

1. **Wait for Initialization**: The app will load PDFs, create embeddings, and build the vector database
2. **Ask Questions**: Type your questions in the chat input at the bottom
3. **View Sources**: Expand "View Source Documents" to see which PDF sections were used
4. **Reload Documents**: Use the sidebar button to reload PDFs after adding new ones

### Example Questions

```
- "What is the main topic of this document?"
- "Summarize the key findings"
- "What does the document say about [specific topic]?"
- "List all the recommendations mentioned"
```

## 📁 Project Structure

```
PDF-QA-Chatbot/
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment configuration template
├── .env                   # Your local configuration (not committed)
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── resources/            # Place your PDF files here
│   └── *.pdf
└── chroma_db/           # Vector database (auto-generated)
```

## ⚙️ Configuration

### Available Ollama Models

Popular models you can use:
- `gpt-oss:20b` (default) - High quality, 20B parameter model
- `llama3.2` - Fast and efficient
- `llama3.1` - More capable, larger model
- `mistral` - Great balance of speed and quality
- `phi3` - Lightweight and fast
- `gemma2` - Google's efficient model

Change model in `.env`:
```plaintext
OLLAMA_MODEL=mistral
```

### Tuning Performance

**For better accuracy (slower):**
```plaintext
CHUNK_SIZE=1500
CHUNK_OVERLAP=300
```

**For faster responses (less accurate):**
```plaintext
CHUNK_SIZE=500
CHUNK_OVERLAP=50
```

## 🔧 Troubleshooting

### "Ollama is not running"
```bash
# Start Ollama server
ollama serve
```

### "No PDF files found"
- Ensure PDF files are in the `resources/` directory
- Check file extensions are `.pdf`

### "Model not found"
```bash
# Pull the model first
ollama pull gpt-oss:20b
```

### Slow Performance
- Use a smaller model (phi3, llama3.2)
- Reduce chunk size
- Ensure Ollama has enough system resources

### Out of Memory
- Reduce `CHUNK_SIZE`
- Use a smaller embedding model
- Close other applications

## 🎯 Roadmap

- [ ] Support for multiple file formats (DOCX, TXT, MD)
- [ ] File upload through web interface
- [ ] Conversation memory and context
- [ ] Multiple conversation threads
- [ ] Export chat history
- [ ] Custom system prompts
- [ ] Model comparison feature
- [ ] Docker deployment
- [ ] API endpoint support

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) - For making local LLMs accessible
- [LangChain](https://github.com/langchain-ai/langchain) - For RAG framework
- [Streamlit](https://streamlit.io/) - For the amazing UI framework
- [HuggingFace](https://huggingface.co/) - For embedding models
- [ChromaDB](https://www.trychroma.com/) - For vector storage

## 📧 Contact

**Author**: WalkingDevFlag  
**Repository**: [PDF-QA-Chatbot](https://github.com/WalkingDevFlag/PDF-QA-Chatbot)

---

⭐ If you find this project helpful, please star the repository!

