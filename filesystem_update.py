import os

def output_folder():
    current_dir = os.getcwd()
    folder_name = os.path.basename(current_dir) + "_converted-md"
    path_to_new = os.path.join(current_dir, folder_name)

    if not os.path.exists(path_to_new):
        os.makedirs(path_to_new)
        print(f"Created new folder: {folder_name}")
    else:
        print(f"Folder already exists: {folder_name}")

    return path_to_new

def store_markdown(markdown_text, original_pdf_name, folder_path):
    md_filename = os.path.splitext(original_pdf_name)[0] + ".md"
    md_path = os.path.join(folder_path, md_filename)

    try:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)
        print(f"✅ Saved: {md_filename}")
    except Exception as e:
        print(f"❌ Couldn't save {md_filename}: {str(e)}")
