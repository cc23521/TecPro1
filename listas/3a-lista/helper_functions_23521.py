"""
Curso: DesenvSistemas59
Disciplina: Técnicas de Programação I
Professora: Andréia
Aluno: Gustavo Inacio de Oliveira Cruz
RA: 23521
Lista: 3a-lista
Data: 27/03/2023

Este arquivo contém as soluções para os problemas de for loop na ordem em
que estão na lista, na forma de funções. Decidi colocá-las em um mesmo
arquivo pois o problema do palindromo utiliza duas delas e, com isso, 
posso fazer o import das funções ao invés refazer o mesmo código.
"""

def conta_letra_a(texto):
    """
    Retorna ocorrências da letra 'a' ou 'A' em um texto.
    """

    ocorrencias = 0
    for char in texto:
        if char in ('A', 'a'):
            ocorrencias += 1 
    return ocorrencias

def conta_caractere(texto, char):
    """
    Retorna o número de vezes que um caractere aparece em um texto.
    """

    ocorrencias = 0
    for c in texto:
        if c == char:
            ocorrencias += 1
    return ocorrencias


def inverte_texto(texto)
    """
    Retorna um texto invertido.
    """

    comprimento_texto = len(texto)
    texto_invertido = str()
    # Itera sobre o texto a partir do último caractere
    for char in range(comprimento_texto - 1, -1, -1):
        texto_invertido += texto[char]
    return texto_invertido

def remove_espaco_branco(texto)
    """
    Retorna um texto sem espaços em branco.
    """

    texto_sem_espaco = str()
    for char in texto:
        if char != ' ':
            texto_sem_espaco += char
    return texto_sem_espaco

