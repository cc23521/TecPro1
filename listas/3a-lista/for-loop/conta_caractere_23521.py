"""
Curso: DesenvSistemas59
Disciplina: Técnicas de Programação I
Professora: Andréia
Aluno: Gustavo Inacio de Oliveira Cruz
RA: 23521
Lista: 3a-lista
Data: 27/03/2023
"""

def conta_caractere(texto, char):
    """
    Retorna o número de vezes que um caractere aparece em um texto.
    """

    ocorrencias = 0
    for c in texto:
        if c == char:
            ocorrencias += 1
    return ocorrencias

