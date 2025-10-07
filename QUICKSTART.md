# ⚡ Quick Start - Your Setup

This is your personal quick-start guide for running the PDF-QA-Chatbot with your gpt-oss:20b model.

## 🚀 Start the App (3 Steps)

### Step 1: Start Ollama
```powershell
ollama serve
```
**Leave this terminal running!**

### Step 2: Activate Environment & Run
Open a **new PowerShell terminal**:
```powershell
# Navigate to project
cd "E:\Hackethon\Hacktober Fest 2025\PDF-QA-Chatbot"

# Activate conda environment
conda activate pdf-qa

# Run the app
streamlit run main.py
```

### Step 3: Open Browser
The app should auto-open at: `http://localhost:8501`

If not, manually open your browser and go to that URL.

## 📄 Adding PDFs

```powershell
# Copy PDFs to resources folder
copy "C:\path\to\your\file.pdf" "E:\Hackethon\Hacktober Fest 2025\PDF-QA-Chatbot\resources\"
```

Then click **"🔄 Reload Documents"** in the sidebar.

## 🔧 Your Configuration

### Current Model: gpt-oss:20b
- **Quality**: Excellent (⭐⭐⭐⭐⭐)
- **Size**: ~12GB
- **Speed**: Medium (high quality worth it!)
- **RAM Needed**: 16GB recommended

### Settings (in .env)
```plaintext
OLLAMA_MODEL=gpt-oss:20b
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

## 🎯 Common Commands

### Check if Ollama is running
```powershell
ollama list
```

### Test your model directly
```powershell
ollama run gpt-oss:20b "What is AI?"
```

### Verify Python environment
```powershell
conda activate pdf-qa
python -c "import streamlit; import langchain; print('All good!')"
```

### Restart everything
```powershell
# Stop Ollama (Ctrl+C in the ollama serve terminal)
# Stop Streamlit (Ctrl+C in the streamlit terminal)

# Start fresh
ollama serve
# Then in new terminal:
conda activate pdf-qa
streamlit run main.py
```

## 🐛 Troubleshooting

### "Ollama is not running"
Solution: Run `ollama serve` in a terminal

### "No PDF files found"
Solution: Add PDFs to the `resources` folder

### App is slow
Your gpt-oss:20b model is high-quality but resource-intensive. This is normal!
- First query is always slowest (loading)
- Subsequent queries are faster
- If too slow, consider using `llama3.2` instead

### Out of memory
- Close other applications
- Use a smaller model: Change `.env` to `OLLAMA_MODEL=llama3.2`
- Restart your computer

## 💡 Pro Tips

### Better Performance
1. **Keep Ollama running** - Don't restart it between sessions
2. **Keep resources folder small** - Start with 1-3 PDFs
3. **Close Chrome/Edge** - They use lots of RAM

### Better Results
1. **Ask specific questions** - "What is X?" not "Tell me everything"
2. **Check source documents** - Expand "📄 View Source Documents"
3. **Reload after adding PDFs** - Use sidebar button

### Development
```powershell
# Create a new feature
git checkout -b feature/my-feature

# Make changes, then:
git add .
git commit -m "feat: Add my feature"
git push origin feature/my-feature
```

## 📂 Project Structure Quick Reference

```
PDF-QA-Chatbot/
├── main.py                    ← Main application
├── .env                       ← Your configuration
├── requirements.txt           ← Dependencies
├── resources/                 ← PUT PDFs HERE
│   └── your-pdfs.pdf
├── chroma_db/                 ← Auto-generated vector DB
└── [docs]/                    ← Documentation
```

## 🎯 Daily Workflow

### Morning Setup
```powershell
# Terminal 1
cd "E:\Hackethon\Hacktober Fest 2025\PDF-QA-Chatbot"
ollama serve

# Terminal 2
cd "E:\Hackethon\Hacktober Fest 2025\PDF-QA-Chatbot"
conda activate pdf-qa
streamlit run main.py
```

### Working with PDFs
1. Copy PDF to `resources/`
2. Click "🔄 Reload Documents" in sidebar
3. Wait for indexing
4. Start asking questions!

### End of Day
- Ctrl+C in both terminals
- Done! Everything is saved.

## 🆘 Emergency Recovery

### If everything breaks:
```powershell
# 1. Delete vector database
Remove-Item -Recurse -Force "E:\Hackethon\Hacktober Fest 2025\PDF-QA-Chatbot\chroma_db"

# 2. Reinstall dependencies
conda activate pdf-qa
pip install -r requirements.txt --force-reinstall

# 3. Restart Ollama
ollama serve

# 4. Run app
streamlit run main.py
```

### Nuclear option (complete reset):
```powershell
# Remove environment
conda deactivate
conda env remove -n pdf-qa

# Recreate from scratch
conda create -n pdf-qa python=3.11 -y
conda activate pdf-qa
pip install -r requirements.txt

# Verify Ollama model
ollama list

# Run
streamlit run main.py
```

## 📞 Need More Help?

1. **README.md** - Overview and features
2. **SETUP_GUIDE.md** - Detailed setup
3. **CHEATSHEET.md** - Quick commands
4. **TRANSFORMATION_SUMMARY.md** - What changed

## ✅ Pre-Flight Checklist

Before starting the app, verify:
- [ ] Ollama is installed: `ollama --version`
- [ ] Model is downloaded: `ollama list` (should show gpt-oss:20b)
- [ ] Environment exists: `conda env list` (should show pdf-qa)
- [ ] PDFs in resources: `ls resources\*.pdf`
- [ ] .env file exists: `ls .env`

All good? Run the app! 🚀

---

**Your Setup**: Windows + PowerShell + Conda + gpt-oss:20b  
**Status**: ✅ Ready to use!  
**Last Updated**: October 7, 2025
