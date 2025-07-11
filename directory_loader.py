from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the Hugging Face model
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

# Create the chat model
model = ChatHuggingFace(llm=llm)


parser = StrOutputParser()

loader = DirectoryLoader(path="pdf_folder", glob="*.pdf", loader_cls=PyPDFLoader)

docs = loader.load()  # loads all documents at once.

# docs = loader.lazy_load()

for document in docs:
    print(document.metadata)


# print(type(docs))
# print(len(docs))  # one page as one doc
# print(docs[4].page_content)
# print(docs[4].metadata)
