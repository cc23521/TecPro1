def preenche_vetor(n):
    """
    Preenche um vetor de 5 posições com números aleatórios de 0 a n.
    """
    from random import randint

    vetor = [0] * 5
    for i in enumerate(vetor):
        vetor[i[0]] = randint(0, n)
    return vetor

def inverte_vetor(vetor):
    print("Vetor original:", vetor)
    indice_esquerda = 0
    indice_direita = len(vetor) - 1
    while indice_esquerda < indice_direita:
        valor_esquerda = vetor[indice_esquerda]
        vetor[indice_esquerda] = vetor[indice_direita]
        vetor[indice_direita] = valor_esquerda
        indice_esquerda += 1
        indice_direita -= 1
    print("Vetor invertido:", vetor)

def solucao():
    """
    Resolve terceira questão da lista.
    """
    maximo = int(input("Qual o valor de n? "))
    inverte_vetor(preenche_vetor(maximo))

