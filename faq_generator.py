from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, temperature=0)

def generate_questions(doc_text, max_tokens=2000):
    question_prompt_template = """
    Baseado no seguinte texto:

    {text}

    Gere uma ou mais perguntas relevantes para o conteúdo acima.
    """
    question_prompt = PromptTemplate(input_variables=["text"], template=question_prompt_template)
    question_chain = LLMChain(llm=llm, prompt=question_prompt)

    blocks = divide_text(doc_text, max_tokens)
    questions = []
    for block in blocks:
        questions.extend(question_chain.run({"text": block}).split("\n"))

    return questions

def generate_answer(question, retriever, max_tokens=2000):
    qa_template = """
    Baseado no seguinte documento, responda à seguinte pergunta:

    Pergunta: {question}

    Resposta:
    """
    answer_prompt = PromptTemplate(input_variables=["question"], template=qa_template)

    qa_chain = LLMChain(llm=llm, prompt=answer_prompt)

    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs])

    context_blocks = divide_text(context, max_tokens)
    answers = []
    for block in context_blocks:
        answers.append(qa_chain.run({"question": question, "context": block}).strip())

    return " ".join(answers)

def generate_faq(retriever, doc_text, max_tokens=2000):
    questions = generate_questions(doc_text, max_tokens)
    faqs = []
    for question in questions:
        answer = generate_answer(question, retriever, max_tokens)
        faqs.append((question, answer))
    return faqs

def divide_text(text, max_tokens):
    words = text.split()
    blocks = []
    current_block = []

    for word in words:
        current_block.append(word)
        if len(current_block) >= max_tokens:
            blocks.append(' '.join(current_block))
            current_block = []

    if current_block:
        blocks.append(' '.join(current_block))

    return blocks

def generate_output_structure(faqs):
    output = "#Perguntas Frequentes\n"
    for question, answer in faqs:
        output += f"### {question}\n{answer}\n"
    return output
