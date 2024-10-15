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
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Ошибка: {e}')
        return None

def update_img():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img

window = Tk()
window.title('Cats')
window.geometry('600x480')

label = Label()
label.pack()

update_button = Button(text='Обновить изображение', command=update_img)
update_button.pack()

url = 'https://cataas.com/cat'

update_img()

window.mainloop()