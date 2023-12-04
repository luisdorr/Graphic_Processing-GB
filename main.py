from tkinter import Tk, Label, Button, filedialog, Frame

import numpy as np
from PIL import Image, ImageTk
import cv2

from Filters import Filters

class ImageEditorApp:

    def __init__(self):

        self.img_x = 600
        self.img_y = 600
        self.root = Tk()
        self.root.title("Image Editor App")
        self.root.config(padx=10, pady=10)
        self.root.geometry("900x900")

        # Cria os widgets do menu usando o atributo self
        self.welcome_label = Label(text="Welcome to our App! :)", font=("Arial", 16))
        self.welcome_label.place(relx=0.5, y=10, anchor="center")
        
        self.option_label = Label(text="Choose an option", font=("Arial", 12))
        self.option_label.place(relx=0.5, y=35, anchor="center")

        self.camera_button = Button(text="Take a photo", width=15, command=self.take_photo)
        self.camera_button.place(relx=0.5, y=60, anchor="center")

        self.file_button = Button(text="Choose an image", width=15, command=self.open_file)
        self.file_button.place(relx=0.5, y=90, anchor="center")
        
        self.image_label = Label(self.root)
        self.image_label.place(relx=0.5, y=500, anchor="center")

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
        self.root.title("Editor de Imagens")
        self.root.geometry("900x900")
        self.display_image(frame)

    def open_file(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            # Esconde os widgets do menu usando o método grid_forget
            self.root.title("Editor de Imagens")
            self.root.geometry("900x900")
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
                
            img = img.resize((600, 600))

            img_tk = ImageTk.PhotoImage(img)

            self.image_label.img = img_tk
            self.image_label.config(image=img_tk)

            self.image_label.pack(pady=110)

            self.filters = Filters()

            info_img = self.image_label.place_info()
            
            filters_label = Label(text="Filters: ", font=("Arial", 12))
            filters_label.place(x=50, y=730)

            # Pega a posição do label dos filtros para aplicar em todos os botoes
            filters_y_pos = 715

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
            img_pencil_sketch_gray = self.filters.pencil_sketch_gray(np.array(img))
            img_pencil_sketch_color = self.filters.pencil_sketch_color(np.array(img))

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
            img_pencil_sketch_gray_thumb = Image.fromarray(img_pencil_sketch_gray).resize((50, 50))
            img_pencil_sketch_color_thumb = Image.fromarray(img_pencil_sketch_color).resize((50, 50))


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
            img_pencil_sketch_gray_tk = ImageTk.PhotoImage(img_pencil_sketch_gray_thumb)
            img_pencil_sketch_color_tk = ImageTk.PhotoImage(img_pencil_sketch_color_thumb)

            # Cria botões com miniaturas das imagens

            red_button = Button(image=img_red_tk, command=lambda: self.renderizar_canal_vermelho(img))
            red_button.image = img_red_tk  # Mantém uma referência para a imagem
            red_button.place(x=106, y=filters_y_pos)

            green_button = Button(image=img_green_tk, command=lambda: self.renderizar_canal_verde(img))
            green_button.image = img_green_tk
            green_button.place(x=156, y=filters_y_pos)

            blue_button = Button(image=img_blue_tk, command=lambda: self.renderizar_canal_azul(img))
            blue_button.image = img_blue_tk
            blue_button.place(x=206, y=filters_y_pos)

            gray_button = Button(image=img_gray_tk, command=lambda: self.grayscale_media_ponderada(img))
            gray_button.image = img_gray_tk
            gray_button.place(x=256, y=filters_y_pos)

            color_button = Button(image=img_color_tk, command=lambda: self.colorizar(img, [50, 100, 200]))
            color_button.image = img_color_tk
            color_button.place(x=306, y=filters_y_pos)

            invert_button = Button(image=img_invert_tk, command=lambda: self.inverter(img))
            invert_button.image = img_invert_tk
            invert_button.place(x=356, y=filters_y_pos)

            binarize_button = Button(image=img_binarize_tk, command=lambda: self.binarizar(img, 150))
            binarize_button.image = img_binarize_tk
            binarize_button.place(x=406, y=filters_y_pos)

            gray_vignette_button = Button(image=img_gray_vignette_tk,
                                               command=lambda: self.grayScale_vignette(img, 275))
            gray_vignette_button.image = img_gray_vignette_tk
            gray_vignette_button.place(x=456, y=filters_y_pos)

            vignette_button = Button(image=img_vignette_tk,
                                          command=lambda: self.vignette(img, 275))
            vignette_button.image = img_vignette_tk
            vignette_button.place(x=506, y=filters_y_pos)

            # Cria um botão com a miniatura da imagem afiada
            self.sharp_button = Button(image=img_sharp_tk,command=lambda: self.sharp(img))
            self.sharp_button.image = img_sharp_tk
            self.sharp_button.place(x=556, y=filters_y_pos)

            # Cria um botão com a miniatura da imagem canny
            self.canny_button = Button(image=img_canny_tk,command=lambda: self.canny(img))
            self.canny_button.image = img_canny_tk
            self.canny_button.place(x=606, y=filters_y_pos)

            # Cria um botão com a miniatura da imagem em lapis cinza
            self.pencil_sketch_gray_button = Button(image=img_pencil_sketch_gray_tk,command=lambda: self.pencil_sketch_gray(img))
            self.pencil_sketch_gray_button.image = img_pencil_sketch_gray_tk
            self.pencil_sketch_gray_button.place(x=656, y=filters_y_pos)

            # Cria um botão com a miniatura da imagem em lapis colorida
            self.pencil_sketch_color_button = Button(image=img_pencil_sketch_color_tk,command=lambda: self.pencil_sketch_color(img))
            self.pencil_sketch_color_button.image = img_pencil_sketch_color_tk
            self.pencil_sketch_color_button.place(x=706, y=filters_y_pos)

            # Cria um botão para salvar a imagem
            self.save_button = Button(text="Save Image", width=15, command=lambda: self.save_image())
            self.save_button.place(relx=0.5, y=870, anchor="center")


        except Exception as e:
            print(f"Error displaying image: {e}")

    def save_image(self):
        try:
            # Obtém a imagem atual exibida no Label
            img = self.image_label.img

            if (img):
                # Converte a imagem Tkinter para PIL
                img_pil = ImageTk.getimage(img)

                # Abre um diálogo para salvar o arquivo
                file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[(".png", "*.png"), (".jpg", "*.jpg")])

                if (file_path):
                    # Salva a imagem usando o caminho especificado
                    img_pil.save(file_path)
                    print("Image saved successfully.")
                else:
                    print("Specified path not found.")
            else:
                print("No image to save.")

        except Exception as e:
            print(f"Error saving imagee: {e}")

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

    def pencil_sketch_gray(self, img):
        img = np.array(img)

        img_pencil_sketch_gray = self.filters.pencil_sketch_gray(img)

        img_pencil_sketch_gray_tk = self.convertImgTk(img_pencil_sketch_gray)

        self.image_label.img = img_pencil_sketch_gray_tk
        self.image_label.config(image=img_pencil_sketch_gray_tk)

    def pencil_sketch_color(self, img):
        img = np.array(img)

        img_pencil_sketch_color = self.filters.pencil_sketch_color(img)

        img_pencil_sketch_color_tk = self.convertImgTk(img_pencil_sketch_color)

        self.image_label.img = img_pencil_sketch_color_tk
        self.image_label.config(image=img_pencil_sketch_color_tk)

    def convertImgTk(self, img):
        img = Image.fromarray(img)
        img = img.resize((600, 600))
        img = ImageTk.PhotoImage(img)
        return img


def main():
    app = ImageEditorApp()


if __name__ == "__main__":
    main()
