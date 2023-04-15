def preenche_vetor():
    """
    Preenche um vetor de 10 posicoes com numeros aleatorios
    entre 0 e 20.
    """
    from random import randint
    
    vetor = [0] * 10
    for i in enumerate(vetor):
        vetor[i[0]] = randint(0, 20)
    return vetor

def translacao(vetor):
    """
    Realiza uma operação de translação para a direita em <vetor>.
    """
    ultimo_elemento = vetor[-1]
    vetor_tmp = vetor[:-1]
    vetor_transladado = [ultimo_elemento] + vetor_tmp 
    return vetor_transladado

def solucao():
    """
    Resolve segunda questão da lista.
    """
    vetor = preenche_vetor()
    return (vetor, translacao(vetor))

