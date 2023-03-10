from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# création de la fenêtre
window = Tk()

# création des frames
framelogo=ttk.Frame(window)
framelogo.place(x=-130, y=-40)

#insertion du logo
logo= Image.open("logouppa.png")
logo_resize = logo.resize((350, 150), Image.ANTIALIAS)

#Créaton de l'image
imglogo= ImageTk.PhotoImage(logo_resize)

#création du label pour le logo
labellogo = Label(framelogo, image=imglogo, background="#304562")
labellogo.pack()

# modifications de la fenêtre
window.title("Banc de Viscosité")
window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("uppa.ico")
window.config(background="#304562")

# afficher la fenêtre
window.mainloop()


