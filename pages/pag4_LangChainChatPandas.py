# Importando as bibliotecas necessárias
from langchain.agents import initialize_agent, AgentType
from langchain.agents import create_pandas_dataframe_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
import streamlit as st
import pandas as pd
import os

# Dicionário contendo formatos de arquivo e suas funções de leitura correspondentes
file_formats = {
    "csv": pd.read_csv,
    "xls": pd.read_excel,
    "xlsx": pd.read_excel,
    "xlsm": pd.read_excel,
    "xlsb": pd.read_excel,
    "json": pd.read_json,
    "html": pd.read_html,
    "sql": pd.read_sql,
    "feather": pd.read_feather,
    "parquet": pd.read_parquet,
    "dta": pd.read_stata,
    "sas7bdat": pd.read_sas,
    "h5": pd.read_hdf,
    "hdf5": pd.read_hdf,
    "pkl": pd.read_pickle,
    "pickle": pd.read_pickle,
    "gbq": pd.read_gbq,
    "orc": pd.read_orc,
    "xpt": pd.read_sas,
    "sav": pd.read_spss,
    "gz": pd.read_csv,
    "zip": pd.read_csv,
    "bz2": pd.read_csv,
    "xz": pd.read_csv,
    "txt": pd.read_csv,
    "xml": pd.read_xml,
}

# Função para limpar o estado do botão de envio
def clear_submit():
    st.session_state["submit"] = False

# Função decorada com @st.cache_data, que armazena em cache os dados carregados por 2 horas
@st.cache_data(ttl="2h")
def load_data(uploaded_file):
    try:
        ext = os.path.splitext(uploaded_file.name)[1][1:].lower()
    except:
        ext = uploaded_file.split(".")[-1]
    if ext in file_formats:
        return file_formats[ext](uploaded_file)
    else:
        st.error(f"Formato de arquivo não suportado: {ext}")
        return None

# Configuração da página Streamlit
st.set_page_config(page_title="LangChain: Chat com Pandas DataFrame", page_icon="🦜")
st.title("🦜 LangChain: Chat com Pandas DataFrame")

# Interface para o usuário fazer o upload de um arquivo de dados
uploaded_file = st.file_uploader(
    "Carregar arquivo de dados",
    type=list(file_formats.keys()),
    help="Diversos formatos de arquivo são suportados",
    on_change=clear_submit,
)

# Se um arquivo foi carregado, carrega os dados para um DataFrame pandas
if uploaded_file:
    df = load_data(uploaded_file)

# Caixa de texto para inserir a chave de API do OpenAI na barra lateral
openai_api_key = st.sidebar.text_input("Chave de API do OpenAI", type="password")

# Verifica se a lista de mensagens está no estado da sessão, caso não esteja, inicia com uma mensagem do assistente
if "messages" not in st.session_state or st.sidebar.button("Limpar histórico da conversa"):
    st.session_state["messages"] = [{"role": "assistente", "content": "Como posso ajudar?"}]

# Exibe as mensagens da conversa na interface do Streamlit
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Se houver uma mensagem digitada pelo usuário
if prompt := st.chat_input(placeholder="Sobre o que é esses dados?"):
    st.session_state.messages.append({"role": "usuário", "content": prompt})
    st.chat_message("usuário").write(prompt)

    # Verifica se a chave de API do OpenAI foi fornecida
    if not openai_api_key:
        st.info("Por favor, adicione sua chave de API do OpenAI para continuar.")
        st.stop()

    # Inicializa o modelo de chat com o OpenAI
    llm = ChatOpenAI(
        temperature=0, model="gpt-3.5-turbo-0613", openai_api_key=openai_api_key, streaming=True
    )

    # Cria um agente que entende comandos específicos relacionados a DataFrames pandas
    pandas_df_agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
    )

    # Resposta do assistente gerada pelo agente com base na mensagem do usuário
    with st.chat_message("assistente"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = pandas_df_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistente", "content": response})
        st.write(response)
