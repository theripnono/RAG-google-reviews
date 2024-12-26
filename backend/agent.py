import os
import faiss
from uuid import uuid4
import pandas as pd
from dotenv import dotenv_values
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate


class ReviewAnalysisAgent:
    def __init__(self,llm_model:str, emedding_model:str):
        """
        Initializes the ReviewAnalysis-Agent class..
        """

        apikey = self._init_api()
        self.llm = ChatOpenAI(model=llm_model , temperature=0.7, openai_api_key=apikey)
        self.embedding_model = self.select_embedding_model(emedding_model)

        
        text_content = self.csv_to_text()
        docs = self.prepare_docs(text_content)
        
        self.vectorstore = self.build_vectorstore(self.embedding_model)

        ids = [str(uuid4()) for _ in range(len(docs))]
        self.vectorstore.add_documents(docs, ids=ids)

        self.retriever = self.vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 6})

        # Set up custom RAG prompt
        self.custom_rag_prompt = PromptTemplate.from_template(
            """Eres un agente experto en analizar comentarios los
            de los usuarios para analizar y mejorar la experiencia.
            Si no sabes la respuesta, di simplemente que no tienes la información.
            No  inventes la respuesta. Si conoces la fecha, mencionala
            Utiliza frases cortas procura que la respuesta sea 
            lo más concreta posible.

            {context}
            Question: {question}
            """
        )

        # Create RAG chain
        self.rag_chain = (
            {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
            | self.custom_rag_prompt
            | self.llm
            | StrOutputParser()
        )

    def _init_api(self):
        """
        Initialize the API.
        """
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        config = dotenv_values(".ENV")
        apikey = config['OPENAI_API_KEY']
        return apikey

    def select_embedding_model(self, model_name: str) -> HuggingFaceEmbeddings:
        """Select embedding model from HuggingFace."""
        return HuggingFaceEmbeddings(model_name=model_name)

    def prepare_docs(self, text_content):
        """Prepare docs from text content.

        Args:
            text_content (str): Content of the extracted text.

        Returns:
            list[Document]: List of Document objects.
        """
        self.text_splitter = CharacterTextSplitter(
            separator="\n\n",
            chunk_size=2000,
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )
        chunks = self.text_splitter.split_text(text_content)
        return [Document(page_content=chunk) for chunk in chunks]

    def build_vectorstore(self, emedding_model:HuggingFaceEmbeddings)-> object:
        """_summary_

        Args:
            emedding_model (object): Embedding model

        Returns:
            object: _description_
        """
        # Set up Fais index. https://github.com/facebookresearch/faiss/wiki/getting-started
        # All indexes need to know when they are built which is the dimensionality of the vectors they operate on
        index = faiss.IndexFlatL2(len(emedding_model.embed_query("dimesion lenght test")))
        vector_store = FAISS(
            embedding_function=emedding_model,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )  
        
        return vector_store
    
    def csv_to_text(self) -> str:
        """
        Transforms the CSV into a plain text.

        Returns:
            str: Transformed text from the CSV file.
        """
        text = ''
        try:
            df = pd.read_csv('data.csv', sep=',')
            new_df = df[['comment', 'date']].copy()
            df_dict = new_df.to_dict(orient='records')
            for row in df_dict:
                text += row['comment'] + ' fecha del comentario ' + row['date'] + '\n\n'
            
            return text     
        except Exception as e:
            print(f'Error: {e}')


    def format_docs(self, docs):
        """
        Format the documents for output.

        Args:
            docs: Documents to format.

        Returns:
            str: Formatted documents as a string.
        """
        return "\n\n".join(doc.page_content for doc in docs)

    def get_answer(self, question: str):
        """
        Get the answer to a question using the RAG chain.

        Args:
            question (str): The question to ask.

        Returns:
            str: The answer generated by the model.
        """
        return self.rag_chain.invoke(question)


        
agent = ReviewAnalysisAgent(llm_model = "gpt-4o-mini",
                             emedding_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
response = agent.get_answer("¿Cual es la comida preferida de los usuarios?")
print(response)
