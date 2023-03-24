def trocaLetra(texto, letra, letra_sub):
    texto_sub = str()
    for char in texto:
        if char == letra:
            texto_sub += letra_sub
        else:
            texto_sub += char
    return texto_sub

print(trocaLetra('Diogo', 'o', 'v'))