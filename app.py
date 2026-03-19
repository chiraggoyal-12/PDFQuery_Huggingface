import os

import cassio
import streamlit as st
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Cassandra
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from PyPDF2 import PdfReader

# -------------------- LOAD SECRETS --------------------
ASTRA_DB_APPLICATION_TOKEN = st.secrets["ASTRA_DB_APPLICATION_TOKEN"]
ASTRA_DB_ID = st.secrets["ASTRA_DB_ID"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# -------------------- INIT --------------------
cassio.init(
    token=ASTRA_DB_APPLICATION_TOKEN,
    database_id=ASTRA_DB_ID
)

# -------------------- UI --------------------
st.set_page_config(page_title="PDF Chat App")
st.title("📄 Chat with your PDF (LangChain + AstraDB)")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# -------------------- PROCESS PDF --------------------
def process_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    return text_splitter.split_text(text)

# -------------------- VECTOR STORE --------------------
def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings(
        openai_api_key=OPENAI_API_KEY,
        model="text-embedding-3-small"
    )

    vstore = Cassandra(
        embedding=embeddings,
        table_name="pdf_qa_demo",
    )

    vstore.add_texts(chunks)
    return vstore

# -------------------- MAIN --------------------
if uploaded_file is not None:
    with st.spinner("Processing PDF..."):
        chunks = process_pdf(uploaded_file)
        vstore = create_vector_store(chunks)

    st.success("✅ PDF processed!")

    query = st.text_input("Ask something about the PDF:")

    if query:
        with st.spinner("Thinking..."):
            docs = vstore.similarity_search(query, k=3)

            llm = ChatOpenAI(
                temperature=0,
                openai_api_key=OPENAI_API_KEY
            )

            chain = load_qa_chain(llm, chain_type="stuff")

            response = chain.run(
                input_documents=docs,
                question=query
            )

        st.subheader("📌 Answer")
        st.write(response)
