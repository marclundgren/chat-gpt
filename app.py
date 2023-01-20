import openai
import sys

# join the list of strings into a single string
cli_prompt = " ".join(sys.argv[1:])

# Read the API key from a file and store the key
key_file = open("key.txt", "r")
key = key_file.read()
key_file.close()

# Set the API key
openai.api_key = key

# Use the ChatGPT model to generate text
model_engine = "text-davinci-002"

fallback_prompt = """
take this text and generate a markdown table:

Model	Technical Name	Description
Ada
text-ada-001	Ada is the fastest model. It performs well at tasks where creativity is more important than precision. It is suitable for applications such as chatbots, parsing text, simple classification, keywords, and address correction. Ada has the lowest costs.
Babbage
text-babbage-001	Babbage excels at identifying salient patterns in text and utilizing them as a reference to generate new text. Additionally, it can effectively perform general classification tasks, such as categorizing industries, genres, and media content.
However, Babbage is not as adept at creative tasks as other models. It can understand sufficient structure to generate simple plots and titles, but it may not be the best choice for more complex creative applications.
Curie
text-curie-001	Curie is capable of many nuanced tasks like sentiment classification and summarization. It reaches almost the level of Davinci but has lower costs. It is also good at answering questions, performing Q&A, and as a general service chatbot.
Davinci
text-davinci-003	Davinci, in its current version 003, corresponds to ChatGPT (GPT3.5). It is a versatile model that can perform a wide range of tasks, often with fewer specific instructions. It excels in tasks that require a deep understanding of content, such as summary generation and creative writing. However, it requires more computational resources and may not be as fast or cost-effective as other models.
"""

prompt = cli_prompt or fallback_prompt

completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.7)
message = completion.choices[0].text
print(message)