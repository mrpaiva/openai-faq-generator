from pdf_processor import process_pdfs
from faq_generator import generate_faq, generate_output_structure
from utils import save_output_to_markdown
from langchain_community.document_loaders import PyPDFLoader
import os

def main():
    # Diretório de entrada e saída
    source_directory = "data/source"
    output_directory = "data/corpus"
    
    # Certifique-se de que o diretório de saída exista
    os.makedirs(output_directory, exist_ok=True)

    # Processar os PDFs e gerar o retriever
    retriever = process_pdfs(source_directory)

    # Ler os documentos e gerar as FAQs
    for pdf_file in os.listdir(source_directory):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(source_directory, pdf_file)
            print(f"Processando: {pdf_path}")
            
            # Carregar e dividir o PDF em textos
            with open(pdf_path, "rb") as file:
                pdf_reader = PyPDFLoader(pdf_path)
                documents = pdf_reader.load_and_split()
                doc_text = "\n".join([doc.page_content for doc in documents])

            # Gerar FAQs
            faqs = generate_faq(retriever, doc_text)
            
            # Gerar a estrutura de saída
            output_content = generate_output_structure(faqs)
            
            # Construir o caminho de saída corretamente
            output_filename = f"{os.path.splitext(pdf_file)[0]}_faq.md"
            
            # Salvar em Markdown
            save_output_to_markdown(output_content, output_filename, output_directory)

if __name__ == "__main__":
    main()
