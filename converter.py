import google.generativeai as genai
import fitz  # PyMuPDF

genai.configure(api_key= "AIzaSyCsiRFp8iZoRw7_21smG3MKqd34sasSSos")

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def pdf_to_md(pdf_path):
    content = extract_text_from_pdf(pdf_path)

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        f"Convert the following text into well-formatted markdown:\n\n{content}"
    )
    
    return response.text
