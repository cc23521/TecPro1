def inverteTexto(texto):
    comprimento_texto = len(texto)
    texto_invertido = str()
    for c in range(comprimento_texto - 1, -1, -1):
        texto_invertido += texto[c]
    return texto_invertido

def removeEspacoBranco(texto):
    texto_sem_espaco = str()
    for char in texto:
        if char != ' ':
            texto_sem_espaco += char
    return texto_sem_espaco

def paridade(numero):
    if (numero % 2 == 0):
        return 0
    else:
        return 1

def identificaPalindromo(texto):
    texto = removeEspacoBranco(texto)
    if paridade(len(texto)):
        esquerda = texto[0:len(texto) // 2]
        direita = texto[len(texto) // 2 + 1:]
    else:
        esquerda = texto[0:len(texto) // 2]
        direita = texto[len(texto) // 2:]
    if (esquerda == inverteTexto(direita)):
        print(f"{texto} é palíndromo.")
    else:
        print(f"{texto} não é palíndromo.")

texto = input()

identificaPalindromo(texto)