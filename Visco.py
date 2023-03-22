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

#====================================================================================================

def plot_graphs():

    # Ouvrez le fichier TXT contenant les données
    with open('ametek air 480.945 etuve 20°.1C fil 0.1mm 0.06V dans cellule.txt', 'r') as f:
        data = f.read().splitlines()

    # Créez des listes pour stocker les données
    x = []
    y = []
    w = []
    z = []

    # Parcourez chaque ligne du fichier TXT
    for line in data[1:]:
        # Séparez les valeurs x, y, w et z en utilisant la tabulation comme séparateur
        split_line = line.split('\t')
        x.append(float(split_line[0]))
        y.append(float(split_line[3]))
        w.append(float(split_line[1]))
        z.append(float(split_line[4]))

    # Créez une figure avec deux sous-graphiques
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Tracez les données dans les sous-graphiques correspondants
    ax1.plot(x, y, color='blue', linewidth=2)
    ax2.plot(w, z, color='red', linewidth=2)

    # Ajoutez des étiquettes pour les axes X et Y et un titre pour chaque sous-graphique
    ax1.set_xlabel("Axe X", fontsize=12)
    ax1.set_ylabel("Axe Y", fontsize=12)
    ax1.set_title("Graphique Réel", fontsize=14)
    ax2.set_xlabel("Axe X", fontsize=12)
    ax2.set_ylabel("Axe Y", fontsize=12)
    ax2.set_title("Graphique Imaginaire", fontsize=14)

    # Ajouter une grille aux sous-graphiques
    ax1.grid(True)
    ax2.grid(True)

    # Modifier l'apparence de la grille
    ax1.grid(color='gray', linestyle='-', linewidth=0.7)
    ax2.grid(color='gray', linestyle='-', linewidth=0.7),

    # Ajouter une légende aux sous-graphiques
    ax1.legend(['Données réelles'], loc='upper right', fontsize=12)
    ax2.legend(['Données imaginaires'], loc='upper right', fontsize=12)

    # Modifier la couleur de fond de la figure
    fig.patch.set_facecolor('#233448')

    # Modifier les marges autour des sous-graphiques
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)


    fig = plt.figure()
    fig.set_size_inches(21, 12)

    # Afficher la fenêtre avec les deux graphiques
    plt.show()

#====================================================================================================

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
