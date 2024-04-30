# private-Ai
1.Development of RAG Pipeline: This is the core system i have  built. It's designed to allow users to interact with PDF files in a conversational manner, even without an internet connection.

2.Integration of Retrieval Component with Mistral Llama Model: 
I combined two different technologies seamlessly. The Mistral Llama model likely handles the generation of responses, while the retrieval component helps find relevant information within the PDF files.


![Untitled Diagram](https://github.com/JayaPradhi/private-Ai/assets/127920413/d7193071-4a44-4258-a5c8-1a58f994475b)


3.PDF File Handling: The pipeline is able to load PDF files using the UnstructuredPDFLoader. This means it can access and read PDF documents.


4.Text Chunking: Once the PDF is loaded, it's split into smaller sections or "chunks" using the RecursiveCharacterTextSplitter. This step breaks down the content into more manageable pieces for analysis.

5.Embedding Creation: Each of these text chunks is transformed into numerical representations or embeddings using OllamaEmbeddings. This step converts the text data into a format that can be easily processed by machine learning models.

6.Vector Database Generation: Using Chroma's 'from_documents' method, a new vector database is created. This database incorporates the embeddings generated in the previous step, along with the updated text chunks. This database serves as a repository of information that the model can search through.

7.Contextual Answer Generation: When a user asks a question, the model retrieves relevant context from the vector database. Based on both the context and the question, it generates a response using the Mistral Llama model. This ensures that the response is not only accurate but also contextually appropriate.

8.Output: Finally, the parsed output, which is the generated response, is returned to the user. This could be displayed in various ways depending on the interface you've designed for your system.
