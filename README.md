# README - Trocando uma Ideia com Meu PDF V1

Troque uma ideia com seu PDF

Bem-vindo(a) ao aplicativo "Trocando uma Ideia com Meu PDF"! Este é um aplicativo desenvolvido com o intuito de permitir que você interaja e faça perguntas sobre o conteúdo de um arquivo PDF. De forma descontraída e inovadora, você poderá extrair informações relevantes do seu PDF e ter uma experiência única de aprendizado e descoberta.

# Instalação

Para utilizar o aplicativo, é necessário ter o Python instalado em seu computador. Além disso, certifique-se de ter instalado os pacotes necessários para a execução do código. Você pode instalar todas as dependências utilizando o pip. Execute o seguinte comando em seu terminal:

`pip install -r requirements.txt`

# Como Funciona

O aplicativo é construído utilizando a biblioteca Streamlit, que possibilita a criação de interfaces de usuário amigáveis em Python. Ele utiliza algumas bibliotecas para realizar o processamento do PDF, a divisão do texto em pedaços, a criação de embeddings (representações numéricas das palavras) e a busca por similaridade das perguntas feitas pelo usuário.

Aqui está uma breve explicação sobre as principais bibliotecas utilizadas no código:

# Dotenv

O pacote `dotenv` é utilizado para carregar variáveis de ambiente a partir de um arquivo `.env`. Isso permite que informações sensíveis, como chaves de API, sejam mantidas em segurança e não sejam expostas no código.

# Streamlit

A biblioteca `streamlit` é a base do nosso aplicativo. Ela é responsável por criar a interface gráfica amigável e interativa que você verá ao executar o código. Utilizamos também a função `st.set_page_config()` para configurar o título da página.

# PyPDF2

O `PyPDF2` é uma biblioteca para lidar com arquivos PDF. Neste aplicativo, utilizamos o `PdfReader` para ler o arquivo PDF carregado pelo usuário e extrair o texto contido nele.

# Langchain

Aqui é onde a mágica acontece! A biblioteca `langchain` é utilizada para processar o texto extraído do PDF e criar representações numéricas (embeddings) para as palavras presentes no texto.

# OpenAI

Dentro do pacote `langchain`, utilizamos o módulo `OpenAI` para carregar um modelo de linguagem treinado pela OpenAI. Esse modelo é utilizado para responder perguntas baseadas nos textos do PDF.

# FAISS

O módulo `vectorstores` contém a classe `FAISS`, que é responsável por criar um banco de conhecimento com os embeddings das palavras. Isso possibilita uma busca eficiente por similaridade entre as perguntas do usuário e o conteúdo do PDF.

#Como Usar

Certifique-se de que todas as dependências estão instaladas corretamente, conforme explicado na seção de instalação.

Execute o código do aplicativo usando o seguinte comando:

`streamlit run openAIchatPDFv1_main_.py`

O aplicativo será aberto em seu navegador padrão.

Clique no botão "Carregue aqui seu PDF" e selecione o arquivo PDF que você deseja explorar.

Após o carregamento do PDF, o texto será extraído automaticamente e dividido em pedaços.

Digite uma pergunta relacionada ao conteúdo do PDF no campo "Pergunte ao seu PDF".

Clique no botão "Perguntar" para obter a resposta com base no texto do PDF.

Divirta-se trocando ideias com o seu PDF!

# Considerações Finais

Espero que você tenha uma experiência agradável e proveitosa utilizando o aplicativo "Trocando uma Ideia com Meu PDF". Sinta-se à vontade para explorar diferentes PDFs e fazer várias perguntas interessantes.

Este aplicativo foi desenvolvido com muito carinho e dedicação por mim para tentar melhorar um pouco a sua produtividade com I.A. de ponta, mas claro, pagando uns centavinhos de dólar para cada pergunta respondida pela OpenAI, não se esqueça de alterar o arquivo `.env` com sua Chave_API da OpenAI. Caso encontre algum problema, tenha alguma sugestão de melhoria ou queira contribuir com o projeto, sinta-se à vontade para abrir uma "issue" ou enviar um "pull request" no repositório do GitHub.

Divulgue este projeto para seus amigos, colegas e redes sociais para que mais pessoas possam ter acesso a essa ferramenta divertida e informativa.

Agradecemos por usar o "Trocando uma Ideia com Meu PDF". Divirta-se e boas descobertas!

<img src="cheetah_data_science.png" alt="Logo do Aplicativo" width="200">

Powered by Cheetah Data Science
