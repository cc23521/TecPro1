"""
Curso: DesenvSistemas59
Disciplina: Técnicas de Programação I
Professora: Andréia
Aluno: Gustavo Inacio de Oliveira Cruz
RA: 23521
Lista: 3a-lista
Data: 27/03/2023
"""

def removeEspacoBranco(texto)
    """
    Retorne um texto sem espaços em branco.
    """

    texto_sem_espaco = str()
    for char in texto:
        if char != ' ':
            texto_sem_espaco += char
    return texto_sem_espaco

