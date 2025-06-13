from imports import Ppdf,os
#ppdf for loading PDF files
def pdf_to_text(pdf_path):
    """
    Extract text from a PDF file using Langchain's PyPDFLoader.
    
    Args:
        pdf_path (str): Path to the PDF file.
        
    Returns:
        str: Extracted text from the PDF.
    """
    pdf_path = os.path.normpath(pdf_path)
    loader = Ppdf(pdf_path)
    documents = loader.load()
    text = ""
    for doc in documents:
        text += doc.page_content + "\n"
    return text

