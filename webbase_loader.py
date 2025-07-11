from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# Define the Hugging Face model
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

# Create the chat model
model = ChatHuggingFace(llm=llm)

# Create a prompt Template
prompt = PromptTemplate(
    input_variables=["question", "text"],
    template="Answer the following question \n {question} from the following text - \n {text}",
)
parser = StrOutputParser()

url = "https://blog.google/intl/en-in/company-news/outreach-initiatives/google-for-india-2024-bringing-ai-to-every-indian-across-our-products/"

# Multiple URL can be passed too.

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser
print(
    chain.invoke(
        {"question": "What is the summary of this blog", "text": docs[0].page_content}
    )
)
