from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# Load PDF
loader = PyPDFLoader("Resume.pdf")
documents = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(documents)

# Embeddings
embedding = OpenAIEmbeddings()

# Store vectors
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding
)

# Retriever
retriever = vectorstore.as_retriever()

# LLM
llm = ChatOpenAI(model="gpt-4o-mini")


def get_response(query):
    retrieved_docs = retriever.invoke(query)

    context = "\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = f"""
    Answer based only on the provided context.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content