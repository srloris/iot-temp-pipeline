import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Configuração da conexão com o banco de dados
DB_USER = "postgres"
DB_PASSWORD = "sua_senha"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "mydb"  # Substitua pelo nome do seu banco de dados

# Criar a conexão com o banco de dados PostgreSQL
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

# Gráfico 1: Média de temperatura por sala
st.header('Média de Temperatura por Sala')
df_avg_temp = load_data('avg_temperature_per_room')  # View para média de temperatura por sala
fig1 = px.bar(df_avg_temp, x='room_id', y='avg_temp')
st.plotly_chart(fig1)

# Gráfico 2: Temperaturas do mês passado
st.header('Temperaturas do Mês Passado')
df_last_month = load_data('temp_last_month')  # View para temperaturas do mês passado
fig2 = px.line(df_last_month, x='noted_date', y='temp')
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas fora do intervalo
st.header('Temperaturas Fora do Intervalo')
df_out_of_range = load_data('temp_out_of_range')  # View para temperaturas fora do intervalo
fig3 = px.scatter(df_out_of_range, x='noted_date', y='temp', color='room_id')
st.plotly_chart(fig3)

