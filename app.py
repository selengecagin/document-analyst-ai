import streamlit as st



def main():
   st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:", layout="wide")

   st.header("Chat with multiple PDFs :books:")
   st.text_input("Ask a question about your documents:")


if __name__ == '__main__':
    main()