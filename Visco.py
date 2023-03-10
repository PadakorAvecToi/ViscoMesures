from tkinter import *
from tkinter import ttk

#création de la fenètre
window = Tk()

#création d'un onglet
#notebook = ttk.Notebook(window)
#tab1 = Frame(notebook, bg="red")
#tab2 = Frame(notebook, bg="green")
#notebook.add(tab1, text="Onglet 1")
#notebook.add(tab2, text="Onglet 2")
#notebook.pack(expand=1, fill="both")

#Ajouter des labels aux onglets
#Label(tab1, text="Contenu de l'onglet 1").pack(padx=10, pady=10)
#Label(tab2, text="Contenu de l'onglet 2").pack(padx=10, pady=10)


#Modifications de la fenètre
window.title("Banc de Viscosité")
window.geometry("1080x720")
window.minsize(1080,720)
window.iconbitmap("uppa.ico")
window.config(background="#304562")

#Création d'une image
width = 2560
height = 966
image = PhotoImage(file="logouppa.png").subsample(5)
canvas = Canvas(window, width=width, height=height, bg='#304562', bd=0, highlightthickness=0)
canvas.create_image(-200, -60, anchor=NW, image=image)
canvas.pack()

#Création d'un boutton
Premier_boutton = Button(text="test du boutton", font=("Courrier", 15), fg='#B2BE12', bg='#233448', bd=0, highlightthickness=0)
Premier_boutton.pack()
Premier_boutton.place(x=10, y=100)

#Afficher la fenètre
window.mainloop()