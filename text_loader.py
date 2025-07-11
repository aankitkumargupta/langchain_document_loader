from langchain_community.document_loaders import TextLoader
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
    input_variables=["story"], template="Summarise the following {story}"
)


parser = StrOutputParser()

loader = TextLoader("story.txt", encoding="utf-8")

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"story": docs[0].page_content}))
