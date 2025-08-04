from flask import * 
from flask_login import *

import sqlite3


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
    def get(cls, user_id: str) -> "User | None": # Retorna o User com base no user_id (email)
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
    
    def add(self, username: str) -> None:
        connection = get_connection()
        sql = "INSERT INTO tb_usuario (usu_username, usu_email, usu_password_hash) VALUES (?, ?, ?)"
        connection.execute(sql, (username, self.email, self.password_hash))
        connection.commit() # Para salvar a alteração no banco
        connection.close()
    

def addDiary(user: "User", title: str = "Novo Diário", content: str = "", share: bool = False) -> int: # Gera um novo diário e retorna o id
    connection = get_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO tb_diarios (dia_usu_id, dia_title, dia_content, dia_share) VALUES (?, ?, ?, ?)"

    cursor.execute(sql, (user.id, title, content, share))
    connection.commit()

    diary_id = cursor.lastrowid

    connection.close()
    
    return diary_id

    
def getDiary(id: int) -> tuple | None: # Retorna as infos do diario com base no id (id)
    connection = get_connection()
    sql = "SELECT * FROM tb_diarios WHERE dia_id = ?"
    diary = connection.execute(sql, (id,)).fetchone()
    connection.close()

    return diary


def updateDiary(id: int, title: str = "Novo Diário", content: str = "", share: bool = False) -> None: # Muda um diário
    connection = get_connection()
    sql = """
            UPDATE tb_diarios 
            SET dia_title = ?, dia_content = ?, dia_share = ?, dia_date = DATETIME('now', 'localtime')
            WHERE dia_id = ?
        """
        
    connection.execute(sql, (title, content, share, id))
    connection.commit()
    connection.close()


def deleteDiary(id: int) -> None: # Deleta um diário
    connection = get_connection()
    sql = "DELETE FROM tb_diarios WHERE dia_id = ?"

    connection.execute(sql, (id,))
    connection.commit()
    connection.close()
