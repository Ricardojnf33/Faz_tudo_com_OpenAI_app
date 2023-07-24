import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🎲",
    layout='wide'
)

st.sidebar.markdown( '# Faz Tudo app' )
st.sidebar.markdown( '## Aqui voce explorará o poder da OpenAI' )
st.sidebar.markdown( """---""" )

#image_path = '/home/ricardo/repos/Pergunta_de_negocio_FTC/' 
image = Image.open( 'cheetah_data_science.png' )
st.sidebar.image( image, width=120 )

st.sidebar.markdown( '### Powered by Cheetah Data Science' )

st.write( "# App faz tudo com OpenAI, só alguns centavinhos de dólar por interação!" )
