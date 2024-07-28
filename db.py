import sqlite3

def criar_banco_dados():
    conexao = sqlite3.connect('ordens_de_servico.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ordens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            aparelho TEXT,
            problema TEXT,
            status TEXT
        )
    ''')
    conexao.commit()
    conexao.close()

def buscar_ordens(busca):
    conexao = sqlite3.connect('ordens_de_servico.db')
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM ordens WHERE cliente LIKE ? OR aparelho LIKE ? OR problema LIKE ?
    ''', (f'%{busca}%', f'%{busca}%', f'%{busca}%'))
    resultados = cursor.fetchall()
    conexao.close()
    return resultados
