from imports import Oembeddings

def get_embedding(text):
    try:
        model_name="granite-embedding:278m"
        embed_model = Oembeddings(model=model_name)
        embedding_vector = embed_model.embed_query(text)
        return embedding_vector
    except Exception as e:
        return f"Error occurred while getting embedding: {str(e)}"
