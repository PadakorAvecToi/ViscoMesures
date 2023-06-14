import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import nidaqmx
import nidaqmx.constants

def graphique_numero2():
    
    def adjust_window_size(root):
        # Obtenir les dimensions de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Définir les dimensions de la fenêtre en fonction de l'écran
        root_width = int(screen_width * 0.8)
        root_height = int(screen_height * 0.8)
        root_x = int((screen_width - root_width) / 2)
        root_y = int((screen_height - root_height) / 2)

        # Définir les dimensions et la position de la fenêtre
        root.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")


    def plot_graphs(root):
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
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10), sharex=True)

        # Tracez les données dans les sous-graphiques correspondants
        ax1.plot(x, y, color='blue', linewidth=2)
        ax2.plot(w, z, color='red', linewidth=2)

        # Ajoutez des étiquettes pour les axes X et Y et un titre pour chaque sous-graphique
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

        # Créer un widget Canvas Tkinter pour afficher la figure
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky='nsew')

        # Redimensionner le widget Canvas en fonction de la taille de la fenêtre
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)


    def display_table(root):
        # Ouvrir le fichier texte contenant les valeurs
        with open('Fichier/releve.txt', 'r') as file:
            lines = file.readlines()

        # Créer un widget de tableau Tkinter
        table = tk.LabelFrame(root, text='Tableau')
        table.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Parcourir les lignes du fichier texte
        for i, line in enumerate(lines):
            # Supprimer les sauts de ligne et diviser la ligne en valeurs individuelles
            values = line.strip().split('\t')

            # Afficher les valeurs dans des étiquettes de texte
            for j, value in enumerate(values):
                label = tk.Label(table, text=value, relief='solid', width=12)
                label.grid(row=i, column=j, padx=5, pady=5)

        # Redimensionner le widget de tableau en fonction de la taille de la fenêtre
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)


    def update_temperature_label(label, task):
        try:
            voltage = task.read()
            temperature = 20 + (voltage * 4)
            arrondi = "{:.1f}".format(temperature)
            label.config(text="Température mesurée: " + arrondi)
        except nidaqmx.DaqError:
            label.config(text="Erreur de lecture de la température")

        label.after(10000, lambda: update_temperature_label(label, task))


    # Création d'une instance du périphérique d'acquisition de données
    with nidaqmx.Task() as task:
        # Configuration du canal d'entrée analogique
        min_val = 0  # Définition de la valeur minimale de mesure
        max_val = 10  # Définition de la valeur maximale de mesure

        task.ai_channels.add_ai_voltage_chan(
            "Dev1/ai0",
            terminal_config=nidaqmx.constants.TerminalConfiguration.RSE,
            min_val=min_val,
            max_val=max_val,
            units=nidaqmx.constants.VoltageUnits.VOLTS
        )

        # Création de la fenêtre Tkinter
        root = tk.Tk()
        root.title("Graphe Xexp et Yexp = f(Freq)")
        root.config(background="#304562")

        # Changer l'icône de la fenêtre
        root.iconbitmap("Image/uppa.ico")

        # Ajuster la taille de la fenêtre en fonction de l'écran
        adjust_window_size(root)

        # Créer l'étiquette pour la température
        temperature_label = tk.Label(root, text="Température mesurée: ")
        temperature_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        # Lancer la mise à jour de la température
        update_temperature_label(temperature_label, task)

        # Afficher les graphiques
        plot_graphs(root)

        # Afficher le tableau
        display_table(root)

        # Démarrer la boucle principale Tkinter
        root.mainloop()
