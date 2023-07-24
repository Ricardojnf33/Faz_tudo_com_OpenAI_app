# README - Trocando uma Ideia com Meu PDF V2

Este é um aplicativo desenvolvido com o framework Streamlit que permite ao usuário fazer perguntas a respeito de um arquivo PDF carregado. O aplicativo utiliza o modelo de perguntas e respostas da OpenAI para encontrar respostas relevantes no texto do PDF. Abaixo estão os passos detalhados para executar o aplicativo em sua própria máquina:

# Pré-requisitos:

Python 3.x instalado na máquina.
Uma API key válida da OpenAI para acessar o modelo de perguntas e respostas.

# Passo 1 - Instalar as bibliotecas necessárias:

Certifique-se de ter instalado todas as bibliotecas necessárias para executar o aplicativo. As principais bibliotecas utilizadas são: Streamlit, PyPDF2, dotenv, langchain, e FAISS. Você pode instalá-las usando o gerenciador de pacotes pip. Abra o terminal (ou prompt de comando) e execute o seguinte comando:

# Passo 2 - Obter uma API key da OpenAI:

Você precisará de uma API key válida da OpenAI para usar o modelo de perguntas e respostas. Caso ainda não tenha uma, siga as instruções da OpenAI para obter a sua chave de API.

# Passo 3 - Crie um arquivo .env:

`OPENAI_API_KEY=SUA_API_KEY_AQUI`

# Passo 4 - Execute o aplicativo:

Após instalar as bibliotecas e criar o arquivo .env, você está pronto para executar o aplicativo. Abra o terminal (ou prompt de comando), navegue até o diretório onde o código do aplicativo está localizado e execute o seguinte comando:

`streamlit run FlaubertchatPDFv4BGPT_main_.py`

# Passo 5 - Interagindo com o aplicativo:

Após executar o comando, o aplicativo estará disponível em seu navegador web padrão. Você verá o título "Troque uma ideia com seu PDF, faça uma pergunta a respeito dele." e uma área para inserir a API key da OpenAI na barra lateral.

Insira sua API key da OpenAI na barra lateral e clique em "Enter".
Carregue o arquivo PDF que deseja utilizar clicando no botão "Carregue aqui seu PDF".
O texto do PDF será extraído automaticamente e dividido em pedaços (chunks) para processamento.
Digite a pergunta que deseja fazer ao PDF na caixa de texto "Pergunte ao seu PDF".
O aplicativo enviará sua pergunta para o modelo de perguntas e respostas da OpenAI e retornará a resposta relevante encontrada.

## Observações:


Certifique-se de que o PDF carregado contenha texto, pois o modelo de perguntas e respostas baseia-se em informações textuais.
O aplicativo utiliza a técnica de "similarity search" para encontrar as partes relevantes do texto antes de executar a pergunta. Assim, a precisão das respostas pode depender da qualidade do texto extraído do PDF e da formulação da pergunta.
Para encerrar a execução do aplicativo, pressione CTRL+C no terminal (ou prompt de comando) onde o aplicativo está sendo executado. Isso fechará o servidor local que o Streamlit iniciou.
Agora você tem uma aplicação interativa que permite fazer perguntas sobre o conteúdo de um PDF usando o poderoso modelo de perguntas e respostas da OpenAI. Divirta-se explorando e interagindo com seu PDF!

Agradecemos por usar o "Trocando uma Ideia com Meu PDF". Divirta-se e boas descobertas!

<img src="cheetah_data_science.png" alt="Logo do Aplicativo" width="200">

Powered by Cheetah Data Science
