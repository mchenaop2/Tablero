import streamlit as st

from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title='Tablero', layout='wide')
st.title('Reconocimiento de Dígitos escritos a mano')


# Add canvas component
# Specify canvas parameters in application
drawing_mode = "freedraw"

bg_color = '#000000'
with st.sidebar:
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    stroke_color = st.color_picker("Pick A Color", "#00f900")
    

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=200,
    key="canvas",
)
