# WatsonX PDF Q&A Streamlit App

This Streamlit app is designed to perform Q&A on the content of a PDF document using IBM WatsonX's LLM and LangChain. By uploading a PDF file, users can ask questions about the content, and the app will respond with relevant answers from the document.

## Features

- **PDF Document Loading**: Load and index PDF files for question-answering.
- **Embeddings & Text Splitting**: Use Hugging Face embeddings for semantic search and split text using LangChain's `RecursiveCharacterTextSplitter`.
- **Q&A with IBM WatsonX**: Integrate with IBM WatsonX's LLM to answer questions based on the PDF content.
- **Interactive Chat Interface**: Uses Streamlit's chat interface to display responses and retain chat history.

## Setup and Installation

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html) (recommended) or Python >= 3.10
- IBM WatsonX API access credentials

### Step 1: Clone the Repository

```bash
git clone https://github.com/WalkingDevFlag/PDF-QA-Chatbot
cd <repository-directory>
```

### Step 2: Create and Activate the Conda Environment

```bash
conda create --name watsonx python=3.10
conda activate watsonx
```

### Step 3: Install Dependencies

Use the `requirements.txt` file to install necessary packages:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory with the following variables:

```plaintext
WATSONX_APIKEY=your_watsonx_apikey
WATSONX_URL=your_watsonx_url
WATSONX_MODEL_ID=your_model_id
WATSONX_PROJECT_ID=your_project_id
```
Replace each placeholder with your actual IBM WatsonX API key, URL, Model ID, Project ID, and the path to your PDF file.

### Step 5: Add the pdf files in the resources directory

Make sure the pdfs you want to run on are present in the "resources" directory

## Usage

1. **Start the App**:

   ```bash
   streamlit run app.py
   ```

2. **Interact with the Q&A System**:
   - The app provides a chat interface. Enter your questions related to the PDF content, and WatsonX will generate responses based on the indexed document.

3. **Historical Messages**:
   - All past questions and answers are displayed in the chat interface, allowing for a seamless Q&A session.

## Environment Setup with Conda

To create a Conda environment with the necessary packages, follow these commands:

```bash
conda create --name watsonx python=3.10
conda activate watsonx
pip install -r requirements.txt
```

## File Structure

- **app.py**: Main script to run the Streamlit app.
- **.env**: Environment file containing IBM WatsonX credentials.
- **requirements.txt**: List of Python packages required for the project.

## Acknowledgments

- [IBM WatsonX](https://www.ibm.com/cloud/watsonx) for API and LLM capabilities.
- [LangChain](https://github.com/hwchase17/langchain) for document loading, embeddings, and retrieval chains.
- [Streamlit](https://streamlit.io/) for the user interface and chat capabilities.
- Generate you WatsonX API-KEYS [here](https://cloud.ibm.com/iam/apikeys)
- Get you Project_id [here](https://eu-de.dataplatform.cloud.ibm.com/wx/home?context=wx)
- [Langchain IBM watsonx.ai documentation](https://python.langchain.com/docs/integrations/llms/ibm_watsonx/)

