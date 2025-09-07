import tkinter as tk   # Importa Tkinter
from tkinter import messagebox   # Para exibir mensagens
import random   # Para escolher palavras aleatórias

def abrir_jogo_forca():
    palavras = ["escola", "historia", "matematica", "programacao", "tecnologia"]  
    # Lista de palavras possíveis
    palavra = random.choice(palavras)   # Escolhe uma palavra aleatória
    letras_descobertas = ["_"] * len(palavra)   # Mostra a palavra como underline "_"
    tentativas = [6]   # Número de tentativas (lista para poder ser alterada dentro da função)
    letras_erradas = []   # Lista de letras erradas já tentadas

    # Criar janela do jogo
    janela = tk.Toplevel()   
    janela.title("Jogo da Forca")  
    janela.geometry("400x300")  

    # Labels
    label_palavra = tk.Label(janela, text=" ".join(letras_descobertas), font=("Arial", 18))  
    # Mostra a palavra com "_" e letras já descobertas
    label_palavra.pack(pady=10)

    label_tentativas = tk.Label(janela, text=f"Tentativas restantes: {tentativas[0]}", font=("Arial", 12))  
    # Mostra quantas tentativas o jogador ainda tem
    label_tentativas.pack()

    label_erradas = tk.Label(janela, text="Letras erradas: ", font=("Arial", 12))  
    # Mostra as letras já chutadas erradas
    label_erradas.pack()

    # Entrada de letra
    entrada = tk.Entry(janela, font=("Arial", 14), width=5)  
    # Caixa para digitar uma letra
    entrada.pack(pady=10)

    # Função para jogar
    def jogar():
        letra = entrada.get().lower()  # Pega a letra digitada e transforma em minúscula
        entrada.delete(0, tk.END)      # Limpa a caixa de entrada

        if not letra or len(letra) > 1:
            messagebox.showwarning("Aviso", "Digite apenas uma letra!")  
            # Garante que o jogador digite só 1 letra
            return

        if letra in palavra:   # Se a letra está na palavra
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra   # Substitui o "_" pela letra correta
            label_palavra.config(text=" ".join(letras_descobertas))
        else:   # Se a letra não está na palavra
            if letra not in letras_erradas:
                letras_erradas.append(letra)   # Adiciona a letra à lista de erradas
                tentativas[0] -= 1             # Diminui as tentativas
                label_tentativas.config(text=f"Tentativas restantes: {tentativas[0]}")  
                label_erradas.config(text="Letras erradas: " + " ".join(letras_erradas))

        # Condições de vitória/derrota
        if "_" not in letras_descobertas:  
            messagebox.showinfo("Vitória", f"🎉 Você acertou! A palavra era {palavra}.")  
            janela.destroy()
        elif tentativas[0] <= 0:  
            messagebox.showerror("Derrota", f"💀 Você perdeu! A palavra era {palavra}.")  
            janela.destroy()

    # Botão
    botao = tk.Button(janela, text="Tentar", command=jogar)  
    # Botão que chama a função jogar()
    botao.pack(pady=10)
