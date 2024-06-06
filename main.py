def verificaNaLista(opcao, lista):
    for i in lista:
        if i == opcao:
            return True
    return False
   
def forcaOpcao(msg, lista):
    msgErro = 'Digite uma opcao valida!'
    opcao = input(msg)
    while not verificaNaLista(opcao, lista):
        print(msgErro)
        opcao = input(msg)
    return opcao
 
def meuIndice(opcao, lista):
    for i in range(len(lista)):
        if lista[i] == opcao:
            return i
    return False

def obter_dados_praia(): 
    print(f"Lista de prais disponivies: ")
    for i in range(len(praias)):
        print(f"{i + 1}. {praias[i]}")
    
    praiaEscolha = forcaOpcao("Digite o nome da praia: ", praias)
    praiaIndice = meuIndice(praiaEscolha, praias) 
    
    return  (f"Qualidade da agua: {qualidadeAgua[praiaIndice]}\n"
             f"Condicao da Praia: {condicoesPraia[praiaIndice]}\n"
             f"Nivel de Poluicao: {nivelPoluicao[praiaIndice]}\n")

def enviar_feedback(praia, indice):
    condicao = forcaOpcao("Digite o condicao da praia: Digite - (Boa/Normal/Ruim) \n", ["Boa","Normal","Ruim"])
    poluicao = forcaOpcao("Digite o nível de presença de lixo: Digite - (Alta/Baixa) \n", ["Alta","Baixa"])
    qualidade = forcaOpcao("Digite o qualidade da agua: Digite - (Boa/Ruim) \n", ["Boa","Ruim"])

    # Atualizar dados existentes
    if verificaNaLista(praia, praias):
        condicoesPraia[indice] = condicao
        nivelPoluicao[indice] = poluicao
        qualidadeAgua[indice] = qualidade
    # Criar novos dados nao existentes
    else:
        praias.append(praia)
        
        condicoesPraia.append(condicao)
        nivelPoluicao.append(poluicao)
        qualidadeAgua.append(qualidade)
    
    return 'Feedback recebido com sucesso'

praias = ['Praia das asturias']
condicoesPraia = ['Boa']
nivelPoluicao = ['Alta']
qualidadeAgua = ['Boa']
            
nome = input("Digite seu nome: ")

while True:
    print(f"Olá {nome}, Seja bem-vindo à Ocean Rescue!\n"
        "1. Consultar dados da praia\n"
        "2. Enviar feedback sobre presença de lixo\n"
        "3. Sair")
    
    escolha = forcaOpcao("Escolha uma opção: ", ["1","2","3"])

    if escolha == '1':
        dados = obter_dados_praia()
        print(dados)

    elif escolha == '2':
        praiaEscolha = input("Digite o nome da praia: ")
        praiaIndice = meuIndice(praiaEscolha, praias) 
        resultado = enviar_feedback(praiaEscolha, praiaIndice)
        print(resultado)

    else:
        print("Muito obrigado por utilizar a Ocean Rescue!")
        break
    
    #Continuacao
    continua = forcaOpcao("Voce desejar continuar? Digite - Sim ou Não: ", ["Sim", "Nao"])
    
    if continua == 'Nao':
        print("Muito obrigado por utilizar a Ocean Rescue!")
        break    
            

