import mysql.connector
import pandas as pd
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'escola'
    )

    if conexao.is_connected():
        print('Conectado!')
        
        cursor = conexao.cursor()

        sql = 'INSERT INTO alunos (nome, cpf, data_nascimento, email, telefone, data_matricula, id_curso) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        valores = ('Joana Dark', '11122253344', '2005-04-21', 'joana@email.com', '219999977712', '2026-02/07', '1')
        
        cursor.execute(sql, valores)

        conexao.commit()

        print(f'Linha inserida. ID gerado: {cursor.lastrowid}')


except Error as e:
    print(f'Erro ao conectar ou executar: {e}')

finally:
    if 'cursor' in locals():
        try:
            cursor.close()
        except Exception:
            pass

    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('Conexão encerrada.')