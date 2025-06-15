import os
import inquirer

def get_pdf_choices():
    pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]

    if not pdf_files:
        print("⚠️  No PDF files found in this folder.")
        return []

    questions = [
        inquirer.Checkbox(
            "selected_pdfs",
            message="Pick the PDF files to convert",
            choices=pdf_files
        )
    ]

    answers = inquirer.prompt(questions)
    return answers.get("selected_pdfs", []) if answers else []
