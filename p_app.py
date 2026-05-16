from flask import (
    Flask,
    jsonify,
    request,
    send_from_directory
)

from flask_cors import CORS

import sqlite3
import os


# =========================================
# CONFIGURAÇÃO DA APLICAÇÃO
# =========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

FRONTEND_DIR = os.path.join(
    BASE_DIR,
    "../frontend"
)

app = Flask(__name__)

# permitir acesso da API pelo frontend
CORS(app)


# =========================================
# BANCO DE DADOS
# =========================================

DB_NAME = "smartcity.db"


def get_connection():

    connection = sqlite3.connect(DB_NAME)

    connection.row_factory = sqlite3.Row

    return connection


# =========================================
# FRONTEND
# =========================================

@app.route("/")
def home():

    return send_from_directory(
        FRONTEND_DIR,
        "index.html"
    )


@app.route("/<path:filename>")
def static_files(filename):

    return send_from_directory(
        FRONTEND_DIR,
        filename
    )


# =========================================
# API - LISTAR PROBLEMAS
# =========================================

@app.route(
    "/api/problemas",
    methods=["GET"]
)

def listar_problemas():

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            SELECT
                id,
                tipo,
                descricao,
                latitude,
                longitude

            FROM problemas

            ORDER BY id DESC

        """)

        dados = cursor.fetchall()

        connection.close()

        resultado = [

            {
                "id": item["id"],
                "tipo": item["tipo"],
                "descricao": item["descricao"],
                "lat": item["latitude"],
                "lng": item["longitude"]
            }

            for item in dados

        ]

        return jsonify(resultado)

    except Exception as error:

        return jsonify({
            "status": "erro",
            "mensagem": str(error)
        }), 500


# =========================================
# API - ADICIONAR PROBLEMA
# =========================================

@app.route(
    "/api/adicionar",
    methods=["POST"]
)

def adicionar_problema():

    try:

        dados = request.json

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            INSERT INTO problemas (
                tipo,
                descricao,
                latitude,
                longitude
            )

            VALUES (?, ?, ?, ?)

        """, (

            dados["tipo"],
            dados["descricao"],
            dados["lat"],
            dados["lng"]

        ))

        connection.commit()

        connection.close()

        return jsonify({
            "status": "sucesso",
            "mensagem": "Problema registrado"
        })

    except Exception as error:

        return jsonify({
            "status": "erro",
            "mensagem": str(error)
        }), 500


# =========================================
# INICIAR SERVIDOR
# =========================================

