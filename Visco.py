from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# création de la fenêtre
window = Tk()

# création des frames
framelogo=ttk.Frame(window)
framelogo.place(x=800, y=1500)

#insertion du logo
logo= ImageTk.PhotoImage(Image.open("logouppa.png"))

#création du label pour le logo
labellogo = Label(window, image=logo)
labellogo.pack()

# modifications de la fenêtre
window.title("Banc de Viscosité")
window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("uppa.ico")
window.config(background="#304562")

# afficher la fenêtre
window.mainloop()

