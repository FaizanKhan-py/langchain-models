from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from .env

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",  # your Azure deployment name
    base_url="https://mychatbot2.openai.azure.com/openai/v1",
    dimensions=32,
    check_embedding_ctx_length=False
)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))