# iot-temp-pipeline

Este projeto implementa um pipeline de dados para processar leituras de temperatura provenientes de dispositivos IoT, utilizando Docker para gerenciar um contêiner PostgreSQL, Python para o processamento dos dados e Streamlit para a criação de um dashboard interativo.

## Visão Geral

O objetivo deste projeto é:
- Ler e processar dados de temperatura provenientes de dispositivos IoT (arquivo CSV).
- Inserir os dados processados em uma instância do PostgreSQL rodando em um contêiner Docker.
- Criar views SQL para facilitar a análise dos dados.
- Desenvolver um dashboard interativo com Streamlit e Plotly para visualização dos dados, tais como:
  - Média de temperatura por dispositivo.
  - Contagem de leituras por hora.
  - Temperaturas máximas e mínimas por dia.

## Estrutura do Projeto

```
iot-temp-pipeline/
├── data/
│   └── IOT-temp.csv     # Dataset com leituras de temperatura (download do Kaggle)
├── pipeline.py                      # Script para leitura do CSV e inserção dos dados no PostgreSQL
├── dashboard.py                     # Script do dashboard em Streamlit para visualização dos dados
├── README.md                        # Documentação do projeto (este arquivo)
```

## Tecnologias Utilizadas

- **Docker:** Para a criação e gerenciamento do contêiner PostgreSQL.
- **PostgreSQL:** Banco de dados relacional para armazenamento dos dados.
- **Python:** Linguagem de programação utilizada para o processamento dos dados.
- **Pandas:** Biblioteca para manipulação e análise de dados.
- **SQLAlchemy:** Biblioteca para conexão e manipulação do banco de dados.
- **Streamlit:** Framework para construção do dashboard interativo.
- **Plotly:** Biblioteca para criação de gráficos interativos.

## Pré-requisitos

- Python 3.8 ou superior
- Docker instalado ([Docker Desktop](https://www.docker.com/get-started))
- VS Code (ou editor de sua preferência)

## Configuração e Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/srloris/iot-temp-pipeline.git
cd iot-temp-pipeline
```

### 2. Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

### 3. Instalar as Dependências Python

```bash
pip install pandas psycopg2-binary sqlalchemy streamlit plotly
```

### 4. Configurar o Contêiner PostgreSQL com Docker

Execute o seguinte comando para iniciar o contêiner PostgreSQL:

```bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres
```

> **Nota:** Substitua `sua_senha` pela senha desejada.

## Executando o Projeto

### 1. Crie o bando de dados e tabela
Conecte-se ao PostgreSQL (via psql, pgAdmin ou outro cliente SQL) e execute os comandos para criar as views. Por exemplo:

```sql
CREATE DATABASE mydb;
```

```sql
CREATE TABLE temperature_readings (
    id VARCHAR(255) PRIMARY KEY,
    room_id VARCHAR(255),
    noted_date TIMESTAMP,
    temp INTEGER,
    out_in VARCHAR(10)
);
```

### 2. Carregar os Dados no Banco de Dados

- Ler o arquivo CSV com as leituras de temperatura.
- Conectar ao PostgreSQL usando SQLAlchemy.
- Inserir os dados na tabela `temperature_readings`.

Execute o script:

```bash
python pipeline.py
```

### 3. Criar as Views SQL

Conecte-se ao PostgreSQL (via psql, pgAdmin ou outro cliente SQL) e execute os comandos para criar as views. Por exemplo:

```sql
CREATE VIEW avg_temperature_per_room AS
SELECT room_id, AVG(temp) AS avg_temp
FROM temperature_readings
GROUP BY room_id;
```

```sql
CREATE VIEW temp_out_of_range AS
SELECT room_id, noted_date, temp
FROM temperature_readings
WHERE temp < 20 OR temp > 30;
```

```sql
CREATE VIEW temp_last_month AS
SELECT room_id, noted_date, temp
FROM temperature_readings
WHERE noted_date >= CURRENT_DATE - INTERVAL '1 month';
```

Crie outras views conforme os requisitos do projeto, como contagem de leituras por hora e temperaturas máximas/mínimas por dia.

### 4. Executar o Dashboard com Streamlit

No arquivo `dashboard.py`, configure o dashboard para:
- Conectar ao banco de dados.
- Carregar os dados das views SQL.
- Gerar gráficos interativos com Plotly.

Exemplo simplificado:

Para iniciar o dashboard, execute:

```bash
streamlit run dashboard.py
```

## Licença

MIT Licence

## Agradecimentos

Este projeto foi desenvolvido como parte do curso de Arquiteturas Disruptivas, explorando conceitos de IoT, Big Data e Inteligência Artificial.
