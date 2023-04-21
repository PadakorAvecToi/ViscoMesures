import os
import tkinter as tk
from tkinter import filedialog

# Créer la fenêtre principale
root = tk.Tk()

# Définir la fonction pour ouvrir le fichier PowerPoint
def open_powerpoint():
    file_path = "test.pptx"
    os.startfile(file_path)
    
# Créer le bouton
button = tk.Button(root, text="Ouvrir PowerPoint", command=open_powerpoint)
button.pack()

# Lancer la fenêtre principale
root.mainloop()
