import os
import tkinter as tk
from tkinter import filedialog

# Créer la fenêtre principale
root = tk.Tk()

# Définir la fonction pour ouvrir le fichier PowerPoint
def open_powerpoint():
    # Ouvrir une boîte de dialogue pour sélectionner le fichier
    file_path = filedialog.askopenfilename(defaultextension=".pptx",
                                           filetypes=[("test", "*.pptx")])
    # Vérifier si un fichier a été sélectionné
    if file_path:
        # Ouvrir le fichier PowerPoint
        os.startfile(file_path)

# Créer le bouton
button = tk.Button(root, text="Ouvrir PowerPoint", command=open_powerpoint)
button.pack()

# Lancer la fenêtre principale
root.mainloop()
