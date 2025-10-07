# 🚀 Complete Setup Guide - PDF QA Chatbot with Ollama

This guide will walk you through setting up the PDF QA Chatbot from scratch.

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Installing Ollama](#installing-ollama)
3. [Python Environment Setup](#python-environment-setup)
4. [Running the Application](#running-the-application)
5. [Troubleshooting](#troubleshooting)

## 💻 System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, macOS 10.15+, or Linux
- **RAM**: 8GB (16GB recommended)
- **Disk Space**: 10GB free space
- **Python**: 3.10 or higher (3.11 recommended)

### Recommended for Better Performance
- **RAM**: 16GB+
- **CPU**: Modern multi-core processor
- **GPU**: Optional, but helps with larger models

## 🦙 Installing Ollama

### Windows

1. Download Ollama for Windows from [ollama.ai/download/windows](https://ollama.ai/download/windows)
2. Run the installer
3. Open PowerShell or Command Prompt
4. Verify installation:
   ```powershell
   ollama --version
   ```

### macOS

```bash
# Using the install script
curl -fsSL https://ollama.ai/install.sh | sh

# Or using Homebrew
brew install ollama
```

### Linux

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Pull Your First Model

```bash
# Start Ollama server (keep this running)
ollama serve

# In a new terminal, pull a model
ollama pull gpt-oss:20b

# Test the model
ollama run gpt-oss:20b "Hello, how are you?"
```

## 🐍 Python Environment Setup

### Option 1: Using Conda (Recommended)

```bash
# Create environment
conda create --name pdf-qa python=3.11 -y

# Activate environment
conda activate pdf-qa

# Navigate to project directory
cd path/to/PDF-QA-Chatbot

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using venv

**Windows:**
```powershell
# Create environment
python -m venv venv

# Activate environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
# Create environment
python -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. Create Environment File

```bash
# Copy the example file
cp .env.example .env
```

### 2. Edit Configuration (Optional)

Open `.env` in a text editor and customize:

```plaintext
# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Embedding Configuration
EMBEDDING_MODEL=all-MiniLM-L6-v2

# RAG Configuration
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

### 3. Add PDF Files

Place your PDF documents in the `resources/` folder:

```bash
# Windows
copy "C:\path\to\your\document.pdf" resources\

# macOS/Linux
cp /path/to/your/document.pdf resources/
```

## 🎬 Running the Application

### Step 1: Start Ollama Server

Open a terminal and run:

```bash
ollama serve
```

**Keep this terminal running!** This starts the Ollama server that the chatbot will connect to.

### Step 2: Start the Chatbot

Open a **new terminal**, activate your environment, and run:

```bash
# Activate environment first
conda activate pdf-qa  # or: source venv/bin/activate

# Run the application
streamlit run main.py
```

### Step 3: Use the Application

1. Your browser should automatically open to `http://localhost:8501`
2. Wait for the initialization (loading PDFs, creating embeddings)
3. Start asking questions about your documents!

## 🔧 Troubleshooting

### Problem: "Ollama is not running"

**Solution:**
```bash
# Start Ollama in a separate terminal
ollama serve
```

### Problem: "No PDF files found"

**Solution:**
- Ensure PDF files are in the `resources/` folder
- Check that files have `.pdf` extension
- Restart the application after adding files

### Problem: "Model not found"

**Solution:**
```bash
# Pull the model
ollama pull llama3.2

# Verify it's available
ollama list
```

### Problem: "Connection refused" error

**Solution:**
- Check if Ollama is running: `ollama list`
- Verify the URL in `.env` is correct: `http://localhost:11434`
- Try restarting Ollama: Stop it (Ctrl+C) and run `ollama serve` again

### Problem: Application is very slow

**Solution:**
1. Use a smaller, faster model:
   ```bash
   ollama pull phi3
   ```
   Then update `.env`: `OLLAMA_MODEL=phi3`

2. Reduce chunk size in `.env`:
   ```plaintext
   CHUNK_SIZE=500
   CHUNK_OVERLAP=50
   ```

3. Close other memory-intensive applications

### Problem: Out of memory errors

**Solution:**
- Use a smaller model (phi3, gemma2)
- Reduce `CHUNK_SIZE` in `.env`
- Process fewer PDFs at once
- Increase system swap/page file

### Problem: Dependencies won't install

**Solution:**
```bash
# Upgrade pip first
pip install --upgrade pip setuptools wheel

# Try installing again
pip install -r requirements.txt

# If specific packages fail, install them separately
pip install streamlit
pip install langchain
# etc.
```

## 🎯 Model Recommendations

### For Best Quality (Recommended - Current Setup)
- **gpt-oss:20b** - Excellent quality, 20B parameters
  ```bash
  ollama pull gpt-oss:20b
  ```

### For Balance (Medium Hardware)
- **llama3.2** - Great balance of speed and quality
  ```bash
  ollama pull llama3.2
  ```

### For Speed (Low-End Hardware)
- **phi3** - Very fast, good quality
  ```bash
  ollama pull phi3
  ```

### For Specific Use Cases
- **mistral** - Good for technical documents
- **gemma2** - Efficient Google model
- **codellama** - Better for code-heavy PDFs

## 📊 Performance Tips

### 1. Optimize Chunk Size

For different document types:

**Dense technical documents:**
```plaintext
CHUNK_SIZE=1500
CHUNK_OVERLAP=300
```

**General documents:**
```plaintext
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

**Quick scanning:**
```plaintext
CHUNK_SIZE=500
CHUNK_OVERLAP=50
```

### 2. Hardware Acceleration

If you have a GPU:
```bash
# Ollama automatically uses GPU if available
# Check with:
ollama list
```

### 3. Multiple PDFs

- Start with 1-2 PDFs to test
- Add more gradually
- Consider splitting very large PDFs

## 🆘 Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Review [Ollama documentation](https://github.com/ollama/ollama)
3. Open an issue on [GitHub](https://github.com/WalkingDevFlag/PDF-QA-Chatbot/issues)

## ✅ Verification Checklist

Before reporting issues, verify:

- [ ] Ollama is installed: `ollama --version`
- [ ] Model is downloaded: `ollama list`
- [ ] Ollama server is running: `ollama serve`
- [ ] Python environment is activated
- [ ] Dependencies are installed: `pip list`
- [ ] PDF files are in `resources/` folder
- [ ] `.env` file exists (copy from `.env.example`)

## 🎓 Next Steps

Once everything is working:

1. Experiment with different models
2. Try different chunk sizes
3. Add more PDF documents
4. Customize the system prompt in `main.py`
5. Explore the codebase and contribute!

---

**Happy Chatting! 🚀**
