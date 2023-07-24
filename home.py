import streamlit as st
from PIL import Image
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

st.set_page_config(
    page_title="Faz tudo com OpenAI app",
    page_icon="🐆",
    layout='wide'
)

# Função para carregar o código do chatbot
def load_chatbot_code():
    with open("2_Chatbot.py", "r") as file:
        return file.read()

# Função para carregar o código do chat com DataFrames
def load_chat_with_df_code():
    with open("4_LangChain_ChatPandas.py", "r") as file:
        return file.read()

# Função para carregar o código do chat com PDFs
def load_chat_with_pdf_code():
    with open("3_Chat_PDF.py", "r") as file:
        return file.read()

# Função para carregar o código do chat com busca
def load_chat_with_search_code():
    with open("5_Chat_with_search.py", "r") as file:
        return file.read()

st.sidebar.markdown("# Faz Tudo app")
st.sidebar.markdown("## Aqui você explorará o poder da OpenAI")
st.sidebar.markdown("""---""")

# image_path = '/home/ricardo/repos/Pergunta_de_negocio_FTC/'
image = Image.open('cheetah_data_science.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('### Powered by Cheetah Data Science')

st.write("# App faz tudo com OpenAI, só alguns centavinhos de dólar por interação!")

st.write("## Escolha entre as ferramentas a sua esquerda!")
