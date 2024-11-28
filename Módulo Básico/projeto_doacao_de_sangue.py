# Projeto Doação de Sangue
# João Pedro Alves da Silva Gomes
# CPF: 073.418.393-33
# E-mail: joao.pedro.alves.sg@gmail.com
# Turma N3 - Professora Priscylla

def tela_apresentacao_inicial():
    print("*********************************************")
    print("*          Bem-vindo ao Programa!           *")
    print("*********************************************\n")
    print("Qual a importância de doar sangue?\n")
    print("A doação de sangue é um ato altruísta que salva vidas. Cada doação pode ajudar até três pessoas em necessidade.\n")
    print("Você sabia que:\n")
    print("- A cada dois segundos, alguém precisa de uma transfusão de sangue.\n")
    print("- Doar sangue é seguro e rápido.\n")
    print("- Você pode ajudar vítimas de acidentes, pacientes cirúrgicos e pessoas com doenças crônicas.\n")
    print("Obrigado por se juntar a nós nessa causa nobre!")

def tela_posso_doar():
    print("*********************************************")
    print("*    Vamos verificar se você pode doar!     *")
    print("*********************************************\n")
    idade = int(input("Digite a sua idade: "))
    peso = int(input("Digite o seu peso: "))
    if(idade >= 16 and idade <= 69):
               if peso >= 50:
                   print("\nVocê pode doar!")
               else:
                   print("\nVocê precisa pesar pelo menos 50kg para doar, sinto muito.")
    elif idade < 16:
        print("\nMenores de idade precisam de autorização dos responsáveis para doar.")
    else:
        print("\nVocê não pode doar, sinto muito.")

def tela_lista_locais():
    print("*********************************************")
    print("*        Lista de locais de doação          *")
    print("*********************************************\n")
    print("\nEm Fortaleza:\n")
    locais = ["HEMOCE SEDE", "HEMOCE PRAÇA DAS FLORES"]
    horarios = ["7h às 17h30","7h às 12h30 "]
    for local, h in zip(locais, horarios):
        print(f'{local} - {h}')
    print("\nInterior do estado do Ceará:\n")
    locais_ce = ["HEMOCE CRATO", "HEMOCE JUAZEIRO DO NORTE", "HEMOCE IGUATU", "HEMOCE QUIXADÁ", "HEMOCE SOBRAL"] 
    horarios_ce = ["7h às 17h30", "7h às 17h", "7h às 17h", "7h às 17h", "7h às 18h"]
    for local_ce, h_ce in zip(locais_ce, horarios_ce):
        print(f'{local_ce} - {h_ce}')

def tela_dicas():
    print("*********************************************")
    print("*   Algumas dicas para você que vai doar!   *")
    print("*********************************************\n")
    dicas = ["Se hidrate!", "Se alimente bem!", "Descance bem!", "Leve documentos com foto!", "Use roupas leves!"]
    for d in dicas:
        print(d)

def sistema():             
    sair = False
    while(sair != True):
        print("\n*********************************************")
        print("*        Sistema de Doação de Sangue        *")
        print("*********************************************")
        print("Escolha uma opção:")
        print("1 - Apresentação Inicial")
        print("2 - Posso doar sangue?")
        print("3 - Dicas para Doadores")
        print("4 - Lista de locais de doação")
        print("5 - Sair")
        resposta = int(input("Digite uma opção: "))
        print("\n")
        if(resposta == 1):
            tela_apresentacao_inicial()
        elif (resposta == 2):
            tela_posso_doar()
        elif (resposta == 3):
            tela_dicas()
        elif (resposta == 4):
            tela_lista_locais()
        elif(resposta == 5):
            sair = True
        else:
            print("Erro! Tente novamente.")
    print("Doe Sangue, doe Vida! Uma campanha do Instituto Atlântico.")
        
sistema()
