#All the library imports for the project are listed here
import os                                                                                  #used for handling file paths and directories
import sys                                                                                 #used for system-specific parameters and functions
import re                                                                                  #used for regular expressions
from langchain_ollama import ChatOllama as Collama                                         #ChatOllama is used to interact with the Ollama API for chat-based models
from langchain_ollama import OllamaEmbeddings as Oembeddings                               #OllamaEmbeddings is used to get embeddings from the Ollama API``
from PyPDF2 import PdfReader as Pr                                                         #Pdf Reader is used to read PDF files
from langchain_chroma import Chroma                                                        #Chroma is used to store and retrieve embeddings
from langchain_community.document_loaders import PyPDFLoader as Ppdf                       #PyPDFLoader is used to load PDF files
from langchain.text_splitter import RecursiveCharacterTextSplitter as Rct                  #RecursiveCharacterTextSplitter is used to split text into smaller chunks
from langchain.chains import RetrievalQA as RQA                                            #RetrievalQA is used to create a question-answering chain
from langchain_core.messages import HumanMessage as Hm                                     #HumanMessage is used to create a message from the user
from langchain_core.prompts import PromptTemplate as Pt                                    #PromptTemplate is used to create a prompt for the model
import textwrap as textwrap                                                                #textwrap is used to format text
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler            #StreamingStdOutCallbackHandler is used to stream the output to the console
import gradio as gr                                                                        #gradio is used to create a web interface for the application