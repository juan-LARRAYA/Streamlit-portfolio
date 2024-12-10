import streamlit as st

# Título y presentación personal
st.title('Juan Cruz Larraya - Ingeniero Electrónico')

# Información de contacto
st.write('Hola, soy Juan Cruz Larraya, Ingeniero Electrónico.')
st.write('Estoy interesado en proyectos de automatización y programación. Puedo ayudarte en proyectos relacionados con la electrónica y la tecnología.')

# Botón para descargar el CV
cv_file = 'Juan Cruz Larraya CV.pdf'
if st.button('Descargar CV'):
    with open(cv_file, "rb") as file:
        st.download_button(
            label="Descargar CV",
            data=file,
            file_name=cv_file,
            mime="application/pdf"
        )



