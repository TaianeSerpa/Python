import tkinter as tk
from tkinter import messagebox
import interface

def iniciar_jogo_handler():
    janela.destroy() #Fechar a janela inicial 
    interface.iniciar_interface_jogo()# Abre a interface do jogo

def mostra_instrucaoes():
    instrucoes =  """
    BEM VINDOS AO JOGO DA FORCA
    - O objetivo do jogo é adivinhar a palavra secreta.
    - Você pode tentar uma letra por vez.
    - A cada erro , perde uma tentativa.
    - o jogo termenina se descobrir a palavra ou acabar as tentativas.
    BOM JOGO
    """
    messagebox.showinfo("Instruçoes", instrucoes)

def sair_jogo():
    janela.quit() #sair do jogo

# janela inicial
janela = tk.Tk()
janela.title("Jogo da Forca")
janela.geometry("400x300")
janela.configure(bg="#f4f4f4")

titulo = tk.Label(janela, text="Jogo da Forca",font=("Helvetica", 24,"bold "),bg ="#f4f4f4",fg ="black", padx=10 ,pady=5)
titulo.pack(pady=20)

botao_iniciar = tk.Button(janela, text="Iniciar Jogo", command= iniciar_jogo_handler, font=("Helvetica",14), bg="#2196F3",fg="white", padx=10, pady=5)
botao_iniciar.pack(pady=10)

botao_instrucoes = tk.Button(janela, text="Instruções", command=mostra_instrucaoes, font=("Helvetica",14), bg="#2196F3",fg="white",padx=10,pady=5)
botao_instrucoes.pack(pady=10) 

botao_sair = tk.Button(janela, text="Sair", command=sair_jogo, font=("Helvetica",14), bg="#f44336", fg="white",padx=10,pady=5)
botao_sair.pack(pady=10)

janela.mainloop()
