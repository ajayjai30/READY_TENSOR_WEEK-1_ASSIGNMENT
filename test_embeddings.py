from embeddings import get_embedding
from database import store_embedding

def test_get_embedding(text):
    try:
        result = get_embedding(text)
        if isinstance(result, str) and result.startswith("Error occurred"):
            print(f"Embedding generation failed for input '{text}': {result}")
            return None
        print(f"Embedding generated successfully for input '{text}'. Length: {len(result)}")
        return result
    except Exception as e:
        print(f"Exception during embedding generation for input '{text}': {str(e)}")
        return None

def test_store_embedding(key, embedding):
    try:
        if embedding is None:
            print(f"No embedding to store for key '{key}'.")
            return
        store_result = store_embedding(key, embedding)
        print(f"Store embedding result for key '{key}': {store_result}")
    except Exception as e:
        print(f"Exception during storing embedding for key '{key}': {str(e)}")

if __name__ == "__main__":
    test_cases = [
        "This is a test sentence to generate embeddings.",
        "",
        "a" * 10000,  # very long text
        "!@#$%^&*()_+-=[]{}|;':,.<>/?`~",  # special characters
        None  # invalid input
    ]

    for i, text in enumerate(test_cases):
        print(f"\nTest case {i+1}:")
        embeddings = test_get_embedding(text)
        test_store_embedding(f"test_key_{i+1}", embeddings)
