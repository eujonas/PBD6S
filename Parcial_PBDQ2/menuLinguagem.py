import bancoLinguagem

MENU = """
- MENU DE LINGUAGENS DE PROGRAMAÇÃO -
1) ADICIONAR LINGUAGEM         
2) VISUALIZAR LINGUAGENS        
3) PESQUISAR LINGUAGEM POR NOME         
4) LINGUAGEM MAIS ANTIGA (ANO)
5) LINGUAGENS MAIS RECENTES (ANO)   
6) SAIR   
"""
def menu():
    conexao = bancoLinguagem.connect()
    #bancoLinguagem.create(conexao)

    while(escolha := input(MENU)) != "6":
        if escolha == "1":
            nome = input("Nome da linguagem:")
            criador = input("Nome do criador:")
            ano = int(input("Ano de criação:"))
            bancoLinguagem.insert(conexao, nome, criador, ano)
           
        elif escolha == "2":
            linguagens =  bancoLinguagem.busca(conexao)
            for linguagem in linguagens:
                print(f'Nome: {linguagem[1]} Criador: {linguagem[2]} ano:{linguagem[3]}')
      
        elif escolha == "3":
            nome = input("Procure pelo nome da linguagem: ")
            linguagens = bancoLinguagem.busca_nome(conexao, nome)

            for linguagem in linguagens:
                print(f'{linguagem[1]} {linguagem[2]} {linguagem[3]}' )

        elif escolha == "4":
            antiga = bancoLinguagem.busca_antiga(conexao)
            print(f'- Linguagem mais antiga -  {antiga[1]} {antiga[2]} {antiga[3]}')

        elif escolha == "5":
            linguagens = bancoLinguagem.busca_recente(conexao)
            for linguagem in linguagens:
                print(f'- 2 Linguagens mais recentes -\nNome: {linguagem[1]} Criador: {linguagem[2]} Ano: {linguagem[3]}')

        elif escolha == "6":
            exit()

        else:
            print("ops")
menu()

