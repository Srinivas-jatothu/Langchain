import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Check API key
if not api_key:
    raise ValueError("Missing OPENROUTER_API_KEY in .env")

# Set up the model
llm = ChatOpenAI(
    model_name="google/gemini-flash-1.5",  # or any OpenRouter-supported model
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=1.9,
    max_completion_tokens=10
)

# Prompt setup
prompt = ChatPromptTemplate.from_template("Write a short essay (5 lines) about MS Dhoni.")
chain = prompt | llm

# Get and print only the answer content
response = chain.invoke({})
# print(response)


print(response.content)  # Print only the content of the response