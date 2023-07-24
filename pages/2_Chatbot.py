# Este código é um aplicativo simples de chatbot usando a biblioteca Streamlit e a API GPT-3.5 Turbo da OpenAI. 
# A barra lateral permite que o usuário insira sua chave de API do OpenAI. 
# O aplicativo exibe uma conversa entre o usuário e o assistente, 
# com o usuário digitando suas mensagens na caixa de entrada e o assistente respondendo com a ajuda do modelo
# de linguagem GPT-3.5 Turbo da OpenAI. É importante notar que é necessário ter uma chave de API válida para que o chatbot funcione corretamente.

import openai
import streamlit as st

# Barra lateral para inserir a chave da API do OpenAI
with st.sidebar:
    openai_api_key = st.text_input("Chave da API OpenAI", key="chatbot_api_key", type="password")
    "[Obtenha uma chave de API OpenAI](https://platform.openai.com/account/api-keys)"

# Título do aplicativo
st.title("💬 Chatbot")

# Se não houver mensagens na sessão, inicializa com uma mensagem do assistente
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistente", "content": "Como posso ajudar você?"}]

# Exibe todas as mensagens armazenadas na sessão
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Entrada do usuário para enviar uma mensagem ao chatbot
if prompt := st.chat_input():
    # Verifica se a chave da API do OpenAI foi fornecida
    if not openai_api_key:
        st.info("Por favor, adicione sua chave da API OpenAI para continuar.")
        st.stop()

    # Configura a chave da API do OpenAI
    openai.api_key = openai_api_key

    # Adiciona a mensagem do usuário à sessão
    st.session_state.messages.append({"role": "usuário", "content": prompt})
    st.chat_message("usuário").write(prompt)

    # Envia as mensagens para a API do OpenAI para obter uma resposta do chatbot
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message

    # Adiciona a resposta do chatbot à sessão
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
