import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash-latest") 

def transform_to_markdown(text):
    prompt = f"""
Take the following PDF content and rewrite it into well-structured Markdown format.
Ensure all headings, lists, and paragraphs are preserved. Ignore empty lines or garbage data.

Content:
{text}
"""
    response = model.generate_content(prompt)
    return response.text.strip()