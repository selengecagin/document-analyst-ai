import streamlit as st



def main():
   st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:", layout="wide")

   st.header("Chat with multiple PDFs :books:")
   st.text_input("Ask a question about your documents:")

   # Sidebar to users upload the PDFs, with for put things inside the sidebar
   with st.sidebar:
       st.subheader("Your Documents")
       st.file_uploader("Upload your PDFs here and click on 'Process'", type="pdf", accept_multiple_files=True)
       st.button("Process")


if __name__ == '__main__':
    main()