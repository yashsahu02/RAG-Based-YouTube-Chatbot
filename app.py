# import required libraries 
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import YoutubeLoader
from youtube_transcript_api import YouTubeTranscriptApi 

import streamlit as st
import os
import sys 

# It is crucial to run this at the very top of the script before any langchain components.
import asyncio
def _ensure_event_loop():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

_ensure_event_loop()

# import environment variables
from dotenv import load_dotenv
load_dotenv()


# Streamlit session state initialization 
# """
# LangChain needs to store some information like (user prefereance, temporary data related to their session) these data 
# can't be mentained without the use of st.session_state 

# if we don't use st.session for below then on every button click or on action page refereshes which results in loss of these data 

# """

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []
if 'video_id' not in st.session_state:
    st.session_state['video_id'] = None
if 'transcript_list' not in st.session_state:
    st.session_state['transcript_list'] = None
if 'transcript' not in st.session_state:
    st.session_state['transcript'] = None
if 'retriever' not in st.session_state:
    st.session_state['retriever'] = None
if 'chain' not in st.session_state:
    st.session_state['chain'] = None


st.title("YouTube ChatBot RAG")
st.header("Enter the Video URL")
video_url = st.text_input("", key="user_input")
video_id = video_url.split("v=")[-1].split("&")[0]
st.caption("Languages Supports: Hindi and English")
button = st.button("Submit")
st.divider()


# check whether the URL is valid or not after clicking submit button 
if button:
    if not video_url:
        st.error("URL is required. Please enter a video URL.")
    else:
        try:
            ytt_api = YouTubeTranscriptApi()
            transcript_list = ytt_api.fetch(video_id,
                                            languages=['hi','en']
                                            )

            # Convert loaded transcript_list to a single transcript string using join 
            transcript = " ".join([doc.text for doc in transcript_list])
            
            # Update session state with new video data such as video_id, transcript and transcript_list 
            st.session_state['video_id'] = video_url.split("v=")[-1].split("&")[0]
            st.session_state['transcript'] = transcript
            st.session_state['transcript_list'] = transcript_list 
            
            # st.subheader("Transcript ->")
            # st.write(st.session_state['transcript'])
            
            st.success("Transcript loaded successfully! You can now ask questions.")

            # --- RAG Pipeline ---
            
            # text splitter 
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            
            # chunks 
            chunks = text_splitter.create_documents([st.session_state['transcript']])
            
            # embeddings and vectore store 
            embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", request_timeout=120)
            vectore_store = FAISS.from_documents(chunks, embeddings)
            
            st.session_state['retriever'] = vectore_store.as_retriever(search_type="similarity", search_kwargs={'k': 2})
            
            # defining the model using 'gemini-2.0-flash' of Google 
            llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
            
            # defining the prompt 
            prompt = PromptTemplate(
                template="""
                You are a helpful assistant. Answer only from the provided transcript context.
                If the context is insufficient or if the answer is not present in the context, respond exactly with just say -> I couldn't find that information in the video. My knowledge is limited to what's in this video's transcript, so please try asking a different question about its content. \n
                context: {context} \n
                Question: {question}
                """,
                input_variables=['context', 'question']
            )
            
            # parser 
            parser = StrOutputParser()
            st.session_state['chain'] = prompt | llm | parser

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.warning("Please ensure the URL is valid and the video has an English or Hindi transcript.")
            
            # Clear state on error
            st.session_state['video_id'] = None
            st.session_state['transcript'] = None
            st.session_state['retriever'] = None
            st.session_state['chain'] = None


# Display message history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])

# Chat functionality
if st.session_state['retriever'] and st.session_state['chain']:
    user_query = st.chat_input("Ask anything about the video...")
    if user_query:
        st.session_state['message_history'].append({'role': 'user', 'content': user_query})
        with st.chat_message('user'):
            st.write(user_query)
        
        retrieved_docs = st.session_state['retriever'].invoke(user_query)
        context = "\n\n".join(doc.page_content for doc in retrieved_docs)
        
        assistant_response = st.session_state['chain'].invoke({'context': context, 'question': user_query})
        
        st.session_state['message_history'].append({'role': 'assistant', 'content': assistant_response})
        with st.chat_message('assistant'):
            st.write(assistant_response)