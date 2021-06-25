import bancoContato

MENU = """
MENU PARA CADASTRO DE CONTATOS
1) ADICIONAR CONTATO         
2) VISUALIZAR CONTATOS        
3) PESQUISAR CONTATO POR NOME         
4) MOSTRAR CONTATO MAIS ANTIGO    
5) MOSTRAR CONTATO MAIS RECENTE   
6) SAIR                  
"""
def menu():
    conexao = bancoContato.connect()
    #bancoContato.create(conexao)

    while(contato := input(MENU)) != "6":
        if contato == "1":
            nome = input("Nome:")
            telefone = input("Número:")
            cidade = input("Cidade:")
            bancoContato.insert(conexao, nome, telefone, cidade)
           
        elif contato == "2":
            dado =  bancoContato.busca_all(conexao)
            for minha_agenda in dado:
                print(f'Nome: {minha_agenda[1]}\nTelefone: {minha_agenda[2]}\nCidade: {minha_agenda[3]}\n')
        
        elif contato == "3":
            nome = input("Procure pelo nome do contato: ")
            dado = bancoContato.busca_nome(conexao, nome)
            for minha_agenda in dado:
                print(f'Nome: {minha_agenda[1]}\nTelefone: {minha_agenda[2]}\nCidade: {minha_agenda[3]}\n')

        elif contato == "4":
            antiga = bancoContato.ctt_antigo(conexao)
            print(f'- Contato mais antigo -\n{antiga[1]}\n{antiga[2]}\n{antiga[3]} ')

        elif contato == "5":
            recente = bancoContato.ctt_recente(conexao)
            print(f'- Contato recente -\n{recente[1]}\n{recente[2]}\n{recente[3]}')

        elif contato == "6":
            exit()
        else:
            print("OPS - ERROR 404")
menu()