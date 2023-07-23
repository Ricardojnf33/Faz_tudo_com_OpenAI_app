# Importar as bibliotecas necessárias
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

# Função para carregar o arquivo e executar o modelo de perguntas e respostas
def main():
    # Carregar as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Configurar a página do Streamlit
    st.set_page_config(page_title="Trocando uma ideia com meu PDF")

    # Título da aplicação
    st.header("Troque uma ideia com seu PDF, faça uma pergunta a respeito dele. 💬")

    # Criar um sidebar para a entrada da API key do usuário
    st.sidebar.header("Configurações")
    api_key = st.sidebar.text_input("Insira sua API key da OpenAI", type="password")

    # Upload do arquivo PDF
    pdf = st.file_uploader("Carregue aqui seu PDF", type="pdf")

    # Extrair o texto do PDF, se um arquivo for carregado
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Dividir o texto em pedaços (chunks) para processamento
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Criar embeddings usando o modelo OpenAI
        embeddings = OpenAIEmbeddings(api_key)  # Usando a API key inserida pelo usuário
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Entrada do usuário para fazer uma pergunta ao PDF
        user_question = st.text_input("Pergunte ao seu PDF:")

        # Processar a pergunta e obter a resposta usando o modelo de perguntas e respostas da OpenAI
        if user_question:
            docs = knowledge_base.similarity_search(user_question)

            # Carregar o modelo de perguntas e respostas da OpenAI
            llm = OpenAI(api_key)  # Usando a mesma API key inserida anteriormente
            chain = load_qa_chain(llm, chain_type="stuff")

            # Executar o modelo com a pergunta do usuário e obter a resposta
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_question)

            # Exibir a resposta na interface do Streamlit
            st.write("Resposta:")
            st.write(response)

# Executar a função principal quando o script é executado diretamente
if __name__ == '__main__':
    main()
    
