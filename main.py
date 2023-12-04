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

        self.sticker_image = None
        self.img = None

        self.root.mainloop()

    def take_photo(self):
        capture = cv2.VideoCapture(0)
        if (not capture.isOpened()):
            print('Unable to open')
            exit(0)

        ret, frame = capture.read()
        if frame is None:
            return

        self.display_image(frame)

    def open_file(self):
        file_path = filedialog.askopenfilename()

        if (file_path):
            self.display_image(file_path)

    def display_image(self, file_path):
        try:
            self.root.title("Editor de Imagens")
            # Verifica se origem da imagem é de webcam ou arquivo
            if (isinstance(file_path, np.ndarray)):
                # Converte a imagem para o formato RGB
                self.img = cv2.cvtColor(file_path, cv2.COLOR_BGR2RGB)
                self.img = Image.fromarray(self.img)
            else:
                self.img = Image.open(file_path)
                # Converte a imagem para o formato RGB
                self.img = self.img.convert("RGB")
                
            self.img = self.img.resize((600, 600))

            img_tk = ImageTk.PhotoImage(self.img)

            self.image_label.img = img_tk
            self.image_label.config(image=img_tk)

            # Botao clique do mouse para adicionar sticker
            self.image_label.bind("<Button-1>", self.mouse_click)

            self.image_label.pack(pady=110)

            self.filters = Filters()

            info_img = self.image_label.place_info()
            
            filters_label = Label(text="Filters: ", font=("Arial", 12))
            filters_label.place(x=50, y=730)

            # Posicao y de todos os botoes de filtro
            filters_y_pos = 715

            # Cria miniaturas das imagens com filtros aplicados
            img_red = self.filters.renderizar_canal_vermelho(np.array(self.img))
            img_green = self.filters.renderizar_canal_verde(np.array(self.img))
            img_blue = self.filters.renderizar_canal_azul(np.array(self.img))
            img_gray = self.filters.grayscale_media_ponderada(np.array(self.img))
            img_color = self.filters.colorizar(np.array(self.img), [50, 100, 200])
            img_invert = self.filters.inverter(np.array(self.img))
            img_binarize = self.filters.binarizar(np.array(self.img), 150)
            img_gray_vignette = self.filters.grayScale_vignette(np.array(self.img), 225)
            img_vignette = self.filters.vignette(np.array(self.img), 225)
            img_sharp = self.filters.sharp(np.array(self.img))
            img_canny = self.filters.canny(np.array(self.img))
            img_pencil_sketch_gray = self.filters.pencil_sketch_gray(np.array(self.img))
            img_pencil_sketch_color = self.filters.pencil_sketch_color(np.array(self.img))

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

            red_button = Button(image=img_red_tk, command=lambda: self.renderizar_canal_vermelho(self.img))
            red_button.image = img_red_tk  # Mantém uma referência para a imagem
            red_button.place(x=106, y=filters_y_pos)

            green_button = Button(image=img_green_tk, command=lambda: self.renderizar_canal_verde(self.img))
            green_button.image = img_green_tk
            green_button.place(x=156, y=filters_y_pos)

            blue_button = Button(image=img_blue_tk, command=lambda: self.renderizar_canal_azul(self.img))
            blue_button.image = img_blue_tk
            blue_button.place(x=206, y=filters_y_pos)

            gray_button = Button(image=img_gray_tk, command=lambda: self.grayscale_media_ponderada(self.img))
            gray_button.image = img_gray_tk
            gray_button.place(x=256, y=filters_y_pos)

            color_button = Button(image=img_color_tk, command=lambda: self.colorizar(self.img, [50, 100, 200]))
            color_button.image = img_color_tk
            color_button.place(x=306, y=filters_y_pos)

            invert_button = Button(image=img_invert_tk, command=lambda: self.inverter(self.img))
            invert_button.image = img_invert_tk
            invert_button.place(x=356, y=filters_y_pos)

            binarize_button = Button(image=img_binarize_tk, command=lambda: self.binarizar(self.img, 150))
            binarize_button.image = img_binarize_tk
            binarize_button.place(x=406, y=filters_y_pos)

            gray_vignette_button = Button(image=img_gray_vignette_tk, command=lambda: self.grayScale_vignette(self.img, 275))
            gray_vignette_button.image = img_gray_vignette_tk
            gray_vignette_button.place(x=456, y=filters_y_pos)

            vignette_button = Button(image=img_vignette_tk, command=lambda: self.vignette(self.img, 275))
            vignette_button.image = img_vignette_tk
            vignette_button.place(x=506, y=filters_y_pos)

            # Cria um botão com a miniatura da imagem afiada
            self.sharp_button = Button(image=img_sharp_tk,command=lambda: self.sharp(self.img))
            self.sharp_button.image = img_sharp_tk
            self.sharp_button.place(x=556, y=filters_y_pos)

            # Cria um botão com a miniatura da imagem canny
            self.canny_button = Button(image=img_canny_tk,command=lambda: self.canny(self.img))
            self.canny_button.image = img_canny_tk
            self.canny_button.place(x=606, y=filters_y_pos)

            # Cria um botão com a miniatura da imagem em lapis cinza
            self.pencil_sketch_gray_button = Button(image=img_pencil_sketch_gray_tk,command=lambda: self.pencil_sketch_gray(self.img))
            self.pencil_sketch_gray_button.image = img_pencil_sketch_gray_tk
            self.pencil_sketch_gray_button.place(x=656, y=filters_y_pos)

            # Cria um botão com a miniatura da imagem em lapis colorida
            self.pencil_sketch_color_button = Button(image=img_pencil_sketch_color_tk,command=lambda: self.pencil_sketch_color(self.img))
            self.pencil_sketch_color_button.image = img_pencil_sketch_color_tk
            self.pencil_sketch_color_button.place(x=706, y=filters_y_pos)

            stickers_label = Label(text="Stickers: ", font=("Arial", 12))
            stickers_label.place(x=35, y=800)

            self.sticker_glasses_button = Button(text="Glasses", width=15, command=self.sticker_glasses)
            self.sticker_glasses_button.place(x=105, y=800)

            self.sticker_vindiesel_button = Button(text="VinDiesel", width=15, command=self.sticker_vindiesel)
            self.sticker_vindiesel_button.place(x=225, y=800)

            self.sticker_pokebola_button = Button(text="Pokebola", width=15, command=self.sticker_pokebola)
            self.sticker_pokebola_button.place(x=345, y=800)

            self.sticker_ronaldinho_button = Button(text="Ronaldinho", width=15, command=self.sticker_ronaldinho)
            self.sticker_ronaldinho_button.place(x=465, y=800)

            self.sticker_cachorro_button = Button(text="Cachorro", width=15, command=self.sticker_cachorro)
            self.sticker_cachorro_button.place(x=585, y=800)

            self.sticker_gato_button = Button(text="Gato", width=15, command=self.sticker_gato)
            self.sticker_gato_button.place(x=705, y=800)

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
    
    def sticker_glasses(self):
        sticker_path = '.\images\eyeglasses.png'  # Substitua com o caminho correto do sticker
        sticker_image = cv2.imread(sticker_path, cv2.IMREAD_UNCHANGED)
        sticker_image = cv2.cvtColor(sticker_image, cv2.COLOR_BGRA2RGBA)

        # Redimensiona a imagem
        nova_largura = int(sticker_image.shape[1] * 0.4)
        nova_altura = int(sticker_image.shape[0] * 0.4)
        sticker_image_redimensionada = cv2.resize(sticker_image, (nova_largura, nova_altura))

        self.sticker_image = sticker_image_redimensionada

    def sticker_vindiesel(self):
        sticker_path = '.\\images\\vindiesel.png'  # Substitua com o caminho correto do sticker
        sticker_image = cv2.imread(sticker_path, cv2.IMREAD_UNCHANGED)
        sticker_image = cv2.cvtColor(sticker_image, cv2.COLOR_BGRA2RGBA)

        # Redimensiona a imagem
        nova_largura = int(sticker_image.shape[1] * 0.2)
        nova_altura = int(sticker_image.shape[0] * 0.2)
        sticker_image_redimensionada = cv2.resize(sticker_image, (nova_largura, nova_altura))

        self.sticker_image = sticker_image_redimensionada

    def sticker_pokebola(self):
        sticker_path = '.\images\pokebola.png'  # Substitua com o caminho correto do sticker
        sticker_image = cv2.imread(sticker_path, cv2.IMREAD_UNCHANGED)
        sticker_image = cv2.cvtColor(sticker_image, cv2.COLOR_BGRA2RGBA)

        # Redimensiona a imagem
        nova_largura = int(sticker_image.shape[1] * 0.1)
        nova_altura = int(sticker_image.shape[0] * 0.1)
        sticker_image_redimensionada = cv2.resize(sticker_image, (nova_largura, nova_altura))

        self.sticker_image = sticker_image_redimensionada

    def sticker_ronaldinho(self):
        sticker_path = '.\\images\\ronaldinho.png'  # Substitua com o caminho correto do sticker
        sticker_image = cv2.imread(sticker_path, cv2.IMREAD_UNCHANGED)
        sticker_image = cv2.cvtColor(sticker_image, cv2.COLOR_BGRA2RGBA)

        # Redimensiona a imagem
        nova_largura = int(sticker_image.shape[1] * 0.3)
        nova_altura = int(sticker_image.shape[0] * 0.3)
        sticker_image_redimensionada = cv2.resize(sticker_image, (nova_largura, nova_altura))

        self.sticker_image = sticker_image_redimensionada

    def sticker_cachorro(self):
        sticker_path = '.\\images\\cachorro.png'  # Substitua com o caminho correto do sticker
        sticker_image = cv2.imread(sticker_path, cv2.IMREAD_UNCHANGED)
        sticker_image = cv2.cvtColor(sticker_image, cv2.COLOR_BGRA2RGBA)

        # Redimensiona a imagem
        nova_largura = int(sticker_image.shape[1] * 0.25)
        nova_altura = int(sticker_image.shape[0] * 0.25)
        sticker_image_redimensionada = cv2.resize(sticker_image, (nova_largura, nova_altura))

        self.sticker_image = sticker_image_redimensionada

    def sticker_gato(self):
        sticker_path = '.\\images\\gato.png'  # Substitua com o caminho correto do sticker
        sticker_image = cv2.imread(sticker_path, cv2.IMREAD_UNCHANGED)
        sticker_image = cv2.cvtColor(sticker_image, cv2.COLOR_BGRA2RGBA)

        # Redimensiona a imagem
        nova_largura = int(sticker_image.shape[1] * 0.25)
        nova_altura = int(sticker_image.shape[0] * 0.25)
        sticker_image_redimensionada = cv2.resize(sticker_image, (nova_largura, nova_altura))

        self.sticker_image = sticker_image_redimensionada

    def mouse_click(self, event):
        try:
            # Obtém as coordenadas do clique do mouse dentro do self.image_label
            x, y = event.x, event.y

            # Obtem a imagem atual do Label em formato Tkinter
            img_tk = self.image_label.img
            if img_tk:
                # Converte a imagem Tkinter para PIL
                img_pil = ImageTk.getimage(img_tk)
                # Converte a imagem PIL em NumPy
                img_np = np.array(img_pil)
                # Remove canal alpha para conter apenas RGB
                img_np = cv2.cvtColor(img_np, cv2.COLOR_RGBA2RGB)

                if self.sticker_image is not None:
                    # Aplica a função overlay na imagem principal
                    result_image = self.overlay(np.array(self.img), self.sticker_image, x, y)

                    # Converte a imagem resultante de NumPy para o formato Tkinter
                    img_result_tk = ImageTk.PhotoImage(Image.fromarray(result_image))

                    # Atualiza o Label com a nova imagem resultante
                    self.img = result_image
                    self.image_label.img = img_result_tk
                    self.image_label.config(image=img_result_tk)
        except Exception as e:
            print(f"Error applying overlay: {e}")

    def overlay(self, background, foreground, x_offset=None, y_offset=None):
        bg_h, bg_w, bg_channels = background.shape
        fg_h, fg_w, fg_channels = foreground.shape

        assert bg_channels == 3, f'background image should have exactly 3 channels (RGB). found:{bg_channels}'
        assert fg_channels == 4, f'foreground image should have exactly 4 channels (RGBA). found:{fg_channels}'

        # center by default
        if x_offset is None: x_offset = (bg_w - fg_w) // 2
        if y_offset is None: y_offset = (bg_h - fg_h) // 2

        w = min(fg_w, bg_w, fg_w + x_offset, bg_w - x_offset)
        h = min(fg_h, bg_h, fg_h + y_offset, bg_h - y_offset)

        if w < 1 or h < 1: return

        # clip foreground and background images to the overlapping regions
        bg_x = max(0, x_offset)
        bg_y = max(0, y_offset)
        fg_x = max(0, x_offset * -1)
        fg_y = max(0, y_offset * -1)
        foreground = foreground[fg_y:fg_y + h, fg_x:fg_x + w]
        background_subsection = background[bg_y:bg_y + h, bg_x:bg_x + w]

        # separate alpha and color channels from the foreground image
        foreground_colors = foreground[:, :, :3]
        alpha_channel = foreground[:, :, 3] / 255  # 0-255 => 0.0-1.0

        # construct an alpha_mask that matches the image shape
        alpha_mask = np.dstack((alpha_channel, alpha_channel, alpha_channel))

        # combine the background with the overlay image weighted by alpha
        composite = background_subsection * (1 - alpha_mask) + foreground_colors * alpha_mask

        # overwrite the section of the background image that has been updated
        background[bg_y:bg_y + h, bg_x:bg_x + w] = composite
        out = background.copy()
        return out

def main():
    app = ImageEditorApp()


if __name__ == "__main__":
    main()
