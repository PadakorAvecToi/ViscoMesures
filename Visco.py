from tkinter import *

# création de la fenêtre
window = Tk()

# création d'une image
width = 2560
height = 966
image = PhotoImage(file="logouppa.png").subsample(5)
canvas = Canvas(window, width=width, height=height, bg='#304562', bd=0, highlightthickness=0)
canvas.create_image(-200, -60, anchor=NW, image=image)




# création des boutons
def open_tab(tab_num):
    # fonction pour ouvrir une nouvelle page en fonction du numéro de l'onglet
    page = Toplevel(window)
    Label(page, text=f"Contenu de l'onglet {tab_num}").pack(pady=20)

Button(window, text="Onglet 1", font=("Courier", 15), fg='#B2BE12', bg='#233448', bd=0, highlightthickness=0, height= 1, width= 1, command=lambda: open_tab(1)).grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
Button(window, text="Onglet 2", font=("Courier", 15), fg='#B2BE12', bg='#233448', bd=0, highlightthickness=0, command=lambda: open_tab(2)).grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
Button(window, text="Onglet 3", font=("Courier", 15), fg='#B2BE12', bg='#233448', bd=0, highlightthickness=0, command=lambda: open_tab(3)).grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
Button(window, text="Onglet 4", font=("Courier", 15), fg='#B2BE12', bg='#233448', bd=0, highlightthickness=0, command=lambda: open_tab(4)).grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
Button(window, text="Onglet 5", font=("Courier", 15), fg='#B2BE12', bg='#233448', bd=0, highlightthickness=0, command=lambda: open_tab(5)).grid(row=4, column=0, sticky="nsew", padx=10, pady=10)
Button(window, text="Onglet 6", font=("Courier", 15), fg='#B2BE12', bg='#233448', bd=0, highlightthickness=0, command=lambda: open_tab(6)).grid(row=5, column=0, sticky="nsew", padx=10, pady=10)
Button(window, text="Onglet 7", font=("Courier", 15), fg='#B2BE12', bg='#233448', bd=0, highlightthickness=0, command=lambda: open_tab(7)).grid(row=6, column=0, sticky="nsew", padx=10, pady=10)






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
