import sqlite3

def get_db_connection():
    conn = sqlite3.connect('jogo.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    conn = sqlite3.connect('jogo.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            usuario TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Banco criado com sucesso!")

if __name__ == '__main__':
    create_db()
