import streamlit as st
from PIL import Image
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

st.set_page_config(
    page_title="Home",
    page_icon="🐆",
    layout='wide'
)

# Função para carregar o código do chatbot
def load_chatbot_code():
    with open("Pag2_SideBar_Chatbot.py", "r") as file:
        return file.read()

# Função para carregar o código do chat com DataFrames
def load_chat_with_df_code():
    with open("pag4_LangChainChatPandas.py", "r") as file:
        return file.read()

# Função para carregar o código do chat com PDFs
def load_chat_with_pdf_code():
    with open("Pag3_openAIchatPDFv2CGPT_main_.py", "r") as file:
        return file.read()

# Função para carregar o código do chat com busca
def load_chat_with_search_code():
    with open("pag5_Chat_with_search.py", "r") as file:
        return file.read()

st.sidebar.markdown("# Faz Tudo app")
st.sidebar.markdown("## Aqui você explorará o poder da OpenAI")
st.sidebar.markdown("""---""")

# image_path = '/home/ricardo/repos/Pergunta_de_negocio_FTC/'
image = Image.open('cheetah_data_science.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('### Powered by Cheetah Data Science')

st.write("# App faz tudo com OpenAI, só alguns centavinhos de dólar por interação!")

# Opções para exibir os códigos
code_options = {
    "Chatbot": load_chatbot_code,
    "Chat com DataFrames": load_chat_with_df_code,
    "Chat com PDFs": load_chat_with_pdf_code,
    "Chat com Busca": load_chat_with_search_code
}

selected_code = st.selectbox("Escolha o código para exibir:", list(code_options.keys()))

st.code(code_options[selected_code](), language="python")
