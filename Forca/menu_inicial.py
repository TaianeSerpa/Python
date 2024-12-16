import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import awesometkinter as atk
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

# Cores disposnivel para a interface
def escolher_cor_fundo(cor):
    if cor == "Branco":
        janela.configure(bg="#FFFFFF")
        titulo.configure(bg = "#FFFFFF",fg = "#000000")
        botao_iniciar.configure(bg = "#EDEDED",fg = "#000000")	
        botao_instrucoes.configure(bg = "#EDEDED",fg = "#000000")
        botao_sair.configure(bg = "#EDEDED",fg = "#000000")
        frame_botoes.configure(bg = "#FFFFFF")
    elif cor == "Preto":
        janela.configure(bg="#000000")
        titulo.configure(bg = "#000000",fg = "#FFFFFF")
        botao_iniciar.configure(bg = "#616161",fg="#FFFFFF")
        botao_instrucoes.configure(bg = "#616161", fg="#FFFFFF")
        botao_sair.configure(bg = "#616161",fg="#FFFFFF")
        frame_botoes.configure(bg = "#000000")
        


def  abrir_menu_cor():
    #nova janela para config
    janela_config = tk.Toplevel(janela)
    janela_config.title("Configuração")
    janela_config.geometry("300x200")
    janela_config.configure(bg = "#FFFFFF")

    # Rotulo para instrução
    label =  tk.Label(janela_config, text="Escolha uma cor de fundo:",font=("Helvetica" , 15), bg= "#FFFFFF")
    label.pack(padx=10, pady=10)

    cor_var = tk.StringVar(value="Preto")
    menu_cor = tk.OptionMenu(
        janela_config, 
        cor_var, 
        "Branco", 
        "Preto",
        # lambda cor: escolher_cor_fundo(cor_var.get()) # Atualiza a cor quando selecionanda 
    )
    menu_cor.config(font=("Helvetica",14),padx=10, pady=5)
    menu_cor.pack(pady = 20)

    botao_aplicar = tk.Button(
        janela_config, 
        text="Aplicar", 
        command=lambda: escolher_cor_fundo(cor_var.get()), # atualiza a cor quando selecionada
        font=("Helvetica",14),
        bg="#4CAF50",
        fg="#FFFFFF"
    )
    botao_aplicar.pack(pady = 10)

# janela inicial
janela = tk.Tk()
janela.title("Jogo da Forca")
janela.geometry("500x350") #tamnho padrão da janela
janela.maxsize(width=900, height= 550) #tamanho maximo da janela
janela.minsize(width=600, height= 300) #tamanho minimo da janela
#janela.configure(bg="#FFFFFF") # configura a cor de fundo 

#Titulo
titulo = tk.Label(janela, text="Jogo da Forca",font=("Helvetica", 30,"bold"),padx=10 ,pady=5)
titulo.pack(side="top", padx=15, pady=20)

#criar frame para botoes
frame_botoes = tk.Frame(janela)
frame_botoes.pack(expand=True,pady=30)
#Botão de iniciar
botao_iniciar = tk.Button(frame_botoes, text="Iniciar Jogo", command=iniciar_jogo_handler, width=20)
botao_iniciar.pack(side= "left",pady=10)

#Botão de instruçoes
botao_instrucoes = tk.Button(frame_botoes, text="Instruções", command=mostra_instrucaoes, width=20)
botao_instrucoes.pack(side="left",pady=10)

#Botao de sair
botao_sair = tk.Button(frame_botoes, text="Sair", command=sair_jogo, width=20)
botao_sair.pack(side="left",pady=10)

#Carregar imagem
imagem_engrenagem = Image.open(r"C:\Python\Forca\Imagens\settings.png") # caminho da imagem
imagem_engrenagem = imagem_engrenagem.resize((32, 32)) # tamanho da imagem
imagem_engrenagem_tk = ImageTk.PhotoImage(imagem_engrenagem) 

#Botao de conf
botao_conf = tk.Button(
    janela, 
    image=imagem_engrenagem_tk, 
    command=abrir_menu_cor,  
    #fg="#FFFFFF", 
    padx=10, 
    pady=5
)
botao_conf.pack(side="right")

botao_conf.image = imagem_engrenagem_tk # manter a referencia para envitar que a imagem seja descartada

janela.mainloop()
