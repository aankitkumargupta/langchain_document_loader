from langchain_community.document_loaders import CSVLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables from a .env file (e.g., for Hugging Face API keys)
load_dotenv()

# Define the Hugging Face model to be used for text generation
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

# Wrap the model in a chat-compatible interface
model = ChatHuggingFace(llm=llm)

# Create a prompt template with a placeholder for the research paper content
prompt = PromptTemplate(
    input_variables=["ResearchPaper"],
    template="Summarise the following {ResearchPaper}",
)

loader = CSVLoader(file_path="CSV_file.csv")
docs = loader.load()
print(len(docs))

print(docs[0])
