import unittest
from pdf_processor import process_pdfs
from faq_generator import generate_faq, generate_output_structure
from utils import save_output_to_markdown
import os
from fpdf import FPDF
from langchain_community.document_loaders import PyPDFLoader

class TestQuestionAnswering(unittest.TestCase):
    def setUp(self):
        self.source_directory = "data/test_source/"
        os.makedirs(self.source_directory, exist_ok=True)

        # Criar um PDF válido para os testes
        test_pdf_path = os.path.join(self.source_directory, "test_document.pdf")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Este é um documento de teste. Ele contém informações sobre como cadastrar usuários.", ln=True)
        pdf.output(test_pdf_path)

        self.retriever = process_pdfs(self.source_directory)

    def tearDown(self):
        for root, dirs, files in os.walk(self.source_directory):
            for file in files:
                os.remove(os.path.join(root, file))

    def test_generate_faq(self):
        test_pdf_path = os.path.join(self.source_directory, "test_document.pdf")
        pdf_reader = PyPDFLoader(test_pdf_path)
        documents = pdf_reader.load_and_split()
        doc_text = "\n".join([doc.page_content for doc in documents])

        faqs = generate_faq(self.retriever, doc_text)
        self.assertGreater(len(faqs), 0)
        for question, answer in faqs:
            self.assertIsInstance(question, str)
            self.assertIsInstance(answer, str)

    def test_output_structure(self):
        faqs = [("Como cadastro um novo usuário?", "Para cadastrar um novo usuário, vá até o menu 'Configurações'.")]
        output = generate_output_structure(faqs)

        expected_output = (
            "#Perguntas Frequentes\n"
            "### Como cadastro um novo usuário?\n"
            "Para cadastrar um novo usuário, vá até o menu 'Configurações'.\n"
        )
        self.assertEqual(output, expected_output)

    def test_save_output(self):
        faqs = [("Como cadastro um novo usuário?", "Para cadastrar um novo usuário, vá até o menu 'Configurações'.")]
        output_directory = "data/corpus"
        output = generate_output_structure(faqs)
        save_output_to_markdown(output, "test_faq_output.md", output_directory)

        saved_path = "data/corpus/test_faq_output.md"
        self.assertTrue(os.path.exists(saved_path))
        with open(saved_path, "r", encoding="utf-8") as f:
            saved_content = f.read()
        self.assertEqual(saved_content, output)

if __name__ == "__main__":
    unittest.main()
