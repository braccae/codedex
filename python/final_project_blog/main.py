from google import genai
import dotenv
from google.genai import types

dotenv.load_dotenv()

client = genai.Client()


def generate_blog(topic):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Write a paragraph about {topic}",
        config=types.GenerateContentConfig(
            maxOutputTokens=1000,
            temperature=0.3, #api docs reccomend keeping the default at 1.0; yolo
            system_instruction="You are a professional writer specializing in blog posts."
        )
    )
    return response.text

keep_writing = True

while keep_writing:
    answer = input("Write a paragraph? Y for yes, anything else for no.")
    if answer.lower() == "y":
        topic = input("Enter a topic for the blog post: ")
        print(generate_blog(topic))
    else:
        keep_writing = False



