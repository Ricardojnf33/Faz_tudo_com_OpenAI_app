# Faz Tudo com OpenAI

Este é um aplicativo Streamlit que demonstra o poder da API da OpenAI por meio de 4 ferramentas interessantes:

## Chatbot com GPT-3.5 Turbo

A primeira ferramenta é um chatbot simples construído com a API ChatCompletion do GPT-3.5 Turbo. O usuário pode inserir uma chave de API válida na barra lateral e então conversar com o chatbot na caixa de entrada de mensagens.

O aplicativo mantém o histórico da conversa no estado da sessão do Streamlit. A cada nova mensagem do usuário, o histórico é enviado para a API ChatCompletion, que retorna uma resposta.

O código deste chatbot está em `2_Chatbot.py`.

## Perguntas e Respostas com PDF

A segunda ferramenta permite que o usuário faça upload de um PDF e então faça perguntas sobre o conteúdo do PDF.

Primeiro, o texto do PDF é extraído usando a biblioteca PyPDF2. Em seguida, o texto é dividido em pequenos trechos usando a classe CharacterTextSplitter do LangChain.

Os trechos de texto são inseridos em um vectorstore FAISS usando embeddings do OpenAI.

Quando o usuário faz uma pergunta, os trechos mais relevantes são recuperados do vectorstore usando a busca por similaridade.

Finalmente, a cadeia de perguntas e respostas do LangChain é executada com esses trechos e a pergunta do usuário para gerar uma resposta.

O código deste recurso está em `3_Chat_PDF.py`.

## Chat com Pandas DataFrames

A terceira ferramenta permite que o usuário faça upload de um arquivo CSV ou Excel e converse sobre os dados em um DataFrame Pandas resultante.

O LangChain é usado para criar um agente com compreensão de comandos relacionados a Pandas e DataFrames.

O agente pode responder a perguntas sobre os dados, plotar gráficos, calcular estatísticas e mais. O StreamlitCallbackHandler exibe os pensamentos e ações do agente.

O código está em `4_LangChain_ChatPandas.py`.

## Chat com Busca

A quarta ferramenta é um chatbot com capacidade de busca. Internamente, ele usa a tarefa DuckDuckGoSearchRun do LangChain para realizar consultas no DuckDuckGo e retornar os resultados.

O usuário pode fazer perguntas naturais como "Quem foi o campeão da Copa do Mundo de 2010?" e o chatbot irá procurar a resposta na web.

O código está em `5_Chat_with_search.py`.

# Considerações Finais

Este aplicativo demonstra o poder da API da OpenAI e bibliotecas como o LangChain para a construção de agentes de conversação avançados e ferramentas de NLP.

Com apenas algumas linhas de código Python e uma chave de API, é possível criar experiências incríveis como chatbots, QA de documentos, compreensão de dados e muito mais.

O aplicativo completo está hospedado em https://faztudocom-openai-app.streamlit.app/ para teste ao vivo. O código-fonte está disponível no GitHub para referência e customização.

Agradecemos por usar o "Trocando uma Ideia com Meu PDF". Divirta-se e boas descobertas!

<img src="cheetah_data_science.png" alt="Logo do Aplicativo" width="200">

Powered by Cheetah Data Science
