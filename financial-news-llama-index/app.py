import os, config
from llama_index import GPTVectorStoreIndex, StorageContext, load_index_from_storage
os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY

import streamlit as st
from llama_index import ServiceContext, LLMPredictor
# from openai import OpenAI
from langchain.llms import OpenAI

llm = OpenAI(model_name='gpt-4', max_tokens=6000)

llm_predictor = LLMPredictor(llm=llm)

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# index = GPTVectorStoreIndex.load_from_disk('index_news.json', service_context=service_context)
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()

st.title('Fintama')

st.header("Financial Assistant")

report_type = st.selectbox(
    'Select data source?',
    ('ChatGPT', 'Fintama'))

if report_type == 'Fintama':
    symbol = st.text_input("How can I help You ?")

    if symbol:
        with st.spinner(f'We are looking for the answer for {symbol}...'):
            response = query_engine.query(f"{symbol}")

            st.write(str(response))


if report_type == 'Single Stock Outlook':
    symbol = st.text_input("Stock Symbol")

    if symbol:
        with st.spinner(f'Generating report for {symbol}...'):
            response = query_engine.query(f"Write a report on the outlook for {symbol} stock from the years 2023-2027. Be sure to include potential risks and headwinds.")

            st.write(response)

if report_type == 'Competitor Analysis':
    symbol1 = st.text_input("Stock Symbol 1")
    symbol2 = st.text_input("Stock Symbol 2")

    if symbol1 and symbol2:
        with st.spinner(f'Generating report for {symbol1} vs. {symbol2}...'):
            response = query_engine.query(f"Write a report on the competition between {symbol1} stock and {symbol2} stock.")

            st.write(response)




