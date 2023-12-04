import numpy as np
import cv2 as cv

class Filters:
    def grayscale_media_aritmetica(self, img):
        img_grayscale_media = img.copy()
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                media = img.item(i, j, 0) * 0.333 + img.item(i, j, 1) * 0.333 + img.item(i, j, 2) * 0.3333
                img_grayscale_media.itemset((i, j, 0), media)
                img_grayscale_media.itemset((i, j, 1), media)
                img_grayscale_media.itemset((i, j, 2), media)
        return img_grayscale_media

    def grayscale_apenas_um_canal(self, img):
        img_grayscale = img.copy()
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                B = img_grayscale.item(i, j, 0)
                img_grayscale.itemset((i, j, 0), B)
                img_grayscale.itemset((i, j, 1), B)
                img_grayscale.itemset((i, j, 2), B)
        return img_grayscale

    def color_ramp(self, img):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_color_ramp = img.copy()
        for i in range(img_gray.shape[0]):
            for j in range(img_gray.shape[1]):
                # "color ramp"
                if img_gray.item(i, j) < 100:
                    img_color_ramp.itemset((i, j, 0), 255)
                    img_color_ramp.itemset((i, j, 1), 255)
                    img_color_ramp.itemset((i, j, 2), 0)
                elif img_gray.item(i, j) < 150:
                    img_color_ramp.itemset((i, j, 0), 255)
                    img_color_ramp.itemset((i, j, 1), 0)
                    img_color_ramp.itemset((i, j, 2), 255)
                else:
                    img_color_ramp.itemset((i, j, 0), 0)
                    img_color_ramp.itemset((i, j, 1), 255)
                    img_color_ramp.itemset((i, j, 2), 255)
        return img_color_ramp

    def renderizar_canal_vermelho(self, img):
        img_red = img.copy()
        for line in range(img.shape[0]):
            for column in range(img.shape[1]):
                img_red.itemset((line, column, 1), 0)
                img_red.itemset((line, column, 2), 0)
        return img_red

    def renderizar_canal_verde(self, img):
        img_green = img.copy()
        for line in range(img.shape[0]):
            for column in range(img.shape[1]):
                img_green.itemset((line, column, 0), 0)
                img_green.itemset((line, column, 2), 0)
        return img_green

    def renderizar_canal_azul(self, img):
        img_blue = img.copy()
        for line in range(img.shape[0]):
            for column in range(img.shape[1]):
                img_blue.itemset((line, column, 1), 0)
                img_blue.itemset((line, column, 0), 0)
        return img_blue

    def grayscale_media_ponderada(self, img):
        img_grayscale = img.copy()
        for line in range(img.shape[0]):
            for column in range(img.shape[1]):
                media_pond = img.item(line, column, 0) * 0.299 + img.item(line, column, 1) * 0.587 + img.item(line,column,2) * 0.114
                img_grayscale.itemset((line, column, 0), media_pond)
                img_grayscale.itemset((line, column, 1), media_pond)
                img_grayscale.itemset((line, column, 2), media_pond)
        return img_grayscale

    # corUniforme = Uma lista com [R, G, B]
    def colorizar(self, img, corUniforme):
        img_colorized = img.copy()
        for line in range(img.shape[0]):
            for column in range(img.shape[1]):
                B = img.item(line, column, 0) | corUniforme[0]
                G = img.item(line, column, 1) | corUniforme[1]
                R = img.item(line, column, 2) | corUniforme[2]
                img_colorized.itemset((line, column, 0), B)
                img_colorized.itemset((line, column, 1), G)
                img_colorized.itemset((line, column, 2), R)
        return img_colorized

    def inverter(self, img):
        img_inverted = img.copy()
        for line in range(img.shape[0]):
            for column in range(img.shape[1]):
                img_inverted.itemset((line, column, 0), 255 - img.item(line, column, 0))
                img_inverted.itemset((line, column, 1), 255 - img.item(line, column, 1))
                img_inverted.itemset((line, column, 2), 255 - img.item(line, column, 2))
        return img_inverted

    # limiar = 0 e 255
    def binarizar(self, img, limiar):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_binarised = img_gray.copy()
        for line in range(img_gray.shape[0]):
            for column in range(img_gray.shape[1]):
                if img_gray.item(line, column) < limiar:
                    img_binarised.itemset((line, column), 0)
                else:
                    img_binarised.itemset((line, column), 255)
        return img_binarised

    def grayScale_vignette(self, img, raio):
        img_gray = self.grayscale_media_ponderada(img)  # aplica o filtro de grayscale
        img_mixed = self.vignette(img_gray, raio)  # aplica o filtro de vignette
        return img_mixed  # retorna a imagem mista

    def vignette(self, img, raio):
        img_vignette = img.copy()
        h, w = img.shape[:2]  # altura e largura da imagem
        cx, cy = w // 2, h // 2  # centro da imagem
        for line in range(h):
            for column in range(w):
                d = ((line - cy) ** 2 + (column - cx) ** 2) ** 0.43  # distância do pixel ao centro
                f = max(0, 1 - d / raio)  # fator de escurecimento
                img_vignette[line, column] = img_vignette[line, column] * f  # multiplica o pixel pelo fator
        return img_vignette
    
    def sharp(self, img):
        sharpKernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
        img_sharp = cv.filter2D(img, -1, sharpKernel)
        return img_sharp

    def canny(self, img):
        img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        img_canny = cv.Canny(img_gray, 50, 100)
        return img_canny
    
    def pencil_sketch_gray(self, img):
        img_pencil_sketch_gray, img_pencil_sketch_color = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) # inbuilt function to generate pencil sketch in both color and grayscale
        return img_pencil_sketch_gray
    
    def pencil_sketch_color(self, img):
        img_pencil_sketch_gray, img_pencil_sketch_color = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) # inbuilt function to generate pencil sketch in both color and grayscale
        return img_pencil_sketch_color
