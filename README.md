# RAG-Based YouTube Chatbot
A web application that enables users to interact with and ask questions about a YouTube video's content, powered by a Retrieval-Augmented Generation (RAG) architecture.


Try it out : <a href="[Your Live URL Here]" target="_blank">Live</a>


<hr>

## Table of Contents
- Introduction
- Features
- Dataset Description
- Technologies Used
- Installation
- Project Structure
- Usage
- Results
- Demo

<hr>

## 1. Introduction
The RAG-Based YouTube Chatbot project utilizes a conversational AI framework to provide answers to user queries based directly on a video's transcript. The tool is designed to offer a reliable and context-aware Q&A experience by preventing the AI model from generating information outside of the provided content.

<hr>

## 2. Features
- A web application built with the Streamlit framework that allows users to ask questions about a YouTube video.
- Utilizes a **Retrieval-Augmented Generation (RAG)** architecture to provide answers directly from a video's transcript, preventing hallucinations.
- The application processes transcripts in English and Hindi, providing a responsive and accurate conversational experience.
- Developed using LangChain and the Google Generative AI API for efficient document loading and model integration.

<hr>

## 3. Dataset Description
The project does not use a fixed dataset. Instead, it dynamically loads video transcripts from YouTube in real-time. This dynamic knowledge base is then processed and used as the context for generating answers.

<hr>

## 4. Technologies Used
#### Programming Language: 
- Python
#### Frameworks and Libraries:
- Streamlit (for the web interface)
- LangChain (for the RAG framework)
- LangChain-Google-GenAI (for LLMs and embeddings)
- LangChain-Groq (for LLM integration)
- UnstructuredURLLoader (for data extraction)
- FAISS (for vector storage)
- Python-dotenv (for environment management)

<hr>

## 5. Installation
#### Follow these steps to set up the project locally:

1. Clone the repository:<br>
```bash
git clone [https://github.com/yashsahu02/RAG-Based_YouTube_Chatbot.git](https://github.com/yashsahu02/RAG-Based_YouTube_Chatbot.git)
Navigate to the project directory:<br>

Install the dependencies:<br>

Bash

pip install -r requirements.txt
<hr>


