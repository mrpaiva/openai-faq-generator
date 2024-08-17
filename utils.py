import os

def find_pdfs_in_directory(directory):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def save_output_to_markdown(output, filename, directory):
    os.makedirs(directory, exist_ok=True)
    markdown_filename = os.path.splitext(filename)[0] + ".md"
    file_path = os.path.join(directory, markdown_filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(output)
    print(f"Arquivo Markdown salvo em: {file_path}")
