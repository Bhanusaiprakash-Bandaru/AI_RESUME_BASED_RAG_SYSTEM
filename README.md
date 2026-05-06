# AI Resume-Based RAG System

An AI-powered Resume Question Answering System built using Retrieval-Augmented Generation (RAG).  
This application allows users to upload or use a resume PDF and ask questions in natural language.  
The system retrieves relevant information from the resume and generates accurate responses using OpenAI LLMs.

---

# Project Overview

This project uses:

- LangChain for orchestration
- OpenAI Embeddings for vector generation
- ChromaDB as vector database
- GPT-4o-mini as the LLM
- Streamlit for UI
- PyPDFLoader for PDF processing

The system converts resume content into embeddings and stores them in a vector database for semantic retrieval.

---

# Features

- Resume PDF processing
- Semantic search using vector embeddings
- Context-aware AI responses
- Streamlit-based interface
- ChromaDB vector storage
- OpenAI LLM integration
- Retrieval-Augmented Generation (RAG) pipeline

---

# Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Framework | LangChain |
| LLM | GPT-4o-mini |
| Embeddings | OpenAI Embeddings |
| Vector Database | ChromaDB |
| Frontend | Streamlit |
| PDF Loader | PyPDFLoader |
| Deployment | Hugging Face Spaces |

---

# Project Structure

```bash
AI-RESUME-RAG/
│
├── app.py
├── rag.py
├── requirements.txt
├── Resume.pdf
└── .env
```

---

# How the System Works

## Step 1 — Load Resume PDF

The resume PDF is loaded using PyPDFLoader.

```python
loader = PyPDFLoader("Resume.pdf")
documents = loader.load()
```

---

## Step 2 — Split Text into Chunks

The document is divided into smaller chunks for efficient retrieval.

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(documents)
```

---

## Step 3 — Generate Embeddings

OpenAI Embeddings convert text chunks into numerical vectors.

```python
embedding = OpenAIEmbeddings()
```

---

## Step 4 — Store Embeddings in ChromaDB

Embeddings are stored inside ChromaDB for semantic retrieval.

```python
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding
)
```

---

## Step 5 — Create Retriever

Retriever fetches relevant chunks based on user query.

```python
retriever = vectorstore.as_retriever()
```

---

## Step 6 — Initialize LLM

GPT-4o-mini is used to generate responses.

```python
llm = ChatOpenAI(model="gpt-4o-mini")
```

---

## Step 7 — Retrieve Relevant Context

Relevant document chunks are retrieved.

```python
retrieved_docs = retriever.invoke(query)
```

---

## Step 8 — Generate AI Response

The retrieved context is passed to the LLM.

```python
response = llm.invoke(prompt)
```

---

# Complete RAG Pipeline

```text
PDF → Text Chunks → Embeddings → Vector Database → Retriever → LLM → Final Response
```

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/your-username/AI-RESUME-RAG.git
```

---

## Move into Project Directory

```bash
cd AI-RESUME-RAG
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root directory.

Add:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Important Security Note

Never upload your `.env` file or API key to GitHub or Hugging Face.

Add `.env` inside `.gitignore`.

Example:

```bash
.env
```

Reason:
- API keys are private credentials
- Exposing keys can lead to unauthorized usage
- Your billing account may be charged if leaked

Always use:
- `.env` locally
- Hugging Face Secrets during deployment

---

# Run the Application

```bash
streamlit run app.py
```

---

# Example Questions

Users can ask questions such as:

- What projects has Bhanu Sai Prakash worked on?
- What technologies were used in the drowsiness detection system?
- What machine learning models were used for churn prediction?
- Compare the technologies used in computer vision vs NLP projects.
- Which project involves deep learning and what model was used?
- What tools were used for data visualization?

---

# Sample Outputs

## Query

```text
What technologies were used in the drowsiness detection system?
```

## Response

```text
The technologies used in the drowsiness detection system include:

- Python
- OpenCV
- NumPy
- Haar cascade classifiers
- Eye Aspect Ratio (EAR)
- Live webcam feed integration
```

---

## Query

```text
Which project involves deep learning and what model was used?
```

## Response

```text
The project involving deep learning is the BERT-Based Named Entity Recognition (NER) System.

The model used was DistilBERT from HuggingFace Transformers.
```

---

## Query

```text
What tools were used for data visualization?
```

## Response

```text
The tools used for data visualization are:

- Power BI
- Pandas
- NumPy
```

---

# Deployment on Hugging Face

## Upload Files

Upload:
- app.py
- rag.py
- requirements.txt
- Resume.pdf

---

## Add Secret

Go to:

```text
Settings → Variables and secrets
```

Add:

```text
OPENAI_API_KEY
```

Paste your OpenAI API key as the value.

---

## Commit Changes

Click:

```text
Commit changes to main
```

Deployment starts automatically.

---

# requirements.txt

```text
streamlit
langchain
langchain-openai
langchain-community
langchain-chroma
langchain-text-splitters
chromadb
openai
pypdf
python-dotenv
```

---

# Future Improvements

- Multi-PDF support
- Conversational memory
- Source citation
- Hybrid search
- Reranking
- Chat history
- Multi-user support
- Agentic AI workflows

---

# Learning Outcomes

This project demonstrates understanding of:

- Retrieval-Augmented Generation (RAG)
- Vector databases
- Embeddings
- Semantic search
- LangChain pipelines
- LLM integration
- Streamlit deployment
- AI application deployment

---

# Tags

`#GenerativeAI`  
`#RAG`  
`#LangChain`  
`#OpenAI`  
`#Streamlit`  
`#ChromaDB`  
`#LLM`  
`#Python`  
`#ArtificialIntelligence`  
`#MachineLearning`  
`#SemanticSearch`  
`#HuggingFace`  
`#VectorDatabase`  
`#NLP`  
`#AIProjects`
