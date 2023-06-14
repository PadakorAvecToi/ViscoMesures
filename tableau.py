import tkinter as tk


def display_table():
    # Ouvrir le fichier texte contenant les valeurs
    with open('Fichier/releve.txt', 'r') as file:
        lines = file.readlines()

    # Créer une fenêtre Tkinter
    window = tk.Tk()
    window.title('Tableau de données')

    # Créer un widget de tableau Tkinter
    table = tk.LabelFrame(window, text='Tableau')
    table.pack(padx=10, pady=10)

    # Parcourir les lignes du fichier texte
    for i, line in enumerate(lines):
        # Supprimer les sauts de ligne et diviser la ligne en valeurs individuelles
        values = line.strip().split('\t')

        # Afficher les valeurs dans des étiquettes de texte
        for j, value in enumerate(values):
            label = tk.Label(table, text=value, relief='solid', width=12)
            label.grid(row=i, column=j, padx=5, pady=5)

    # Lancer la boucle principale Tkinter
    window.mainloop()


# Appeler la fonction pour afficher le tableau
display_table()
