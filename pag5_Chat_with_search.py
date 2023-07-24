import streamlit as st

# Importando módulos e classes necessárias
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun

# Barra lateral do Streamlit
with st.sidebar:
    # Caixa de texto para inserir a chave de API do OpenAI
    openai_api_key = st.text_input("Chave de API do OpenAI", key="langchain_search_api_key_openai", type="password")

    # Links para obter a chave de API do OpenAI e visualizar o código-fonte no GitHub
    "[Obter uma chave de API do OpenAI](https://platform.openai.com/account/api-keys)"
    "[Visualizar o código-fonte](https://github.com/streamlit/llm-examples/blob/main/pages/2_Chat_with_search.py)"
    "[![Abrir no GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

# Título do aplicativo Streamlit
st.title("🔎 LangChain - Chat com busca")

# Introdução do aplicativo
"""
Neste exemplo, estamos usando o `StreamlitCallbackHandler` para exibir os pensamentos e ações de um agente em um aplicativo interativo do Streamlit.
Experimente mais exemplos de Agentes LangChain 🤝 Streamlit em [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

# Verifica se a lista de mensagens está no estado da sessão, caso não esteja, inicia com uma mensagem do assistente
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistente", "content": "Olá, sou um chatbot que pode fazer buscas na web. Como posso ajudar?"}
    ]

# Exibe as mensagens da conversa na interface do Streamlit
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Caixa de texto para que o usuário digite uma pergunta ou consulta
if prompt := st.chat_input(placeholder="Quem venceu o U.S. Open feminino em 2018?"):
    st.session_state.messages.append({"role": "usuário", "content": prompt})
    st.chat_message("usuário").write(prompt)

    # Verifica se a chave de API do OpenAI foi fornecida
    if not openai_api_key:
        st.info("Por favor, adicione sua chave de API do OpenAI para continuar.")
        st.stop()

    # Inicializa o modelo de chat do OpenAI e a tarefa de busca no DuckDuckGo
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
    search = DuckDuckGoSearchRun(name="Pesquisa")
    search_agent = initialize_agent([search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)

    # Resposta do assistente com base na consulta do usuário
    with st.chat_message("assistente"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistente", "content": response})
        st.write(response)
