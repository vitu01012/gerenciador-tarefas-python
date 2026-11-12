# Projeto: Gerenciador de Tarefas

# Pode adicionar tarefas na lista, remover tarefas, marcar tarefas como concluidas, listar as tarefas ou encerrar o programa

# Falta adicionar desmarcar tarefa que já tá marcada como concluida, adicionar para mostrar a porcentagem das tarefas concluidas em relação ao total, e talvez adicionar dicionário para não precisar ter duas listas



# Listas

tarefas = []
status = []

# Funções do programa (Cálculos)

def separador(caractere="-", tamanho=50):
    print(caractere * tamanho)

def titulo(texto):
    separador()
    print(texto)
    separador()

def impressaoLista(status, tarefa):
    print("A lista de tarefas atualmente está assim:")
    print()
    for i in range(len(tarefa)):
        if status[i]:
            simbolo = "X"
        else:
            simbolo = " "
        print(f"{i+1} - {tarefa[i]} - [{simbolo}]")

def pedirInteiro(pergunta):
    while (True):
        try:
            numeroInt = int(input(pergunta))
            return numeroInt
        except ValueError:
            print('Erro, digite um número válido.')

def pedirIndice(pergunta, tamanho):
    while True:
        posicao = pedirInteiro(pergunta)
        posicao = posicao - 1
        if posicao < 0 or posicao >= tamanho:
            print("Erro, tente novamente.")
        else:
            return posicao

def listaVazia(lista):
    return len(lista) == 0

def avisoListaVazia():
    print("A lista de tarefas está vazia por enquanto.")


# MENU (Selecionar a opção desejada)

titulo("GERENCIADOR DE TAREFAS")

print("Testando Git")

while (True):
    separador()
    print()
    print("1 - Adicionar uma tarefa")
    print("2 - Listar as tarefas")
    print("3 - Marcar uma tarefa como concluída")
    print("4 - Remover uma tarefa")
    print("5 - Sair")
    print()
    separador()
    print()
    respOpcaoMenu = pedirInteiro("Digite o número correspondente a opção desejada: ")
    print()
    
    if respOpcaoMenu > 5 or respOpcaoMenu < 1:
        print()
        print("Erro, digite o número correspondente a opção desejada. ")
        continue

# OPÇÃO 1 (Adicionar uma tarefa digitada pelo usuário na lista)

    elif respOpcaoMenu == 1:
        print("Você selecionou a opção 1.")
        while (True):
            print()
            respAddTarefa = input("Digite a tarefa para ser adicionada (Ou 0 para voltar ao menu): ")
            if respAddTarefa == "" or respAddTarefa == " ":
                print()
                print("Erro, por favor, digite novamente")
                continue
            elif respAddTarefa in tarefas:
                print()
                print("Essa tarefa já está na lista.")
                continue
            elif respAddTarefa == "0":
                print()
                print("Retornando ao menu...")
                break
            else:
                tarefas.append(respAddTarefa)
                status.append(False)
                print()
                print("Tarefa adicionada com sucesso!")
                break

# OPÇÃO 2 (Mostrar como está a lista de tarefas)

    elif respOpcaoMenu == 2:
        print("Você selecionou a opção 2.")
        if listaVazia(tarefas):
            avisoListaVazia()
        else:
            impressaoLista(status, tarefas)

# OPÇÃO 3 (Marcar uma tarefa selecionada como conclúida)

    elif respOpcaoMenu == 3:
        print("Você selecionou a opção 3.")
        if listaVazia(tarefas):
            avisoListaVazia()
        else:
            impressaoLista(status, tarefas)
            print()
            respConcluirTarefa = pedirIndice("Qual tarefa você gostaria de marcar como concluída? ", len(tarefas))
            status[respConcluirTarefa] = True
            print()
            print(f"A tarefa '{tarefas[respConcluirTarefa]}' foi concluída com sucesso!")

# OPÇÃO 4 (Excluir uma tarefa)

    elif respOpcaoMenu == 4:
        print("Você selecionou a opção 4.")
        if listaVazia(tarefas):
            avisoListaVazia()
        else:
            impressaoLista(status, tarefas)
            print()
            respRemoverTarefa = pedirIndice("Qual tarefa você gostaria de remover? ", len(tarefas))
            nomeTarefa = tarefas[respRemoverTarefa]
            del tarefas[respRemoverTarefa]
            del status[respRemoverTarefa]
            print()
            print(f"A tarefa '{nomeTarefa}' foi removida com sucesso!")

# OPÇÃO 5 (Encerrar o programa)

    else:
        print()
        print("Você selecionou a opção 5.")
        print("Saindo do programa...")
        print()
        exit()