"""
PDF QA Chatbot with Ollama Integration
A local, privacy-focused RAG application for PDF question answering
"""

import os
import glob
import time
from pathlib import Path
from typing import List

import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.callbacks.base import BaseCallbackHandler

# Load environment variables
load_dotenv()

# Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:20b")
OLLAMA_TEMPERATURE = float(os.getenv("OLLAMA_TEMPERATURE", "0.7"))
OLLAMA_NUM_PREDICT = int(os.getenv("OLLAMA_NUM_PREDICT", "-1"))
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))
RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", "6"))

# Directories
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(SCRIPT_DIR, 'resources')
VECTOR_DB_DIR = os.path.join(SCRIPT_DIR, 'chroma_db')


class StreamHandler(BaseCallbackHandler):
    """Callback handler for streaming responses to Streamlit"""
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        """Run when LLM generates a new token"""
        self.text += token
        self.container.markdown(self.text + "▌")


def check_ollama_connection():
    """Check if Ollama is running and accessible"""
    try:
        import requests
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        return response.status_code == 200
    except Exception as e:
        return False


def check_pdf_files() -> List[str]:
    """Check for PDF files in resources directory"""
    pdf_files = glob.glob(os.path.join(RESOURCES_DIR, "*.pdf"))
    return pdf_files


@st.cache_resource
def initialize_rag_system():
    """Initialize the RAG system with embeddings and vector store"""
    try:
        # Check for PDF files
        pdf_files = check_pdf_files()
        if not pdf_files:
            return None, None, "No PDF files found in the 'resources' folder!"
        
        # Load PDFs
        loader = PyPDFDirectoryLoader(RESOURCES_DIR)
        documents = loader.load()
        
        if not documents:
            return None, None, "Failed to load any documents from PDFs!"
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_documents(documents)
        
        # Create embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        # Create vector store
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=VECTOR_DB_DIR
        )
        
        # Initialize Ollama LLM
        llm = OllamaLLM(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=OLLAMA_TEMPERATURE,
            num_predict=OLLAMA_NUM_PREDICT,  # -1 = no limit, let model decide naturally
        )
        
        # Create custom prompt template
        prompt_template = """You are a knowledgeable AI assistant specializing in analyzing and explaining document content.

Use the following context from the documents to answer the question comprehensively and in detail.

Instructions:
- Provide a thorough, well-structured answer with appropriate depth based on the question
- For broad questions: Give comprehensive multi-point answers covering all relevant aspects
- For specific questions: Give focused, detailed answers without unnecessary elaboration
- Include specific details, examples, and explanations from the context
- Organize your response with clear sections or bullet points when appropriate
- If the context covers multiple aspects, explain each one thoroughly
- Be informative and educational in your response
- Stop naturally when you've fully answered the question - don't pad or cut off mid-thought
- If you don't know something based on the context, acknowledge it, but provide what information you do have

Context from documents:
{context}

Question: {question}

Detailed Answer:"""
        
        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": RETRIEVAL_K}  # Configurable chunk retrieval
            ),
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT}
        )
        
        # Return qa_chain, vectorstore, and metadata
        pdf_count = len(pdf_files)
        doc_count = len(documents)
        chunk_count = len(chunks)
        
        return qa_chain, vectorstore, {
            'pdf_count': pdf_count,
            'pdf_names': [Path(f).name for f in pdf_files],
            'doc_count': doc_count,
            'chunk_count': chunk_count
        }
    
    except Exception as e:
        return None, None, f"Error: {str(e)}"


def main():
    """Main Streamlit application"""
    
    # Page configuration
    st.set_page_config(
        page_title="PDF QA Chatbot (Ollama)",
        page_icon="📚",
        layout="wide"
    )
    
    # Title and description
    st.title("📚 PDF QA Chatbot with Ollama")
    st.markdown("*Ask questions about your PDF documents using local AI models*")
    
    # Sidebar with information
    with st.sidebar:
        st.header("⚙️ Configuration")
        st.markdown(f"**Model:** {OLLAMA_MODEL}")
        st.markdown(f"**Base URL:** {OLLAMA_BASE_URL}")
        st.markdown(f"**Temperature:** {OLLAMA_TEMPERATURE}")
        st.markdown(f"**Max Tokens:** {'Unlimited' if OLLAMA_NUM_PREDICT == -1 else OLLAMA_NUM_PREDICT}")
        st.markdown(f"**Embedding:** {EMBEDDING_MODEL}")
        st.markdown(f"**Chunk Size:** {CHUNK_SIZE}")
        st.markdown(f"**Chunk Overlap:** {CHUNK_OVERLAP}")
        st.markdown(f"**Retrieval Chunks:** {RETRIEVAL_K}")
        
        st.divider()
        
        # Check Ollama connection
        if check_ollama_connection():
            st.success("✅ Ollama is running")
        else:
            st.error("❌ Ollama is not running")
            st.markdown("**Start Ollama:**")
            st.code("ollama serve", language="bash")
            st.markdown(f"**Pull the model:**")
            st.code(f"ollama pull {OLLAMA_MODEL}", language="bash")
        
        st.divider()
        
        # PDF files info
        pdf_files = check_pdf_files()
        st.markdown(f"**PDF Files:** {len(pdf_files)}")
        for pdf in pdf_files:
            st.markdown(f"- {Path(pdf).name}")
        
        if st.button("🔄 Reload Documents"):
            st.cache_resource.clear()
            st.rerun()
    
    # Initialize RAG system
    if not check_ollama_connection():
        st.warning("⚠️ Please start Ollama server to use this application.")
        st.code("ollama serve", language="bash")
        st.stop()
    
    # Initialize with progress indicators
    with st.spinner("🚀 Initializing RAG system..."):
        result = initialize_rag_system()
    
    # Check for errors
    if result[0] is None:
        st.error(f"⚠️ {result[2]}")
        st.info("Please add PDF files to the 'resources' directory and restart the app.")
        st.stop()
    
    qa_chain, vectorstore, metadata = result
    
    # Show toast notifications only on first load (not from cache)
    if 'initialized' not in st.session_state:
        st.toast(f"📄 Found {metadata['pdf_count']} PDF file(s): {', '.join(metadata['pdf_names'])}", icon="📄")
        st.toast(f"✅ Loaded {metadata['doc_count']} pages from PDFs", icon="✅")
        st.toast(f"✅ Created {metadata['chunk_count']} text chunks", icon="✂️")
        st.toast(f"✅ Connected to Ollama model: {OLLAMA_MODEL}", icon="🤖")
        st.session_state.initialized = True
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    
    # Chat input
    if prompt := st.chat_input("Ask a question about your documents..."):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Add user message to history
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        
        # Generate response with streaming
        with st.chat_message("assistant"):
            try:
                # Create placeholder for streaming
                message_placeholder = st.empty()
                
                # Create streaming callback handler
                stream_handler = StreamHandler(message_placeholder)
                
                # Get response from QA chain with streaming
                with st.spinner("🔍 Searching documents..."):
                    result = qa_chain.invoke(
                        {"query": prompt},
                        config={"callbacks": [stream_handler]}
                    )
                    response = result['result']
                
                # Final update without cursor
                message_placeholder.markdown(response)
                
                # Optional: Show source documents
                with st.expander("📄 View Source Documents"):
                    for i, doc in enumerate(result.get('source_documents', []), 1):
                        st.markdown(f"**Source {i}:**")
                        st.text(doc.page_content[:300] + "...")
                        st.markdown(f"*Page: {doc.metadata.get('page', 'N/A')}*")
                        st.divider()
                
                # Add assistant message to history
                st.session_state.messages.append({
                    'role': 'assistant',
                    'content': response
                })
            
            except Exception as e:
                error_msg = f"❌ Error generating response: {str(e)}"
                st.error(error_msg)
                st.exception(e)


if __name__ == "__main__":
    main()
