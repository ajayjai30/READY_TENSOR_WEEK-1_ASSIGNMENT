from imports import gr
from RAG_pipeline import get_rag_chain
import time


# Initializing once to avoid reloading every time
rag_chain = get_rag_chain()

#generator function to handle streaming responses
def chat_with_rag(message, history):
    response = ""
    for chunk in rag_chain.stream({"query": message}):
        if isinstance(chunk, dict) and "result" in chunk:
            partial = chunk["result"]
            for word in partial.split():
                response += word + " "
                yield response
                time.sleep(0.1)



# chat interface setup
interface= gr.ChatInterface(
    fn=chat_with_rag,
    title="Research Paper Q&A with RAG",
    description="Get instant answers and explanations for your research papers using this Retrieval-Augmented Generation (RAG) tool. Simply upload your document and ask questions to understand its content better.",
    examples=["What is the document about?", "Explain the main idea in simple words."]
)

if __name__ == "__main__":
    interface.launch(share=True,debug=True)