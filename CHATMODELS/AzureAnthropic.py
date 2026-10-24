from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # loads ANTHROPIC_API_KEY from .env

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",  # your Azure deployment name
    base_url="https://mychatbot2.services.ai.azure.com/anthropic",
    temperature=0.2,
    max_tokens=90
)

result = model.invoke("What is the capital of India")

print(result.content)