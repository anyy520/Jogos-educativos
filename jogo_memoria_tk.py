import tkinter as tk   # Importa Tkinter para criar a interface
from tkinter import messagebox   # Importa messagebox para mostrar janelas de aviso/erro/sucesso
import random   # Importa a biblioteca random para escolher perguntas aleatórias

def abrir_jogo_memoria():
    perguntas = {       # Dicionário com perguntas e respostas corretas
        "5 + 3": "8",
        "9 - 4": "5",
        "6 x 2": "12",
        "12 ÷ 3": "4"
    }

    # Escolhe uma pergunta aleatoriamente
    pergunta, resposta_certa = random.choice(list(perguntas.items()))

    # Criar janela do jogo
    janela = tk.Toplevel()         # Cria uma nova janela (independente do menu principal)
    janela.title("Jogo da Memória")  
    janela.geometry("300x200")  

    # Exibir pergunta
    label_pergunta = tk.Label(janela, text=f"Quanto é {pergunta}?", font=("Arial", 14))  
    # Cria um texto com a pergunta escolhida
    label_pergunta.pack(pady=20)  

    # Caixa de entrada
    entrada = tk.Entry(janela, font=("Arial", 14))  # Caixa para o jogador digitar a resposta
    entrada.pack(pady=10)

    # Função para verificar resposta
    def verificar():
        tentativa = entrada.get()  # Pega o que o usuário digitou
        if tentativa == resposta_certa:
            messagebox.showinfo("Resultado", "✅ Parabéns, você acertou!")  
            # Mostra mensagem de acerto
        else:
            messagebox.showerror("Resultado", f"❌ Errou! A resposta correta era {resposta_certa}.")  
            # Mostra mensagem de erro
        janela.destroy()  # Fecha a janela do jogo depois da resposta

    # Botão de confirmar
    botao = tk.Button(janela, text="Responder", command=verificar)  
    # Botão que chama a função de verificação
    botao.pack(pady=10)
