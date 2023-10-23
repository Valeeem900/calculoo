import streamlit as st
from PIL import Image

def Inicio():
     st.markdown(
        """
        ##Bienvenidos a la calculadora web##. Con esta app se busca principalmente facilitar el calculo de operaciones matemáticas de una manera rápida y eficiente, con resultados correctos al instante
          """ )
     image = Image.open('calculadora.png')
     st.image(image, caption='calculadora')


     image = Image.open('math.png')
     st.image(image, caption='math')

     image = Image.open('signos.png')
     st.image(image, caption='signos')

# Página 2: Calculadora de Suma
def suma():
    st.header("Calculadora de Suma")
    num1 = st.number_input("Ingrese el primer número")
    num2 = st.number_input("Ingrese el segundo número")
    resultado = num1 + num2
    st.write(f"Resultado: {resultado}")

# Página 3: Calculadora de Resta
def resta():
    st.header("Calculadora de Resta")
    num1 = st.number_input("Ingrese el primer número")
    num2 = st.number_input("Ingrese el segundo número")
    resultado = num1 - num2
    st.write(f"Resultado: {resultado}")

# Página 4: Calculadora de Multiplicación
def multiplicacion():
    st.header("Calculadora de Multiplicación")
    num1 = st.number_input("Ingrese el primer número")
    num2 = st.number_input("Ingrese el segundo número")
    resultado = num1 * num2
    st.write(f"Resultado: {resultado}")

def contacto():
# Usando st.write()
  st.write("¡Contactos!")
  mensaje = "Contactos:hugo Arias: CEO , Camila Arias: programadora, valentina jerez: diseñadora "
  st.text(mensaje)

# Barra de navegación para cambiar entre páginas
page = st.sidebar.selectbox( "Seleccione una calculadora:", ("Inicio","Suma", "Resta", "Multiplicación", "contacto"))

if page == "Suma":
     suma()
elif page == "Resta":
     resta()
elif page == "Multiplicación":
     multiplicacion()
elif page == "Inicio": 
    Inicio()
elif page == "contacto":
     contacto() 