from tkinter import Tk, Label, Button, filedialog
from tkinter.constants import CENTER

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
        capture = cv2.VideoCapture(0)
        if not capture.isOpened():
            print('Unable to open')
            exit(0)

        ret, frame = capture.read()
        if frame is None:
            return

        # Display the resulting frame
        self.display_image(frame)

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
            if (isinstance(file_path, np.ndarray)):
                # Converte a imagem para o formato RGB
                img = cv2.cvtColor(file_path, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
            else:
                img = Image.open(file_path)
                # Converte a imagem para o formato RGB
                img = img.convert("RGB")
                
            img = img.resize((300, 300))

            img_tk = ImageTk.PhotoImage(img)

            self.image_label.img = img_tk
            self.image_label.config(image=img_tk)

            self.image_label.place(relx=0.5, rely=0.5, anchor=CENTER)

            self.filters = Filters()

            info_img = self.image_label.place_info()
            x_img = info_img['x']
            y_img = info_img['y']

            # Cria miniaturas das imagens com filtros aplicados
            img_red = self.filters.renderizar_canal_vermelho(np.array(img))
            img_green = self.filters.renderizar_canal_verde(np.array(img))
            img_blue = self.filters.renderizar_canal_azul(np.array(img))
            img_gray = self.filters.grayscale_media_ponderada(np.array(img))
            img_color = self.filters.colorizar(np.array(img), [50, 100, 200])
            img_invert = self.filters.inverter(np.array(img))
            img_binarize = self.filters.binarizar(np.array(img), 150)
            img_gray_vignette = self.filters.grayScale_vignette(np.array(img), 225)
            img_vignette = self.filters.vignette(np.array(img), 225)
            img_sharp = self.filters.sharp(np.array(img))
            img_canny = self.filters.canny(np.array(img))

            # Redimensiona as miniaturas
            img_red_thumb = Image.fromarray(img_red).resize((50, 50))
            img_green_thumb = Image.fromarray(img_green).resize((50, 50))
            img_blue_thumb = Image.fromarray(img_blue).resize((50, 50))
            img_gray_thumb = Image.fromarray(img_gray).resize((50, 50))
            img_color_thumb = Image.fromarray(img_color).resize((50, 50))
            img_invert_thumb = Image.fromarray(img_invert).resize((50, 50))
            img_binarize_thumb = Image.fromarray(img_binarize).resize((50, 50))
            img_gray_vignette_thumb = Image.fromarray(img_gray_vignette).resize((50, 50))
            img_vignette_thumb = Image.fromarray(img_vignette).resize((50, 50))
            img_sharp_thumb = Image.fromarray(img_sharp).resize((50, 50))
            img_canny_thumb = Image.fromarray(img_canny).resize((50, 50))

            # Converte miniaturas para o formato do Tkinter
            img_red_tk = ImageTk.PhotoImage(img_red_thumb)
            img_green_tk = ImageTk.PhotoImage(img_green_thumb)
            img_blue_tk = ImageTk.PhotoImage(img_blue_thumb)
            img_gray_tk = ImageTk.PhotoImage(img_gray_thumb)
            img_color_tk = ImageTk.PhotoImage(img_color_thumb)
            img_invert_tk = ImageTk.PhotoImage(img_invert_thumb)
            img_binarize_tk = ImageTk.PhotoImage(img_binarize_thumb)
            img_gray_vignette_tk = ImageTk.PhotoImage(img_gray_vignette_thumb)
            img_vignette_tk = ImageTk.PhotoImage(img_vignette_thumb)
            img_sharp_tk = ImageTk.PhotoImage(img_sharp_thumb)
            img_canny_tk = ImageTk.PhotoImage(img_canny_thumb)
            
            # Cria botões com miniaturas das imagens
            self.red_button = Button(image=img_red_tk, command=lambda: self.renderizar_canal_vermelho(img))
            self.red_button.image = img_red_tk  # Mantém uma referência para a imagem
            self.red_button.grid(row=5, column=0)

            self.green_button = Button(image=img_green_tk, command=lambda: self.renderizar_canal_verde(img))
            self.green_button.image = img_green_tk
            self.green_button.grid(row=5, column=1)

            self.blue_button = Button(image=img_blue_tk, command=lambda: self.renderizar_canal_azul(img))
            self.blue_button.image = img_blue_tk
            self.blue_button.grid(row=5, column=2)

            # Cria um botão com a miniatura da imagem em escala de cinza
            self.gray_button = Button(image=img_gray_tk, command=lambda: self.grayscale_media_ponderada(img))
            self.gray_button.image = img_gray_tk
            self.gray_button.grid(row=5, column=3)

            # Cria um botão com a miniatura da imagem colorida
            self.color_button = Button(image=img_color_tk, command=lambda: self.colorizar(img, [50, 100, 200]))
            self.color_button.image = img_color_tk
            self.color_button.grid(row=5, column=4)

            # Cria um botão com a miniatura da imagem invertida
            self.invert_button = Button(image=img_invert_tk, command=lambda: self.inverter(img))
            self.invert_button.image = img_invert_tk
            self.invert_button.grid(row=5, column=5)

            # Cria um botão com a miniatura da imagem binarizada
            self.binarize_button = Button(image=img_binarize_tk, command=lambda: self.binarizar(img, 150))
            self.binarize_button.image = img_binarize_tk
            self.binarize_button.grid(row=5, column=6)

            # Cria um botão com a miniatura da imagem em escala de cinza com vinhetagem
            self.gray_vignette_button = Button(image=img_gray_vignette_tk,
                                               command=lambda: self.grayScale_vignette(img, 225))
            self.gray_vignette_button.image = img_gray_vignette_tk
            self.gray_vignette_button.grid(row=5, column=7)

            # Cria um botão com a miniatura da imagem colorida com vinhetagem
            self.vignette_button = Button(image=img_vignette_tk,
                                          command=lambda: self.vignette(img, 225))
            self.vignette_button.image = img_vignette_tk
            self.vignette_button.grid(row=5, column=8)

            # Cria um botão com a miniatura da imagem afiada
            self.sharp_button = Button(image=img_sharp_tk,command=lambda: self.sharp(img))
            self.sharp_button.image = img_sharp_tk
            self.sharp_button.grid(row=5, column=9)

            # Cria um botão com a miniatura da imagem canny
            self.canny_button = Button(image=img_canny_tk,command=lambda: self.canny(img))
            self.canny_button.image = img_canny_tk
            self.canny_button.grid(row=5, column=10)

        except Exception as e:
            print(f"Error displaying image: {e}")
    def save_image(self):
        # Lógica para salvar a imagem editada (não implementada aqui)
        pass

    def renderizar_canal_vermelho(self, img):
        img = np.array(img)
        img_red = self.filters.renderizar_canal_vermelho(img)

        img_red_tk = self.convertImgTk(img_red)

        self.image_label.img = img_red_tk
        self.image_label.config(image=img_red_tk)

    def renderizar_canal_verde(self, img):
        img = np.array(img)
        img_green = self.filters.renderizar_canal_verde(img)

        img_green_tk = self.convertImgTk(img_green)

        self.image_label.img = img_green_tk
        self.image_label.config(image=img_green_tk)

    def renderizar_canal_azul(self, img):
        img = np.array(img)
        img_blue = self.filters.renderizar_canal_azul(img)

        img_blue_tk = self.convertImgTk(img_blue)

        self.image_label.img = img_blue_tk
        self.image_label.config(image=img_blue_tk)

    def grayscale_media_ponderada(self, img):
        img = np.array(img)
        img_gray = self.filters.grayscale_media_ponderada(img)

        img_gray_tk = self.convertImgTk(img_gray)
        # Atualiza a imagem no label
        self.image_label.img = img_gray_tk
        self.image_label.config(image=img_gray_tk)

    def colorizar(self, img, corUniforme):
        img = np.array(img)
        img_color = self.filters.colorizar(img, corUniforme)

        img_color_tk = self.convertImgTk(img_color)

        self.image_label.img = img_color_tk
        self.image_label.config(image=img_color_tk)

    def inverter(self, img):
        img = np.array(img)
        img_invert = self.filters.inverter(img)

        img_invert_tk = self.convertImgTk(img_invert)

        self.image_label.img = img_invert_tk
        self.image_label.config(image=img_invert_tk)

    def binarizar(self, img, limiar):
        img = np.array(img)
        img_binarize = self.filters.binarizar(img, limiar)

        img_binarize_tk = self.convertImgTk(img_binarize)

        self.image_label.img = img_binarize_tk
        self.image_label.config(image=img_binarize_tk)

    def grayScale_vignette(self, img, raio):
        img = np.array(img)
        img_gray_vignette = self.filters.grayScale_vignette(img, raio)

        img_gray_vignette_tk = self.convertImgTk(img_gray_vignette)

        self.image_label.img = img_gray_vignette_tk
        self.image_label.config(image=img_gray_vignette_tk)

    def vignette(self, img, raio):
        img = np.array(img)
        img_vignette = self.filters.vignette(img, raio)

        img_vignette_tk = self.convertImgTk(img_vignette)

        self.image_label.img = img_vignette_tk
        self.image_label.config(image=img_vignette_tk)

    def sharp(self, img):
        img = np.array(img)

        img_sharp = self.filters.sharp(img)

        img_sharp_tk = self.convertImgTk(img_sharp)

        self.image_label.img = img_sharp_tk
        self.image_label.config(image=img_sharp_tk)

    def canny(self, img):
        img = np.array(img)

        img_canny = self.filters.canny(img)

        img_canny_tk = self.convertImgTk(img_canny)

        self.image_label.img = img_canny_tk
        self.image_label.config(image=img_canny_tk)

    def convertImgTk(self, img):
        img = Image.fromarray(img)
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)
        return img
        
    def save_image(self):
        # Lógica para salvar a imagem editada (não implementada aqui)
        pass


def main():
    app = ImageEditorApp()


if __name__ == "__main__":
    main()
