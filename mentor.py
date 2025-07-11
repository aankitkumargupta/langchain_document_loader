from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", task="text-generation"
)

# Prompt template for generating content based on the topic
prompt = PromptTemplate(
    input_variables=["topic"],
    template="""<|system|>
You are an assistant designed to help mentors prepare for their classes.
Based on the topic provided, you will generate structured content for the mentor.

The topic of the class is: {topic}

</s>
<|user|>
Generate the following content for the mentor:

1. **Class Overview**: Provide a brief overview of the topic and key takeaways the mentor should focus on.
2. **Key Concepts to Explain**: List the key concepts the mentor should explain to the students. Include any terms, methods, or techniques the mentor needs to explain.
3. **Code Implementation Details**: Provide a breakdown of any code implementations the mentor should explain. Explain each code block and its purpose. (if applicable)
4. **Content for PPT**: Provide text content for Powerpoint presentation (5 Slides).
</s>
""",
)

# Allow mentor to input the class topic
topic = input("Please enter the class topic: ")

# Set up the chain (Prompt → Model → Output Parser)
chain = prompt | model

# Generate the mentor's content
result = chain.invoke({"topic": topic})

# Output the generated content
print("\nGenerated Mentor Content:")
print(result)
