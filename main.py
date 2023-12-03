from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk
import cv2

class ImageEditorApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Image Editor App")
        self.root.config(padx=10, pady=10)

        welcome_label = Label(text="Welcome to our App! :)", font=("Arial", 16))
        welcome_label.grid(row=0, column=0, columnspan=2, sticky="n")

        option_label = Label(text="Choose an option", font=("Arial", 12))
        option_label.grid(row=1, column=0, columnspan=2, pady=10)

        camera_button = Button(text="Take a photo", width=15, command=self.take_photo)
        camera_button.grid(row=2, column=0, columnspan=2, padx=5)

        file_button = Button(text="Choose an image", width=15, command=self.open_file)
        file_button.grid(row=3, column=0, columnspan=2, padx=5)

        self.image_label = Label(self.root)
        self.image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.root.mainloop()

    def take_photo(self):
        # Lógica para tirar uma foto (não implementada aqui)
        pass

    def open_file(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        try:
            img = cv2.imread(file_path)
            if img is None:
                raise FileNotFoundError("Invalid file or unsupported image format")

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = img.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)

            self.image_label.img = img_tk
            self.image_label.config(image=img_tk)
        except Exception as e:
            print(f"Error displaying image: {e}")

    def save_image(self):
        # Lógica para salvar a imagem editada (não implementada aqui)
        pass

def main():
    app = ImageEditorApp()

if __name__ == "__main__":
    main()
