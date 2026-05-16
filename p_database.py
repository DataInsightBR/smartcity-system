import sqlite3


# =========================================
# CONECTAR AO BANCO DE DADOS
# =========================================

conn = sqlite3.connect("smartcity.db")

cursor = conn.cursor()


# =========================================
# CRIAR TABELA DE PROBLEMAS
# =========================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS problemas (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    tipo TEXT NOT NULL,

    descricao TEXT,

    latitude REAL NOT NULL,

    longitude REAL NOT NULL,

    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

""")


# =========================================
# SALVAR ALTERAÇÕES
# =========================================

conn.commit()


# =========================================
# FECHAR CONEXÃO
# =========================================

conn.close()


# =========================================
# MENSAGEM FINAL
# =========================================

print("Banco de dados SmartCity inicializado com sucesso!")