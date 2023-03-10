from tkinter import *
from tkinter import ttk

#création de la fenètre
window = Tk()

#création du gestionnaire d'onglets
notebook = ttk.Notebook(window)

# création des onglets
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
tab4 = Frame(notebook)
tab5 = Frame(notebook)
tab6 = Frame(notebook)
tab7 = Frame(notebook)

# ajout du texte dans les onglets
Label(tab1, text="Contenu de l'onglet 1").pack(pady=20)
Label(tab2, text="Contenu de l'onglet 2").pack(pady=20)
Label(tab3, text="Contenu de l'onglet 3").pack(pady=20)
Label(tab4, text="Contenu de l'onglet 4").pack(pady=20)
Label(tab5, text="Contenu de l'onglet 5").pack(pady=20)
Label(tab6, text="Contenu de l'onglet 6").pack(pady=20)
Label(tab7, text="Contenu de l'onglet 7").pack(pady=20)

# ajout des onglets au gestionnaire d'onglets
notebook.add(tab1, text="Onglet 1")
notebook.add(tab2, text="Onglet 2")
notebook.add(tab3, text="Onglet 3")
notebook.add(tab4, text="Onglet 4")
notebook.add(tab5, text="Onglet 5")
notebook.add(tab6, text="Onglet 6")
notebook.add(tab7, text="Onglet 7")

# placement des onglets dans une colonne
notebook.grid(row=0, column=0, rowspan=7)

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