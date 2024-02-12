```python
import streamlit as st

# Diccionario de conversiones
conversiones = {
    "Temperatura": {
        "Celsius a Fahrenheit": lambda x: x * 9/5 + 32,
        "Fahrenheit a Celsius": lambda x: (x - 32) * 5/9,
        "Celsius a Kelvin": lambda x: x + 273.15,
        "Kelvin a Celsius": lambda x: x - 273.15
    },
    "Longitud": {
        "Pies a Metros": lambda x: x * 0.3048,
        "Metros a Pies": lambda x: x / 0.3048,
        "Pulgadas a Centímetros": lambda x: x * 2.54,
        "Centímetros a Pulgadas": lambda x: x / 2.54
    },
    "Peso/Masa": {
        "Libras a Kilogramos": lambda x: x * 0.453592,
        "Kilogramos a Libras": lambda x: x / 0.453592,
        "Onzas a Gramos": lambda x: x * 28.3495,
        "Gramos a Onzas": lambda x: x / 28.3495
    },
    "Volumen": {
        "Galones a Litros": lambda x: x * 3.78541,
        "Litros a Galones": lambda x: x / 3.78541,
        "Pulgadas cúbicas a Centímetros cúbicos": lambda x: x * 16.3871,
        "Centímetros cúbicos a Pulgadas cúbicas": lambda x: x / 16.3871
    },
    "Tiempo": {
        "Horas a Minutos": lambda x: x * 60,
        "Minutos a Segundos": lambda x: x * 60,
        "Días a Horas": lambda x: x * 24,
        "Semanas a Días": lambda x: x * 7
    },
    "Velocidad": {
        "Millas por hora a Kilómetros por hora": lambda x: x * 1.60934,
        "Kilómetros por hora a Metros por segundo": lambda x: x * 0.277778,
        "Nudos a Millas por hora": lambda x: x * 1.15078,
        "Metros por segundo a Pies por segundo": lambda x: x * 3.28084
    },
    "Área": {
        "Metros cuadrados a Pies cuadrados": lambda x: x * 10.7639,
        "Pies cuadrados a Metros cuadrados": lambda x: x / 10.7639,
        "Kilómetros cuadrados a Millas cuadradas": lambda x: x * 0.386102,
        "Millas cuadradas a Kilómetros cuadrados": lambda x: x / 0.386102
    },
    "Energía": {
        "Julios a Calorías": lambda x: x * 0.239006,
        "Calorías a Kilojulios": lambda x: x * 0.004184,
        "Kilovatios-hora a Megajulios": lambda x: x * 3.6,
        "Megajulios a Kilovatios-hora": lambda x: x / 3.6
    },
    "Presión": {
        "Pascales a Atmósferas": lambda x: x * 0.00000986923,
        "Atmósferas a Pascales": lambda x: x * 101325,
        "Barras a Libras por pulgada cuadrada": lambda x: x * 14.5038,
        "Libras por pulgada cuadrada a Barras": lambda x: x / 14.5038
    },
    "Tamaño de datos": {
        "Megabytes a Gigabytes": lambda x: x / 1024,
        "Gigabytes a Terabytes": lambda x: x / 1024,
        "Kilobytes a Megabytes": lambda x: x / 1024,
        "Terabytes a Petabytes": lambda x: x / 1024
    }
}

# Configuración de la aplicación
st.title("Conversor Universal")

# Selección de categoría
categoria = st.sidebar.selectbox("Selecciona una categoría", list(conversiones.keys()))

# Selección de tipo de conversión dentro de la categoría seleccionada
if categoria:
    subcategoria = st.sidebar.selectbox(f"Selecciona un tipo de conversión en {categoria}", list(conversiones[categoria].keys()))
    if subcategoria:
        valor = st.number_input(f"Ingrese el valor en {subcategoria.split(' a ')[0]}", value=0.0)
        resultado = conversiones[categoria][subcategoria](valor)
        st.write(f"El resultado de la conversión es: {resultado} {subcategoria.split(' a ')[1]}")
```
