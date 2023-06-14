import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image

def test_graph1():
    # Code d'affichage des graphiques
    def plot_graphs():
        # Ouvrez le fichier TXT contenant les données
        with open('Fichier/releve.txt', 'r') as f:
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
            y.append(float(split_line[1]))
            w.append(float(split_line[0]))
            z.append(float(split_line[2]))

        # Créez une figure avec deux sous-graphiques
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Tracez les données dans les sous-graphiques correspondants
        ax1.plot(x, y, color='blue', linewidth=2)
        ax2.plot(w, z, color='red', linewidth=2)

        # Ajoutez des étiquettes pour les axes X et Y et un titre pour chaque sous-graphique
        ax1.set_xlabel("Axe X", fontsize=12, color='yellow')
        ax1.set_ylabel("Axe Y", fontsize=12, color='yellow')
        ax1.set_title("Graphique Réel", fontsize=14, color='yellow')
        ax2.set_xlabel("Axe X", fontsize=12, color='yellow')
        ax2.set_ylabel("Axe Y", fontsize=12, color='yellow')
        ax2.set_title("Graphique Imaginaire", fontsize=14, color='yellow')

        # Ajouter une grille aux sous-graphiques
        ax1.grid(True)
        ax2.grid(True)

        # Modifier l'apparence de la grille
        ax1.grid(color='gray', linestyle='-', linewidth=0.5)
        ax2.grid(color='gray', linestyle='-', linewidth=0.5)


        # Ajouter une légende aux sous-graphiques
        ax1.legend(['Données réelles'], loc='upper right', fontsize=12)
        ax2.legend(['Données imaginaires'], loc='upper right', fontsize=12)

        # Modifier la couleur de fond de la figure
        fig.patch.set_facecolor('#304562')

        # Créer une fenêtre Tkinter
        root = tk.Tk()
        root.title("Graphe X,Y = f(Freq)")

        # Changer l'icône de la fenêtre
        root.iconbitmap("Image/uppa.ico")

        # Obtenir les dimensions de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Définir les dimensions de la fenêtre en fonction de l'écran
        root_width = int(screen_width * 0.8)
        root_height = int(screen_height * 0.8)
        root_x = int((screen_width - root_width) / 2)
        root_y = int((screen_height - root_height) / 2)

        # Créer un widget Canvas Tkinter pour afficher la figure
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()

        # Modifier la couleur de fond de la fenêtre Tkinter
        root.configure(bg='#304562')

        # Fonction de redimensionnement des graphiques en fonction de la taille de la fenêtre
        def resize_graphs(event):
            # Récupérer la taille de la fenêtre
            width = event.width
            height = event.height

            # Calculer la nouvelle taille des graphiques en fonction de la taille de la fenêtre
            figsize = (width /100, height / 100)  # Ajustez les valeurs selon vos besoins

            # Mettre à jour la taille des graphiques
            #fig.set_size_inches(figsize)
            fig.subplots_adjust(left=1, right=1, top=1, bottom=1)  # Ajuster les marges selon vos besoins
            canvas.draw()

        # Lier la fonction de redimensionnement à l'événement de redimensionnement de la fenêtre
        root.bind('<Configure>', resize_graphs)

        # Créer une étiquette pour le titre
        title_label = tk.Label(root, text='Banc de viscosité', font=('Arial', 16), fg='yellow', bg='#233448')
        title_label.pack(pady=10)

        # Afficher le widget Canvas
        canvas.get_tk_widget().pack()

        # Lancer la boucle principale Tkinter
        tk.mainloop()


    # Appeler la fonction pour afficher les graphiques
    plot_graphs()
