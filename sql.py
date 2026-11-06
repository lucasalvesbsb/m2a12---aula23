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
        
        cursor.execute('SELECT * FROM alunos LIMIT 5')

        resultados = cursor.fetchall()
        for linha in resultados:
            print(linha)


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