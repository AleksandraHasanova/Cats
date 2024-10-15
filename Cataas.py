from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO


allowed_tags = ['sleep', 'jump', 'fight', 'black', 'white', 'bengal', 'siamese', 'cute', 'red','snow','heart']

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

def open_new_window():
    tag = tag_combobox.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)
    if img:
        img_window = Toplevel(window)
        img_window.title('Картинка с котиком')
        img_window.geometry('600x480')
        img_window.iconbitmap('cat_icon.ico')
        label = Label(img_window)
        label.pack()
        label.config(image=img)
        label.image = img

def exit():
    window.destroy()

window = Tk()
window.title('Cats')
window.geometry('200x150')
window.iconbitmap('cat_icon.ico')

menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)

tag_label = Label(text='Выберите тэг')
tag_label.pack(pady=10)

tag_combobox = ttk.Combobox(values=allowed_tags)
tag_combobox.pack(pady=10)

load_btn = Button(window, text='Загрузить по тегу', command=open_new_window)
load_btn.pack()

window.mainloop()