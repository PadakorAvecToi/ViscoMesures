import os
import tkinter as tk
from tkinter import filedialog

# Créer la fenêtre principale
root = tk.Tk()

# Définir la fonction pour ouvrir le fichier PowerPoint
def open_powerpoint():
    # Ouvre la boîte de dialogue pour sélectionner un fichier PowerPoint
    file_path = filedialog.askopenfilename(title="Sélectionnez un fichier PowerPoint", filetypes=(("PowerPoint files", "*.pptx"), ("all files", "*.*")))
    
    # Vérifie que l'utilisateur a sélectionné un fichier et qu'il existe
    if file_path and os.path.exists(file_path):
        # Vérifie que PowerPoint est installé sur cet ordinateur
        if os.path.isfile("C:/Program Files/Microsoft Office/root/Office16/POWERPNT.exe"):
            # Ouvre le fichier avec PowerPoint
            os.startfile(file_path)
        else:
            # Affiche une erreur si PowerPoint n'est pas installé
            tk.messagebox.showerror("Erreur", "Impossible d'ouvrir PowerPoint, veuillez vérifier que le logiciel est bien installé sur cet ordinateur.")
    else:
        # Affiche une erreur si aucun fichier n'a été sélectionné ou si le fichier n'existe pas
        tk.messagebox.showerror("Erreur", "Impossible de trouver le fichier PowerPoint sélectionné.")

# Créer le bouton
button = tk.Button(root, text="Ouvrir PowerPoint", command=open_powerpoint)
button.pack()

# Lancer la fenêtre principale
root.mainloop()

