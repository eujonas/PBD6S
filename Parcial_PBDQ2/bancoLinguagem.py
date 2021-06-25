import sqlite3

def connect():
    return sqlite3.connect("linguagens.db")

CREATE_TABLE = "create table linguagens(id integer primary key, nome text, criador text, ano integer)"
def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

INSERT_LINGUAGENS = "insert into linguagens (nome, criador, ano) values (?, ?, ?);"
def insert(conexao, nome, criador, ano):
    with conexao:
        conexao.execute(INSERT_LINGUAGENS,( nome, criador, ano))
    
BUSCA_LINGUAGENS = "select * from linguagens;"
def busca(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGENS).fetchall()

BUSCA_LINGUAGENS_POR_NOME = "select * from linguagens where nome = ?;"
def busca_nome(conexao, nome):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGENS_POR_NOME, (nome,)).fetchall()

BUSCA_LINGUAGEM_MAIS_ANTIGA = "select * from linguagens order by ano asc limit 1;" 
def busca_antiga(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGEM_MAIS_ANTIGA).fetchone() 
        
BUSCA_LINGUAGEM_MAIS_RECENTE = "select * from linguagens order by ano desc limit 2;"
def busca_recente(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGEM_MAIS_RECENTE).fetchall()