# Gerador de FAQs Automatizadas com Python, Langchain e OpenAI API

Este projeto visa automatizar a criação de FAQs (Perguntas Frequentes) a partir de documentos PDF utilizando Python, Langchain e a OpenAI API. A ideia é transformar documentos longos e complexos em FAQs simples e fáceis de entender, que podem ser facilmente manipuladas e publicadas em um site.

## Estrutura do Projeto

```bash
openai-faq-generator/
│
├── .env                    # Arquivo de variáveis de ambiente
├── requirements.txt        # Arquivo com as dependências do projeto
├── main.py                 # Arquivo principal que orquestra a execução do projeto
├── faq_generator.py        # Módulo responsável pela geração de FAQs
├── pdf_processor.py        # Módulo que lida com o processamento de PDFs
├── utils.py                # Funções auxiliares usadas no projeto
│
├── data/                   # Diretório para armazenar dados
│   ├── source/             # PDF de entrada para processamento
│   │   └── documento1.pdf  # Exemplo de arquivo PDF
│   └── corpus/             # Saída do processo em formato markdown
│       └── documento1_faq.md

```

## Funcionalidades

- **Processamento de PDFs:** Extração de texto dos arquivos PDF.
- **Geração de FAQs:** Criação de perguntas e respostas relevantes com base no conteúdo dos PDFs.
- **Saída em Markdown:** As FAQs geradas são salvas em arquivos markdown (.md) prontos para serem publicados em um site.

## Como Usar

1. Clone o repositório:
    
    ```bash
    git clone https://github.com/seu-usuario/openai-faq-generator.git
    cd openai-faq-generator
    ```
    
2. Instale as dependências:
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. Configure suas variáveis de ambiente no arquivo `.env`:
    
    ```makefile
    makefileCopiar código
    OPENAI_API_KEY=your_openai_api_key
    ```
    
4. Coloque os PDFs que você deseja processar na pasta `data/source`.
5. Execute o script principal:
    
    ```bash
    python main.py
    ```
    
6. As FAQs geradas serão salvas na pasta `data/corpus`.

## Saiba Mais

Para uma explicação detalhada sobre o funcionamento do projeto, confira o artigo completo no Medium:

🔗 [Como Gerar FAQs Automatizadas com Python, Langchain e a OpenAI API](https://medium.com/@mrpaiva/como-gerar-faqs-automatizados-com-python-langchain-e-a-openai-api-e26c30a921b1)

## Contribuições

Contribuições são bem-vindas! Se você tiver ideias, sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License.