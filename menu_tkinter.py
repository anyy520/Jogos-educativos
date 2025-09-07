import tkinter as tk   # Importa a biblioteca Tkinter para criar a interface gráfica
from jogo_memoria_tk import abrir_jogo_memoria  # Importa a função que abre o jogo da memória
from jogo_forca_tk import abrir_jogo_forca      # Importa a função que abre o jogo da forca

def sair():
    janela.destroy()   # Fecha a janela principal quando o usuário clicar em "Sair"

# Criar a janela principal
janela = tk.Tk()                   # Cria a janela principal do programa
janela.title("Jogos Educativos")   # Define o título da janela
janela.geometry("300x200")         # Define o tamanho da janela (largura x altura)

# Título
titulo = tk.Label(janela, text="Escolha um Jogo", font=("Arial", 16))  # Cria um texto como título
titulo.pack(pady=20)  # Organiza o título na janela com espaçamento (20px de margem vertical)

# Botões do menu
botao_memoria = tk.Button(janela, text="🎴 Jogo da Memória", command=abrir_jogo_memoria, width=20, height=2)  
# Cria um botão que abre o jogo da memória
botao_memoria.pack(pady=5)  # Posiciona o botão com espaçamento de 5px

botao_forca = tk.Button(janela, text="🔠 Jogo da Forca", command=abrir_jogo_forca, width=20, height=2)  
# Cria um botão que abre o jogo da forca
botao_forca.pack(pady=5)  # Posiciona o botão

botao_sair = tk.Button(janela, text="❌ Sair", command=sair, width=20, height=2)  
# Cria um botão que fecha o programa
botao_sair.pack(pady=10)  # Posiciona o botão com margem maior

# Iniciar a janela
janela.mainloop()   # Mantém a janela aberta aguardando interações do usuário
