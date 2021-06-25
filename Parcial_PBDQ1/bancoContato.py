import sqlite3 #importanto a biblioteca do banco de dados SQLite

def connect(): 
    return sqlite3.connect("minha_agenda.db")

#criando a coxenao com a tabela "minha_agenda.db"
CREATE_TABLE = "create table minha_agenda(id integer primary key, nome text, telefone text, cidade text)"
def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

#inserindo dados na "minha_agenda.db"
INSERT_DADOS = "insert into minha_agenda (nome, telefone, cidade) values (?, ?, ?);"
def insert(conexao, nome, telefone, cidade):
    with conexao:
        conexao.execute(INSERT_DADOS,( nome, telefone, cidade))

#busca todos os contatos ja adicionados
CONTATO_DADOS = "select * from minha_agenda;"
def busca_all(conexao):
    with conexao:
        return conexao.execute(CONTATO_DADOS).fetchall()

#busca contato atraves do nome
CONTATO_NOME = "select * from minha_agenda where nome = ?;"
def busca_nome(conexao, nome):
    with conexao:
        return conexao.execute(CONTATO_NOME, (nome,)).fetchall()

#mostra o primeiro contato adicionado atraves do comando abaixo
CTT_ANT = "select * from minha_agenda order by id asc limit 1;" 
def ctt_antigo(conexao):
    with conexao:
        return conexao.execute(CTT_ANT).fetchone()

#mostra contato mais recente adicionado atraves do comando abaixo
CTT_RCT = "select * from minha_agenda order by id desc limit 1;"
def ctt_recente(conexao):
    with conexao:
        return conexao.execute(CTT_RCT).fetchone()