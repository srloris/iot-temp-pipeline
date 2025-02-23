import pandas as pd
from sqlalchemy import create_engine

# Configuração do banco de dados
DB_USER = "postgres"
DB_PASSWORD = "sua_senha"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "mydb"

# Criar conexão com PostgreSQL usando SQLAlchemy
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Ler o arquivo CSV
csv_file = "C:/projects/iot-temp-pipeline/data/IOT-temp.csv"  # Ajuste o caminho conforme necessário
df = pd.read_csv(csv_file)

# Inserir dados no banco de dados
table_name = "temperature_readings"

df['noted_date'] = pd.to_datetime(df['noted_date'], format='%d-%m-%Y %H:%M')

df.to_sql(table_name, con=engine, if_exists="append", index=False)


print("Dados inseridos com sucesso!")
