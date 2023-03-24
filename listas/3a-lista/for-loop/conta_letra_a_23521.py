"""
Curso: DesenvSistemas59
Disciplina: Técnicas de Programação I
Professora: Andréia
Aluno: Gustavo Inacio de Oliveira Cruz
RA: 23521
Lista: 3a-lista
Data: 27/03/2023
"""

def conta_letra_a(texto):
    """
    Retorne ocorrências da letra 'a' ou 'A' em um texto.
    """

    ocorrencias = 0
    for char in texto:
        if char in ('A', 'a'):
            ocorrencias += 1 
    return ocorrencias

