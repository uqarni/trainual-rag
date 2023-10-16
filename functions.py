import openai


#similarity search
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pandas as pd

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

def find_txt_examples(query, k=8):
    loader = TextLoader("docs.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings()

    db = FAISS.from_documents(docs, embeddings)
    docs = db.similarity_search(query, k=k)

    examples = ""
    for doc in docs:
       examples += '\n\n' + doc.page_content
    return examples


def responder(examples, query):
    messages = []
    prompt = {
        'role': 'system',
        'content': f'You work for Trainual, which sells a SaaS product designed to help businesses onboard their employees faster. Your job is to answer the question based on the following documentation excerpts:\n\n{examples}'
    }
    user_input = {'role': 'user', 'content': query}

    messages.append(prompt)
    messages.append(user_input)

    response = openai.ChatCompletion.create(
        model = 'gpt-4',
        temperature = 0,
        messages = messages,
        max_tokens = 300
    )
    return response["choices"][0]["message"]["content"]
