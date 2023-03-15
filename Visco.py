from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# création de la fenêtre
window = Tk()

# création des frames
framelogo = ttk.Frame(window)
framelogo.place(x=-180, y=-50)

frameGraphique = ttk.Frame(window)
frameGraphique.place(x=20, y=80)

framePlacement1 = ttk.Frame(window)
framePlacement1.place(x=500, y=100)

framePlacement2 = ttk.Frame(window)
framePlacement2.place(x=1000, y=100)

#insertion du logo
logo = Image.open("logouppa.png")
logo_resize = logo.resize((450, 150), Image.ANTIALIAS)

#Création de l'image
imglogo = ImageTk.PhotoImage(logo_resize)

#création du label pour le logo
labellogo = Label(framelogo, image=imglogo, background="#304562")
labellogo.pack()

def plot_graphs():
    # Créez des données pour le graphique
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    # Créez un graphique avec les données
    fig1 = plt.Figure(figsize=(5,4), dpi=100)
    ax1 = fig1.add_subplot(111)
    ax1.plot(x, y)
    ax1.set_title("Graphique Réel")
    ax1.set_xlabel("Axe X")
    ax1.set_ylabel("Axe Y")

    # Créez des données pour le graphique
    w = [5, 6, 7, 8, 9]
    z = [2, 8, 18, 32, 50]

    # Créez un graphique avec les données
    fig2 = plt.Figure(figsize=(5,4), dpi=100)
    ax2 = fig2.add_subplot(111)
    ax2.plot(w, z)
    ax2.set_title("Graphique Imaginaire")
    ax2.set_xlabel("Axe X")
    ax2.set_ylabel("Axe Y")

    # Créez les widgets tkinter pour les graphiques
    canvas1 = FigureCanvasTkAgg(fig1, master=framePlacement1)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=LEFT, padx=20)


    canvas2 = FigureCanvasTkAgg(fig2, master=framePlacement2)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=LEFT, padx=20)


    # Créez un bouton pour cacher les graphiques
    hide_button = Button(window, text="Cacher les graphiques", command=lambda: hide_graphs(canvas1, canvas2, hide_button))
    hide_button.pack(side=LEFT, padx=10)

def hide_graphs(canvas1, canvas2, button):
    # Supprimez les widgets tkinter des graphiques et le bouton
    canvas1.get_tk_widget().pack_forget()
    canvas2.get_tk_widget().pack_forget()
    button.pack_forget()

# création du bouton pour afficher les graphiques
show_button = Button(frameGraphique, text="Afficher les graphiques", command=plot_graphs, bg="#233448", fg="#B1BD11", font=("Arial", 14))
show_button.pack()

# modifications de la fenêtre
window.title("Banc de Viscosité")
window.geometry("1920x1080")
window.minsize(1080, 720)
window.iconbitmap("uppa.ico")
window.config(background="#304562")

# afficher la fenêtre
window.mainloop()
