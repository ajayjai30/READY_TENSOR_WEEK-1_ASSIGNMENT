from imports import Chroma,Oembeddings

# Initialize or connect to the Chroma vector store
ollama_embedding_instance=Oembeddings(model="granite-embedding:278m")
chroma = Chroma(persist_directory="./chroma_db",embedding_function=ollama_embedding_instance)
def store_embedding(key: str, embedding: list):
    """
    Store the embedding vector in the chroma database with the given key.
    """
    try:
        chroma.add_texts(texts=[key], embeddings=[embedding])
        #chroma.persist()
        return "Embedding stored successfully."
    except Exception as e:
        return f"Error storing embedding: {str(e)}"
def get_retriever():
    """
    Returns a retriever object from the Chroma vector store.
    """
    return chroma.as_retriever(kwargs={"search_type": "similarity", "search_kwargs": {"k": 5}})#this k helps in getting the top 5 similar results from the database
