from langchain_core.prompts import PromptTemplate 
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from youtube_transcript_api import YouTubeTranscriptApi 

import os
from dotenv import load_dotenv
load_dotenv()

print("API Key:",os.getenv("GOOGLE_API_KEY"))

## Step 1 : Indexing (Documnet Ingestion)

video_url = input("Enter the Video URL that you want to know about...") ## pass the youtube video url here 

video_id = video_url.split("v=")[-1].split("&")[0]

try:
    # transcript_list = ytt_api.fetch(video_id)
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.fetch(video_id,
                                    languages=['hi','en']
                                    ) # for hi because trying with hindi video
                                        
except Exception as e:
    print("Unable to extract transcript")
    print("Error -> ", e)
    
def get_transcript(transcript_list):
    transcript = " ".join(chunk.text for chunk in transcript_list)
    return transcript

## getting transcript (all the text from each chunk in transcript_list)
transcript = get_transcript(transcript_list)


## Step 1 - Indexing(Text Splitting)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) 
chunks = text_splitter.create_documents([transcript])


## Step 1 - Indexing (Embedding Generation and storing in Vecotor Scores)

embeddings = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001",request_timeout=120)

## create vector store
vectore_store = FAISS.from_documents(chunks,embeddings)


## Step 2 - Retriever 
retriever = vectore_store.as_retriever(search_type="similarity", seach_kwargs={'k':2})  # k:2 means retrieve most similar two chunks or para



## define the query or question of user 
question = input("Ask anything related to the video you provided url: ")


## looping from here 
while(question!='Q'):
    retrieved_docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in retrieved_docs)


    ## Step - 3 (Augmentation)

    # define the llm or model
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

    # define the prompt using prompt template 
    prompt = PromptTemplate(
        template="""
        You are a helpful assistent. Answer only from the provided transcript context. 
        If the context is insufficient or If the answer is not present in the context, respond exactly with just say The provided context doesn’t contain information to answer your question.
        {context} \n
        Question: {question}
        
        """,
        input_variables=['context','question']
    )

    # define parser
    from langchain_core.output_parsers import StrOutputParser

    parser = StrOutputParser()

    # Build the chain properly
    chain = prompt | llm | parser

    # Now invoke the chain with input variables
    ans = chain.invoke({'context': context, 'question': question})

    print("Response Final -> \n", ans)
    
    question = input("Ask anything related to the video you provided url: ")