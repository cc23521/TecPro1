"""
Curso: DesenvSistemas59
Disciplina: Técnicas de Programação I
Professora: Andréia
Aluno: Gustavo Inacio de Oliveira Cruz
RA: 23521
Lista: 3a-lista
Data: 27/03/2023
"""

def conta_palavras(texto):
    """
    Conta a quantidade de palavras em um texto.

    Considera a ocorrência de um ou mais espaços vazios como a marcação
    do fim de uma palavra e incrementa um contador ao encontrar uma palavra.

    Retorna:
        0: Texto não contém caracteres alfabéticos.
        qnt_palavras (int): quantidade de palavras.
    """

    if len(texto) >= 1:
        if not texto.isalpha: # Testa se o texto contém caracteres não alfabéticos
            return 0
        if texto.isspace(): # Testa se o texto contém apenas espaços vazios
            return 0

        qnt_palavras = 0
        in_palavra = False # Lembra se a iteração está dentro de uma palavra
        for i, char in enumerate(texto):
            if char.isspace():
                in_palavra = False
                continue
            elif char.isalpha() and in_palavra == True:
                continue
            elif char.isalpha():
                in_palavra = True
                qnt_palavras += 1
        return qnt_palavras
    else:
        return 0

