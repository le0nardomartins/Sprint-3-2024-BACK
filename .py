import sqlite3
import random
from datetime import datetime

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('banco-de-dados.db')
cursor = conn.cursor()

# Criar a tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS dados_sensores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperatura REAL,
    umidade REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Função para inserir dados na tabela com valores aleatórios
def inserir_dados_aleatorios():
    # Gerar valores aleatórios para temperatura e umidade
    temperatura = round(random.uniform(15.0, 35.0), 2)  # Intervalo de temperatura (15°C a 35°C)
    umidade = round(random.uniform(30.0, 90.0), 2)      # Intervalo de umidade (30% a 90%)

    # Inserir os dados no banco de dados
    cursor.execute('''
    INSERT INTO dados_sensores (temperatura, umidade)
    VALUES (?, ?)
    ''', (temperatura, umidade))
    conn.commit()

# Inserir um conjunto de dados aleatórios
for _ in range(30):  # Exemplo: adiciona 10 registros com valores aleatórios
    inserir_dados_aleatorios()

# Fechar a conexão com o banco de dados
conn.close()

print("Dados aleatórios inseridos com sucesso!")
