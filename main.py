from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_ibm import WatsonxLLM
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from the .env file
load_dotenv()

# Retrieve environment variables
watsonx_apikey = os.getenv("WATSONX_APIKEY")
watsonx_url = os.getenv("WATSONX_URL")
watsonx_model_id = os.getenv("WATSONX_MODEL_ID")
watsonx_project_id = os.getenv("WATSONX_PROJECT_ID")

llm = WatsonxLLM(
    model_id=watsonx_model_id,
    url=watsonx_url,
    params={"decoding_method": "greedy", "max_new_tokens": 500},
    project_id=watsonx_project_id,
)
script_dir = os.path.dirname(__file__)
directory = os.path.join(script_dir, 'resources')
@st.cache_resource
def load_pdf():
    loaders = [PyPDFDirectoryLoader(directory)]
    index = VectorstoreIndexCreator(
        embedding=HuggingFaceEmbeddings(model_name='all-MiniLM-L12-v2'),
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    ).from_loaders(loaders)
    return index

index = load_pdf()

# Create a QnA chain
chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=index.vectorstore.as_retriever(),
    input_key='question'
)

# App Title
st.title("A Student's Guide :)")

# Setup a session state message variable to hold all the old messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Build a prompt input template to display the prompts
prompt = st.chat_input('Pass Your Prompt Here')

if prompt:
    # Display the prompt
    st.chat_message('user').markdown(prompt)
    # Store the user prompt in state
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    # Send the user prompt to the llm
    response = chain.run(prompt) 
    # Show the llm response
    st.chat_message('assistant').markdown(response)
    # Store the llm response in state
    st.session_state.messages.append({'role': 'assistant', 'content': response})
