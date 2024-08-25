import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplate import css, bot_template, user_template

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vector_store

def get_conversation_chain(vector_store):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain

def main():
    load_dotenv()

    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:", layout="wide")

    # add custom css*
    st.write(css, unsafe_allow_html=True)

    if"conversation" not in st.session_state:
        st.session_state.conversation = None

    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents:")

    # display the chat messages*
    st.write(user_template.replace("{{MSG}}", "Hello robot"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello human"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", type="pdf", accept_multiple_files=True)
        if st.button("Process"):
           with st.spinner("Processing your documents..."):
            # get pdf text
            raw_text = get_pdf_text(pdf_docs)

            # get text chunks
            text_chunks = get_text_chunks(raw_text)

            # create vector store
            vector_store = get_vector_store(text_chunks)

            # create conversation chain, it takes history of the conv. and returns the next element in the conv.
            # session state is used to store the conversation chain -this variable is not supposed to be re-initialized
            # streamlit usually load all code from scratch when the page is refreshed
            # session_state is used to store the conversation chain -this variable is not supposed to be re-initialized
            st.session_state.conversation = get_conversation_chain(vector_store)
            st.success("Documents processed successfully!")


if __name__ == '__main__':
    main()