# Blocos = [[ID, Tamanho, Endereço Alocado]]
# Memoria = [[Endereço, Tamanho]]
blocos = [['1', 5, 'N/A'], ['2', 2, 'N/A'], ['3', 2, 'N/A']]
memoria = [['A', 2], ['B', 3], ['C', 10]]

def bestFit(blocos, memoria):

    for i in range(len(blocos)):
        menor = 99
        for j in range(len(memoria)):
            if memoria[j][1] >= blocos[i][1] and memoria[j][1] < menor:
                menor = memoria[j][1]
                indexMenor = j
        blocos[i][2] = memoria[indexMenor][0]
        memoria[indexMenor][1] = memoria[indexMenor][1] - blocos[i][1]

    print(f"Memoria: {memoria}, Blocos alocados: {blocos}")

def worstFit(blocos, memoria):

    for i in range(len(blocos)):
        maior = 0
        for j in range(len(memoria)):
            if memoria[j][1] >= blocos[i][1] and memoria[j][1] > maior:
                maior = memoria[j][1]
                indexMaior = j
        blocos[i][2] = memoria[indexMaior][0]
        memoria[indexMaior][1] = memoria[indexMaior][1] - blocos[i][1]

    print(f"Memoria: {memoria}, Blocos alocados: {blocos}")

def firstFit(blocos, memoria):

    for i in range(len(blocos)):
        for j in range(len(memoria)):
            if memoria[j][1] >= blocos[i][1]:
                blocos[i][2] = memoria[j][0]
                memoria[j][1] = memoria[j][1] - blocos[i][1]
                break

    print(f"Memoria: {memoria}, Blocos alocados: {blocos}")

if __name__ == "__main__":

    print('Selecione uma opção:\n 1. First-Fit\n 2. Best-Fit\n 3. Worst-Fit')
    x = int(input())

    if x == 1:
        firstFit(blocos,memoria)

    elif x == 2:
        bestFit(blocos,memoria)

    elif x == 3:
        worstFit(blocos,memoria)

