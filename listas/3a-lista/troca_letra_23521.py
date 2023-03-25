def troca_letra(texto, letra_alvo, letra_sub):
    """
    Substitui as ocorrências de uma letra alvo de um texto por outra.

    Args:
        letra_alvo: letra a ser substituída.
        letra_sub: letra de substituição.
    """

    texto_sub = str()
    for letra in texto:
        if letra == letra_alvo:
            texto_sub += letra_sub
        else:
            texto_sub += letra
    return texto_sub

