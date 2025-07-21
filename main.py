import pdf_selector
import filesystem_update 
import converter
 
def start_conversion():
    print("Welcome! Starting the PDF to Markdown converter...\n")

    chose_pdfs = pdf_selector.get_pdf_choices()

    if len(chose_pdfs) == 0:
        print("No PDFs selected.")
        return

    new_folder = filesystem_update.output_folder()

    for each_file in chose_pdfs:
        print(f"Converting file: {each_file}")
        md_result = converter.pdf_to_md(each_file)
        filesystem_update.store_markdown(md_result, each_file, new_folder)

    print("\nDone! All selected files have been converted.")

if __name__ == "__main__":
    start_conversion()
