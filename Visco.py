from tkinter import *

# création de la fenêtre
window = Tk()

# création d'une image
width = 2560
height = 966
image = PhotoImage(file="logouppa.png").subsample(5)
canvas = Canvas(window, width=width, height=height, bg='#304562', bd=0, highlightthickness=0)
canvas.create_image(-200, -60, anchor=NW, image=image)

# placement du canvas en-dessous des boutons
canvas.grid(row=0, column=1, rowspan=7)

# modifications de la fenêtre
window.title("Banc de Viscosité")
window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("uppa.ico")
window.config(background="#304562")

# afficher la fenêtre
window.mainloop()
