from imports import RQA
from Prompt_template_for_LLM import QA_Prompt_template
from database import get_retriever
from imports import Collama,StreamingStdOutCallbackHandler

def get_rag_chain():
    retriever = get_retriever()
    llm = Collama(model="granite3.1-moe:1b",streaming=True,callbacks=[StreamingStdOutCallbackHandler()]) 

    rag_chain = RQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": QA_Prompt_template}
    )
    return rag_chain

    
