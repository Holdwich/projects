
#GRUPO: Matheus Castro, Arthur Arash, Filipe e Gabriel Ribeiro

# [nome, tempo de execução, prioridade]
processos = [["X", 4, 4], ["Y", 10, 3], ["Z", 2, 1]]

def prioridadeProcessos():
    maiorPrioridade = -1
    indexMaiorPrioridade = -1
    for i in range(0, len(processos)):
        if processos[i][2] > maiorPrioridade:
            maiorPrioridade = processos[i][2]
            indexMaiorPrioridade = i
    return indexMaiorPrioridade

indexAtual = 0
indexMaiorPrioridade = prioridadeProcessos()
booleanoAdicionar = False

while len(processos) != 0:

    if booleanoAdicionar:
        processos.append(["T1", 4, 6])
        booleanoAdicionar = False

    if indexAtual == indexMaiorPrioridade:
        processos[indexAtual][1] = processos[indexAtual][1] - 1
        print(processos[indexAtual])
        if processos[indexAtual][1] == 6:
            booleanoAdicionar = True
        if processos[indexAtual][1] == 0:
            processos.pop(indexAtual)
        indexMaiorPrioridade = prioridadeProcessos()
        indexAtual = indexMaiorPrioridade

    else:
        indexMaiorPrioridade = prioridadeProcessos()
        indexAtual = indexMaiorPrioridade

