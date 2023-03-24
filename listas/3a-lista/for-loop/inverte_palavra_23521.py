"""
Curso: DesenvSistemas59
Disciplina: Técnicas de Programação I
Professora: Andréia
Aluno: Gustavo Inacio de Oliveira Cruz
RA: 23521
Lista: 3a-lista
Data: 27/03/2023
"""

def inverteTexto(texto)
    """
    Retorne um texto invertido.
    """

    comprimento_texto = len(texto)
    texto_invertido = str()
    # Itera sobre o texto a partir do último caractere
    for char in range(comprimento_texto - 1, -1, -1):
        texto_invertido += texto[char]
    return texto_invertido

