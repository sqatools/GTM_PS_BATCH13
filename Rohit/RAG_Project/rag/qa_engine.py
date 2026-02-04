from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter

def get_rag_chain():
    loader = TextLoader("Data/insurance_policy.txt")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    llm = ChatOpenAI(temperature=0)

    # Create retriever
    retriever = vectorstore.as_retriever()
    
    # Create prompt for the chain
    template = """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, say that you don't know.

Context: {context}

Question: {input}

Answer:"""
    
    prompt = ChatPromptTemplate.from_template(template)
    
    # Create the chain using LCEL (LangChain Expression Language)
    rag_chain = (
        {"context": retriever | (lambda docs: "\n".join([d.page_content for d in docs])), "input": RunnablePassthrough()}
        | prompt
        | llm
    )
    
    # Wrap to return both answer and context
    def run_chain(input_text):
        answer = rag_chain.invoke(input_text)
        context = retriever.invoke(input_text)
        return {
            "answer": answer.content if hasattr(answer, 'content') else str(answer),
            "context": context
        }
    
    return run_chain
