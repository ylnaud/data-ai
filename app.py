# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar la página principal
st.title("Aplicación de Visualización de Datos")
st.write("Sube un archivo CSV para generar gráficos interactivos.")

# Cargar el archivo CSV
uploaded_file = st.file_uploader("Elige un archivo CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Datos del CSV:")
    st.write(data.head())
    
    # Gráfico de la distribución del costo del pedido
    st.write("Distribución del costo del pedido")
    fig, ax = plt.subplots()
    sns.histplot(data=data, x='cost_of_the_order', kde=True, ax=ax)
    ax.set_title('Distribución del costo del pedido')
    ax.set_xlabel('Costo del pedido')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

    # Gráfico de la distribución del tiempo de preparación de la comida
    st.write("Distribución del tiempo de preparación de la comida")
    fig, ax = plt.subplots()
    sns.histplot(data=data, x='food_preparation_time', kde=True, ax=ax)
    ax.set_title('Distribución del tiempo de preparación de la comida')
    ax.set_xlabel('Tiempo de preparación')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

    # Gráfico de la distribución del tiempo de entrega
    st.write("Distribución del tiempo de entrega")
    fig, ax = plt.subplots()
    sns.histplot(data=data, x='delivery_time', kde=True, ax=ax)
    ax.set_title('Distribución del tiempo de entrega')
    ax.set_xlabel('Tiempo de entrega')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

    # Frecuencia de cada restaurante
    st.write("Frecuencia de cada restaurante")
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.countplot(y=data['restaurant_name'], order=data['restaurant_name'].value_counts().index, ax=ax)
    ax.set_title('Frecuencia de cada restaurante')
    ax.set_xlabel('Cuenta')
    ax.set_ylabel('Nombre del Restaurante')
    st.pyplot(fig)

    # Proporción de tipos de cocina
    st.write("Proporción de tipos de cocina")
    fig, ax = plt.subplots(figsize=(10, 10))
    data['cuisine_type'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_title('Proporción de tipos de cocina')
    ax.set_ylabel('')
    st.pyplot(fig)

    # Frecuencia de pedidos por día de la semana
    st.write("Frecuencia de pedidos por día de la semana")
    fig, ax = plt.subplots()
    data['day_of_the_week'].value_counts().plot.bar(ax=ax)
    ax.set_title('Frecuencia de pedidos por día de la semana')
    ax.set_xlabel('Día de la semana')
    ax.set_ylabel('Cuenta')
    st.pyplot(fig)
