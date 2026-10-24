from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from .env

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",  # your Azure deployment name
    base_url="https://mychatbot2.openai.azure.com/openai/v1",
    dimensions=32,
    check_embedding_ctx_length=False
)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))