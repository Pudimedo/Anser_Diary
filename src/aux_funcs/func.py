from flask import * 
from flask_login import *

import sqlite3
# Créditos desse código a Lívia Lopes


def get_connection() -> sqlite3.Connection:
    # Função par fazer a conexão com o banco de dados
    conection = sqlite3.connect('database/banco.db')
    conection.row_factory = sqlite3.Row
    return conection

class User(UserMixin):
    def __init__(self, email: str, password_hash: str) -> None:
        self.email = email
        self.password_hash = password_hash
        
    @classmethod
    def get(cls, user_id: str) -> "User | None":
        # user_id: email do usuário como chave única
        connection = get_connection()
        sql = "SELECT * FROM tb_usuario WHERE usu_email = ?"
        resultado = connection.execute(sql, (user_id,)).fetchone() # Execta o código sql na connection e retorna em forma de tupla(ou None) com o fetchone
        if resultado:
            user = User(email=resultado['usu_email'], password_hash=resultado['usu_password_hash'])
            user.id = resultado['usu_email']
            connection.close()
            return user
        
        connection.close()
    
    def set(self, username: str) -> None:
        connection = get_connection()
        sql = "INSERT INTO tb_usuario (usu_username, usu_email, usu_password_hash) VALUES (?, ?, ?)"
        connection.execute(sql, (username, self.email, self.password_hash))
        connection.commit() # Para salvar a alteração no banco
        connection.close()
