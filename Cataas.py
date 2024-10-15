from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from pygame.examples.moveit import load_image

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Ошибка: {e}')
        return None

def update_img():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img

def quit():
    window.destroy()

window = Tk()
window.title('Cats')
window.geometry('600x520')

menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Обновить фото', command=update_img)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit)


label = Label()
label.pack()

url = 'https://cataas.com/cat'

update_img()

window.mainloop()