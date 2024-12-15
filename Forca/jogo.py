import random

# Carrega as palavras do arquivo
with open(r"C:\\Python\\Forca\\palavras.txt", "r", encoding="utf-8") as f:
    palavras = f.read().splitlines()

# Função para iniciar o jogo
def iniciar_jogo():
    palavra = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra]
    tentativas = 8 
    return palavra, letras_descobertas, tentativas

# Função para jogar uma tentativa
def jogar(palavra, letras_descobertas, tentativa, letra):
    if tentativa in palavra:
        for i, letra in enumerate(palavra):
            if letra == tentativa:
                letras_descobertas[i] = tentativa
        return True, letras_descobertas  # Retorna True se acertou
    else:
        return False, letras_descobertas  # Retorna False se errou