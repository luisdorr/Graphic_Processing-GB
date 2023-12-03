from tkinter import Tk, Label, Button, filedialog

import numpy as np
from PIL import Image, ImageTk
import cv2

from Filters import Filters


class ImageEditorApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Image Editor App")
        self.root.config(padx=10, pady=10)

        # Cria os widgets do menu usando o atributo self
        self.welcome_label = Label(text="Welcome to our App! :)", font=("Arial", 16))
        self.welcome_label.grid(row=0, column=0, columnspan=2, sticky="n")

        self.option_label = Label(text="Choose an option", font=("Arial", 12))
        self.option_label.grid(row=1, column=0, columnspan=2, pady=10)

        self.camera_button = Button(text="Take a photo", width=15, command=self.take_photo)
        self.camera_button.grid(row=2, column=0, columnspan=2, padx=5)

        self.file_button = Button(text="Choose an image", width=15, command=self.open_file)
        self.file_button.grid(row=3, column=0, columnspan=2, padx=5)

        self.image_label = Label(self.root)
        self.image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.root.mainloop()

    def take_photo(self):
        # Lógica para tirar uma foto (não implementada aqui)
        pass

    def open_file(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            # Esconde os widgets do menu usando o método grid_forget
            self.welcome_label.grid_forget()
            self.option_label.grid_forget()
            self.camera_button.grid_forget()
            self.file_button.grid_forget()

            self.display_image(file_path)

    def display_image(self, file_path):
        try:
            # Carrega a imagem do arquivo
            img = Image.open(file_path)
            # Converte a imagem para o formato RGB
            img = img.convert("RGB")
            # Redimensiona a imagem para 300x300 pixels
            img = img.resize((300, 300))
            # Converte a imagem para o formato do Tkinter
            img_tk = ImageTk.PhotoImage(img)
            # Atualiza a imagem no label
            self.image_label.img = img_tk
            self.image_label.config(image=img_tk)

            # Cria uma instância da classe Filters
            self.filters = Filters()

            # Cria os botões para os filtros
            self.red_button = Button(text="Red", width=10, command=lambda: self.renderizar_canal_vermelho(img))
            self.red_button.grid(row=5, column=0, padx=5, pady=5)

            self.green_button = Button(text="Green", width=10, command=lambda: self.renderizar_canal_verde(img))
            self.green_button.grid(row=5, column=1, padx=5, pady=5)

            self.blue_button = Button(text="Blue", width=10, command=lambda: self.renderizar_canal_azul(img))
            self.blue_button.grid(row=5, column=2, padx=5, pady=5)

            self.gray_button = Button(text="Gray", width=10, command=lambda: self.grayscale_media_ponderada(img))
            self.gray_button.grid(row=6, column=0, padx=5, pady=5)

            self.color_button = Button(text="Color", width=10, command=lambda: self.colorizar(img, [50, 100, 200]))
            self.color_button.grid(row=6, column=1, padx=5, pady=5)

            self.invert_button = Button(text="Invert", width=10, command=lambda: self.inverter(img))
            self.invert_button.grid(row=6, column=2, padx=5, pady=5)

            self.binarize_button = Button(text="Binarize", width=10, command=lambda: self.binarizar(img, 150))
            self.binarize_button.grid(row=7, column=0, padx=5, pady=5)

            self.gray_vignette_button = Button(text="Gray Vignette", width=10,
                                               command=lambda: self.grayScale_vignette(img, 225))
            self.gray_vignette_button.grid(row=7, column=1, padx=5, pady=5)

            self.vignette_button = Button(text="Vignette", width=10, command=lambda: self.vignette(img, 225))
            self.vignette_button.grid(row=7, column=2, padx=5, pady=5)

        except Exception as e:
            print(f"Error displaying image: {e}")
    def save_image(self):
        # Lógica para salvar a imagem editada (não implementada aqui)
        pass

    def renderizar_canal_vermelho(self, img):
        img = np.array(img)
        img_red = self.filters.renderizar_canal_vermelho(img)

        img_red = Image.fromarray(img_red)
        img_red = img_red.resize((300, 300))
        img_red_tk = ImageTk.PhotoImage(img_red)

        self.image_label.img = img_red_tk
        self.image_label.config(image=img_red_tk)

    def renderizar_canal_verde(self, img):
        img = np.array(img)
        img_green = self.filters.renderizar_canal_verde(img)

        img_green = Image.fromarray(img_green)
        img_green = img_green.resize((300, 300))
        img_green_tk = ImageTk.PhotoImage(img_green)

        self.image_label.img = img_green_tk
        self.image_label.config(image=img_green_tk)

    def renderizar_canal_azul(self, img):
        img = np.array(img)
        img_blue = self.filters.renderizar_canal_azul(img)

        img_blue = Image.fromarray(img_blue)
        img_blue = img_blue.resize((300, 300))
        img_blue_tk = ImageTk.PhotoImage(img_blue)

        self.image_label.img = img_blue_tk
        self.image_label.config(image=img_blue_tk)

    def grayscale_media_ponderada(self, img):
        img = np.array(img)
        img_gray = self.filters.grayscale_media_ponderada(img)

        img_gray = Image.fromarray(img_gray)
        img_gray = img_gray.resize((300, 300))
        img_gray_tk = ImageTk.PhotoImage(img_gray)
        # Atualiza a imagem no label
        self.image_label.img = img_gray_tk
        self.image_label.config(image=img_gray_tk)

    def colorizar(self, img, corUniforme):
        img = np.array(img)
        img_color = self.filters.colorizar(img, corUniforme)

        img_color = Image.fromarray(img_color)
        img_color = img_color.resize((300, 300))
        img_color_tk = ImageTk.PhotoImage(img_color)

        self.image_label.img = img_color_tk
        self.image_label.config(image=img_color_tk)

    def inverter(self, img):
        img = np.array(img)
        img_invert = self.filters.inverter(img)

        img_invert = Image.fromarray(img_invert)
        img_invert = img_invert.resize((300, 300))
        img_invert_tk = ImageTk.PhotoImage(img_invert)

        self.image_label.img = img_invert_tk
        self.image_label.config(image=img_invert_tk)

    def binarizar(self, img, limiar):
        img = np.array(img)
        img_binarize = self.filters.binarizar(img, limiar)

        img_binarize = Image.fromarray(img_binarize)
        img_binarize = img_binarize.resize((300, 300))
        img_binarize_tk = ImageTk.PhotoImage(img_binarize)

        self.image_label.img = img_binarize_tk
        self.image_label.config(image=img_binarize_tk)

    def grayScale_vignette(self, img, raio):
        img = np.array(img)
        img_gray_vignette = self.filters.grayScale_vignette(img, raio)

        img_gray_vignette = Image.fromarray(img_gray_vignette)
        img_gray_vignette = img_gray_vignette.resize((300, 300))
        img_gray_vignette_tk = ImageTk.PhotoImage(img_gray_vignette)

        self.image_label.img = img_gray_vignette_tk
        self.image_label.config(image=img_gray_vignette_tk)

    def vignette(self, img, raio):
        img = np.array(img)
        img_vignette = self.filters.vignette(img, raio)

        img_vignette = Image.fromarray(img_vignette)
        img_vignette = img_vignette.resize((300, 300))
        img_vignette_tk = ImageTk.PhotoImage(img_vignette)

        self.image_label.img = img_vignette_tk
        self.image_label.config(image=img_vignette_tk)

    def save_image(self):
        # Lógica para salvar a imagem editada (não implementada aqui)
        pass


def main():
    app = ImageEditorApp()


if __name__ == "__main__":
    main()
