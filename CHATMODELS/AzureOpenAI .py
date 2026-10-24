from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from .env

llm = ChatOpenAI(
    model="gpt-4.1-mini",  
    base_url="https://mychatbot2.openai.azure.com/openai/v1",
    temperature =1.8,
    max_completion_tokens =90
)


result = llm.invoke("write story")
print(result.content)