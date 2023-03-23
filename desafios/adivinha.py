from random import randint
import os
from math import log
from time import sleep

def aumenta_dificuldade():
    """Atualiza variáveis para o próximo nível."""
    global limite, n_secreto, tentativas, nivel
    limite *= 2
    n_secreto = randint(0, limite)
    tentativas = round(log(limite, 2)) + 1
    nivel += 1
    limpa_tela()
    print(f"NÍVEL {nivel}\n")

def reinicia_partida():
    """Reinicializa variáveis para uma nova partida."""
    global limite, n_secreto, tentativas, nivel
    limite = 2
    n_secreto = randint(0, limite)
    tentativas = round(log(limite, 2)) + 1
    nivel = 0
    limpa_tela()
    print(f"NÍVEL {nivel}\n")

def limpa_tela():
    """Escolhe qual comando de limpar tela é utilizado baseado no SO."""
    os.system("cls") if os.name == "nt" else os.system("clear")

def main():
    """Jogo de adivinhação numérica com níveis de dificuldade crescente."""
    limpa_tela()
    global limite, n_secreto, tentativas, nivel
    limite = 2
    n_secreto = randint(0, limite)
    tentativas = round(log(limite, 2)) + 1
    nivel = 0
    print(f"NÍVEL {nivel}\n")
    while True:
        print(f"{tentativas} tentativa(s) restante(s)")
        chute = int(input(f"Tente um valor de 0 a {limite}: "))
        if (chute == n_secreto):
            aumenta_dificuldade()
        else:
            tentativas -= 1
            if (tentativas):
                if (chute < n_secreto):
                    print("Muito baixo.")
                else:
                    print("Muito alto.")
                print()
            else:
                print(
                    "Suas chances acabaram",
                    f"O número secreto é {n_secreto}",
                    sep="\n")
                sleep(2)
                reinicia_partida()

main()

