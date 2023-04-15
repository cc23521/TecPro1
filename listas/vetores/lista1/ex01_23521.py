def preenche_vetor():
    """
    Preenche um vetor de 50 posições com valores aleatórios
    entre 0 e 20.
    """
    from random import randint

    vetor = [0] * 50
    for i in enumerate(vetor):
        vetor[i[0]] = randint(0, 20)
    return vetor

def soma(vetor):
    """
    Resolve item 1a.

    Soma valores armazenados em <vetor>.
    """
    soma = 0
    for i in vetor:
        soma += i
    return soma

def procura_numero_nove(vetor):
    """
    Resolve item 1b.

    Conta ocorrências do número 9 em <vetor>.
    """
    ocorrencias = 0
    for i in vetor:
        if i == 9:
            ocorrencias += 1
    return ocorrencias

def get_maior_valor(vetor):
    """
    Resolve item 1c.

    Determina o maior valor de <vetor>.
    """
    maior = vetor[0]
    for i in vetor:
        if i > maior:
            maior = i
    return maior

def posicoes_maior_valor(vetor):
    """
    Resolve item 1d.

    Retorna uma lista com as posições de ocorrência
    do maior valor de <vetor>.
    """
    maior_valor = get_maior_valor(vetor)
    pos = []
    for i, valor in enumerate(vetor):
        if valor == maior_valor:
            pos.append(i) 
    return pos

def solucao():
    """
    Integra as soluções dos itens da primeira questão da lista.
    """
    vetor = preenche_vetor()
    print("Vetor:", vetor)
    print("Soma:", soma(vetor)) 
    print("# Aparições número 9:", procura_numero_nove(vetor))
    print("Maior valor:", get_maior_valor(vetor))
    print("Posições do maior valor:", posicoes_maior_valor(vetor))

