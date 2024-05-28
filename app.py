from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"

#Write the prompt
prompt = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful assistant. Please respond to the human user funnily."),
    ('user', 'Question:{question}')
]
)

#streamlit framework
st.title("Chatbot with Lanchain and Langsmith")
input_text = st.text_input("Ask off..")

#Call model and create output parser for chaining
llm_model = Ollama(model="llama2")
output_parser = StrOutputParser()

#Chaining
chain = prompt | llm_model | output_parser

if input_text:
    response = chain.invoke({'question':input_text})
    st.write(response)