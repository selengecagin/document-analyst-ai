# Document Analyst: Your Intelligent PDF Companion

## Overview

The Document Analyst is a sophisticated Python application that revolutionizes your interaction with multiple PDF documents. This powerful tool enables you to engage in natural language conversations about the content of your PDFs, providing an intuitive and efficient way to extract information and insights.

## How It Works
------------
![Document Analyst App Diagram](./docs/document-analyst-ai.png)

1. PDF Processing: The app efficiently extracts text from multiple uploaded PDF documents.
2. Text Segmentation: The extracted text is intelligently divided into manageable parts for effective processing.
3. Semantic Encoding: An advanced language model converts text parts into rich vector representations (embeddings).
4. Relevance Matching: When asked, the app swiftly identifies the most semantically similar text parts.
5. Intelligent Response: The app leverages the language model to generate a coherent answer based on the relevant PDF content and the user's query.
6. Contextual Conversation: The system maintains conversation history, enabling follow-up questions and more natural interactions.

## Dependencies and Installation
----------------------------
To install the Document Analyst App, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_secrit_api_key

## Usage
-----
To use the Document Analyst App, follow these steps:

1. Ensure you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Load multiple PDF documents into the app by following instructions.

5. Ask questions in natural language about the loaded PDFs using the chat interface.

