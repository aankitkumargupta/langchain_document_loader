from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", task="text-generation"
)

# Define the prompt template with clearer instructions
prompt = PromptTemplate(
    input_variables=["classnotes"],
    template="""<|system|>
You are an assistant that summarizes classroom discussions into structured points.
The class notes you are summarizing include a mentor-student interaction, code examples, and topics covered in a Python programming lesson.

</s>
<|user|>
Summarize the following class transcript into the following sections:
1. Topic Covered: Provide the main topic discussed in the class.
2. Key Concepts Explained: List the core concepts that were explained during the class.
3. Code Examples Explained: Provide an explanation of any code examples given during the class.
4. Student Questions and Answers: Include any questions from the students and their answers by the mentor.
5. Action Items or Next Steps: List any action items or tasks that were assigned for students to follow up on.
6. Quiz Questions: Generate 5 quiz questions based on the class content. Each question should have 4 options, with one correct answer. Format as MCQs.

Transcript:
{classnotes}
</s>
""",
)


# Load the class notes from the text file
loader = TextLoader("classnotes.txt", encoding="utf-8")
docs = loader.load()
full_text = "\n".join([doc.page_content for doc in docs])

# Ensure the content loaded correctly
print("Loaded class notes:")
print(full_text[:100])  # Print the first 500 characters to verify the content

# Set up the chain (Prompt → Model → Output Parser)
parser = StrOutputParser()
chain = prompt | model | parser

# Generate and print the summary
result = chain.invoke({"classnotes": full_text})
print("Generated Summary:")
print(result)
