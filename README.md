# RAG-Based YouTube Chatbot
A web application that enables users to interact with and ask questions about a YouTube video's content, powered by a Retrieval-Augmented Generation (RAG) architecture.


<!-- Try it out : <a href="[Your Live URL Here]" target="_blank">Live</a> -->


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
```
2. Navigate to the project directory:<br>

3. Install the dependencies:<br>

```bash

pip install -r requirements.txt

``` 
<hr>

## 6. Project Structure
```
📂 RAG_Based_YouTube_Chatbot
 ├── 📄 app.py
 ├── 📄 .env
 ├── 📄 .gitignore
 ├── 📄 requirements.txt
 └── 📄 README.md
```

<hr>

## 7. Usage
Run the application:

```bash
streamlit run app.py
```
Here app.py is name of python file.

Use the web interface to:
Enter a YouTube video URL.
<br>
Wait for the transcript to load.

Ask questions about the video's content in the chat interface.

<hr>

## 8. Results
The RAG architecture ensures all generated responses are grounded in the video's content, providing accurate and reliable information.

By utilizing Google Gemini's gemini-2.0-flash model, the chatbot offers near-instantaneous, low-latency responses.

This project successfully demonstrates an effective method for providing context-aware Q&A from unstructured video data, effectively mitigating model hallucinations.

<hr>

## 9. Demo
Watch the full project demo:



<hr>

Screenshots

<hr>

<hr>

<hr>

<br>

## Yash Sahu
<a href="https://www.linkedin.com/in/yashsahu02" target="_blank">LinkedIn</a>
<br>
<a href="https://www.kaggle.com/yashsahu02" target="_blank">Kaggle</a>











