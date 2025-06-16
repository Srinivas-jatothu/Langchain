import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import streamlit as st
from langchain_core.prompts import PromptTemplate , load_prompt

# Load .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Set up the LangChain model
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    model="google/gemini-flash-1.5"
)

# Streamlit UI
st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)


template = load_prompt("research_paper_summarizer_template.json")
# Format the prompt
prompt = template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=length_input
)

# Submit button
if st.button('Summarize Paper'):
    result = llm.invoke([HumanMessage(content=prompt)])
    st.write(result.content)
