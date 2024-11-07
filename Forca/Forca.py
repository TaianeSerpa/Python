import random
import tkinter

# Tente abrir o arquivo e verificar o conteúdo
with open(r"C:\\Python\\Forca\\palavras.txt", "r", encoding="utf-8") as f:
    palavras = f.read().splitlines()  # Cada linha do arquivo é uma palavra na lista

def jogar_focar():
    palavra = random.choice(palavras)
    letras_descobertas= ["_" for _ in palavra]
    tentativas = 6

    print("Bem-Vindo ao jogo da forca!")
    print("Adivinhe a palavra:" + "".join(letras_descobertas))

    while tentativas > 0:
        print("\nPalavra:"," ".join(letras_descobertas))
        print(f"Tentativas restantes:{tentativas}")

        tentativa = input("Digite uma letra:").lower()

        if len(tentativa) !=1 or not  tentativa.isalpha():
            print("Por favor, insira apenas uma letra válida.")
            continue
        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_descobertas[i] = tentativa
            print("Boa! A palavra agora está assim: "+ " ".join(letras_descobertas))
        else:
            tentativas -= 1
            print(f"A letra '{tentativa}' não está na palavra. Você tem {tentativa} tentativas restantes")

        if "_" not in letras_descobertas:
            print("\nParabéns! Você adivinhou a palavra:",palavra)
    else:
        print("\nQue pena! Suas tentativas acabaram. A palavra era:", palavra)
jogar_focar()