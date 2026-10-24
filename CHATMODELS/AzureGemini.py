from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # loads GOOGLE_API_KEY from .env

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.8,
    max_output_tokens=90
)

result = model.invoke("What is the capital of India")

print(result.content)