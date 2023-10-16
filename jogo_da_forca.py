from biblioteca import *

import random
jogador = []
erro = 0
venceu = False
palavra = ["sakamoto"]
letraescolha = random.choice(palavra)
print("---Bem-vindo ao jogo da forca.---")
while True:
    escolha = input("Digite uma letra: ")
    jogador.append(escolha.lower)
    for letra in letraescolha:
        if letra.lower() in jogador:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

    if escolha.lower() not in letraescolha.lower():
        erro += 1
        print(f"Você tem {8 - erro} tentativas.")
        enforcado(erro)

    venceu = True
    for letra in letraescolha:
        if letra.lower() not in jogador:
            venceu = False

    if erro == 8 or venceu:
        break