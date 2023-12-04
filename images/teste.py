from tkinter import *
import cv2
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

# Função para escolher uma foto do arquivo
def escolher_foto():
    global foto
    caminho = filedialog.askopenfilename(title="Selecione uma foto", filetypes=[("Arquivos de imagem", "*.jpg *.png")])
    if caminho:
        foto = ImageTk.PhotoImage(Image.open(caminho))
        foto_label.configure(image=foto)

# Função para tirar uma nova foto
def tirar_foto():
    global foto
    # Usando a OpenCV para acessar a câmera do computador
    cap = cv2.VideoCapture(0) # 0 é o índice da câmera padrão
    if cap.isOpened():
        ret, frame = cap.read() # Lendo um frame da câmera
        if ret:
            # Convertendo o frame de BGR para RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convertendo o frame para um objeto Image do PIL
            frame = Image.fromarray(frame)
            # Convertendo o frame para um objeto PhotoImage do Tkinter
            foto = ImageTk.PhotoImage(frame)
            # Mostrando a foto na tela
            foto_label.configure(image=foto)
        else:
            messagebox.showerror(
                title="Erro!",
                message="Não foi possível ler a imagem da câmera")
    else:
        messagebox.showerror(
            title="Erro!",
            message="Não foi possível abrir a câmera")
    # Liberando a câmera
    cap.release()

# Função para aplicar um filtro na foto
def aplicar_filtro(filtro):
    global foto
    # Aqui você pode usar alguma biblioteca para aplicar filtros na foto
    # Por exemplo, você pode usar a OpenCV ou a Pillow
    # Para simplificar, vamos usar um filtro padrão
    foto = ImageTk.PhotoImage(Image.open(filtro))
    foto_label.configure(image=foto)

# Função para adicionar um sticker na foto
def adicionar_sticker(sticker):
    global foto
    # Aqui você pode usar alguma biblioteca para adicionar stickers na foto
    # Por exemplo, você pode usar a Pillow ou a PyGame
    # Para simplificar, vamos usar um sticker padrão
    foto = ImageTk.PhotoImage(Image.open(sticker))
    foto_label.configure(image=foto)

# Criando a janela principal
janela = Tk()
janela.title("Editor de Imagens")
janela.geometry("800x600")

# Criando os widgets da parte central
foto_label = Label(janela, width=400, height=400, bg="white")
foto_label.pack(pady=10)

# Criando os widgets da parte inferior
botao_escolher = Button(janela, text="Escolher Foto", command=escolher_foto)
botao_escolher.place(x=100, y=550)

botao_tirar = Button(janela, text="Tirar Foto", command=tirar_foto)
botao_tirar.place(x=200, y=550)

botao_salvar = Button(janela, text="Salvar Foto")
botao_salvar.place(x=300, y=550)

# Criando os widgets da parte esquerda
filtro1 = Button(janela, text="Filtro 1", command=lambda: aplicar_filtro("filtro1.png"))
filtro1.place(x=10, y=100)

filtro2 = Button(janela, text="Filtro 2", command=lambda: aplicar_filtro("filtro2.png"))
filtro2.place(x=10, y=150)

filtro3 = Button(janela, text="Filtro 3", command=lambda: aplicar_filtro("filtro3.png"))
filtro3.place(x=10, y=200)

# Criando os widgets da parte direita
sticker1 = Button(janela, text="Sticker 1", command=lambda: adicionar_sticker("sticker1.png"))
sticker1.place(x=750, y=100)

sticker2 = Button(janela, text="Sticker 2", command=lambda: adicionar_sticker("sticker2.png"))
sticker2.place(x=750, y=150)

sticker3 = Button(janela, text="Sticker 3", command=lambda: adicionar_sticker("sticker3.png"))
sticker3.place(x=750, y=200)

# Iniciando o loop principal
janela.mainloop()
