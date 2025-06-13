import os
from Retriever import retrieve_and_store_embeddings

def process_all_pdfs_in_data_folder(data_folder="data"):
    """
    Process all PDF files in the specified data folder:
    - Extract text, generate embeddings, and store them in the database.
    """
    if not os.path.exists(data_folder):
        print(f"Data folder '{data_folder}' does not exist.")
        return

    pdf_files = [f for f in os.listdir(data_folder) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print(f"No PDF files found in '{data_folder}'.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(data_folder, pdf_file)
        print(f"Processing file: {pdf_path}")
        result = retrieve_and_store_embeddings(pdf_path)
        print(f"Result: {result}")

if __name__ == "__main__":
    process_all_pdfs_in_data_folder()
