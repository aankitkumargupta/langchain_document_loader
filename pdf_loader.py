from langchain_community.document_loaders import PyPDFLoader
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

# Create a prompt Template
prompt = PromptTemplate(
    input_variables=["ResearchPaper"],
    template="Summarise the following {ResearchPaper}",
)


parser = StrOutputParser()

loader = PyPDFLoader("Pdf_paper.pdf")

docs = loader.load()

# print(type(docs))

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"ResearchPaper": docs[0].page_content}))
