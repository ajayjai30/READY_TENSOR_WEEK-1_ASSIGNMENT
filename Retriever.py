from file_to_text import pdf_to_text
from imports import Rct
from embeddings import get_embedding
from database import store_embedding


def retrieve_and_store_embeddings(pdf_path):
    #Extracting text from the PDF file
    text = pdf_to_text(pdf_path)
    if not text:
        return "No text extracted from the PDF."
    #Splitting the text into smaller chunks
    text_splitter = Rct(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(text)
    if not texts:
        return "No text chunks created from the PDF."
    #Storing the embeddings in the database
    for text in texts:
        embedding = get_embedding(text)
        if isinstance(embedding, str):
            print(f"Error generating embedding for text chunk: {embedding}")
            continue    
        store_result = store_embedding(text, embedding)
        if not store_result:
            print(f"Error storing embedding for text chunk: {text}")
        else:
            print(f"Successfully stored embedding for text chunk: {text[:50]}...")  
    return store_result
