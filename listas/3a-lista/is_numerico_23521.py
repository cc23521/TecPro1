"""
Curso: DesenvSistemas59
Disciplina: Técnicas de Programação I
Professora: Andréia
Aluno: Gustavo Inacio de Oliveira Cruz
RA: 23521
Lista: 3a-lista
Data: 27/03/2023
"""

def is_numeric(texto):
    """
    Identifica se um texto contém apenas caracteres numéricos.

    Retorna:
        True: texto numérico.
        False: texto contém ao menos um caractere numérico.
    """

    for char in texto:
        if not char.isdigit():
            return False
    return True

