#file upload
file= "C:\\Users\\prade\\Videos\\RESUME\\pradeep new (AutoRecovered).pdf"

# Local PDF file uploads
if file:
  local = UnstructuredPDFLoader(file_path=file)
  pdf  = local.load()
else:
  print("Upload a PDF file")



#Vector Embeddings
!ollama pull nomic-embed-text
!ollama list

text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100)
chunks = text_splitter.split_documents(pdf)


# Add to vector database
vector_db = Chroma.from_documents(
    documents=chunks, 
    embedding=OllamaEmbeddings(model="nomic-embed-text",show_progress=True),
    collection_name="local-rag"
)


# LLM from Ollama
local_model = "mistral"
llm = ChatOllama(model=local_model)



QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant. Your task is to generate five
    different versions of the given user question to retrieve relevant documents from
    a vector database. By generating multiple perspectives on the user question, your
    goal is to help the user overcome some of the limitations of the distance-based
    similarity search. Provide these alternative questions separated by newlines.
    Original question: {question}""",
)

retriever = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(), 
    llm,
    prompt=QUERY_PROMPT
)

# RAG prompt
template = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)


chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)



chain.invoke("how is the owner of the resume")
chain.invoke("show pradeep skills")
