"""
Curso: DesenvSistemas59
Disciplina: Técnicas de Programação I
Professora: Andréia
Aluno: Gustavo Inacio de Oliveira Cruz
RA: 23521
Lista: 3a-lista
Data: 27/03/2023
"""

from helper_functions_23521 import inverte_texto, remove_espaco_branco

def get_paridade(comprimento_texto):
    """
    Identifica a paridade do comprimento de um texto.
    Um texto com comprimento ímpar terá um caractere na sua metade
    que não afetará o palíndromo e poderá ser descartado no slicing
    do texto.

    Funciona apenas para textos contendo caracteres alfanuméricos.
    
    Retorna:
        Os retornos 1 e 0, por serem truthy e falsy values, respectivamente,
        podem ser testados em um "if else" para decidir como dividir a string
        de texto em duas partes.
    """

    if (comprimento_texto % 2 == 0):
        return 0
    else:
        return 1

def is_palindromo(texto):
    """
    Identifica se um texto é palíndromo.

    Retorna:
        True: texto é palíndromo.
        False: texto não é palíndromo.
    """
    texto = remove_espaco_branco(texto).lower()

    # Divide o texto em duas partes
    if get_paridade(len(texto)):
        esquerda = texto[0:len(texto) // 2]
        direita = texto[len(texto) // 2 + 1:] # A soma com + 1 assegura que o caractere do meio do texto seja desconsiderado
    else:
        esquerda = texto[0:len(texto) // 2]
        direita = texto[len(texto) // 2:]

    if (esquerda == inverte_texto(direita)):
        return True 
    else:
        return False
