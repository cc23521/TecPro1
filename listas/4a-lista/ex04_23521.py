def preenche_vetor():
    """
    Inputa números do usuário até que seja passado um número negativo.
    """
    vetor = []
    numero = int(input("Insira um número natural: "))
    while numero >= 0:
        vetor.append(numero)
        numero = int(input("Insira um número natural: "))
    return vetor

def maior_que_cinco(vetor):
    """
    Determina quantidade de valores maiores que cinco em <vetor>.
    """
    quantidade = 0
    for i in vetor:
        if i > 5:
            quantidade += 1
    return quantidade

def soma_paridade(vetor):
    """
    Soma números pares e ímpares de <vetor>.

    Retorna:
        soma (dicionário): soma_pares, soma_impares.
    """
    soma = {'soma_pares': 0, 'soma_impares': 0}
    for i in vetor:
        if i % 2:
            soma['soma_impares'] += i 
        else:
            soma['soma_pares'] += i
    return soma

def solucao():
    """
    Resolve quarta questão da lista.
    """
    vetor = preenche_vetor()
    print("\nVetor:", vetor)
    print("Quantidade de valores maiores do que 5:", maior_que_cinco(vetor))
    print("Soma dos números pares:", soma_paridade(vetor)['soma_pares'])
    print("Soma dos números ímpares:", soma_paridade(vetor)['soma_impares'])
    print("Quantidade total de valores armazenados:", len(vetor))

