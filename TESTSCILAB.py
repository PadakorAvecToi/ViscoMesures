import subprocess
import tkinter as tk
from tkinter import *



def test_command():
    zizi = Tk()
    # Chemin d'accès à l'exécutable Scilab
    scilab_path = "C:\\Program Files\\scilab-5.5.2\\bin"

    # Fonction pour envoyer des commandes à Scilab et récupérer les résultats
    def send_scilab_command(command):
        process = subprocess.Popen([scilab_path, '-nw', '-nb', '-nogui'],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        process.stdin.write(bytes(command + '\n', 'utf-8'))
        process.stdin.flush()
        output = process.stdout.read().decode('utf-8')
        process.stdout.close()
        process.stderr.close()
        return output

    # Fonction pour exécuter une commande Scilab et afficher le résultat
    def execute_scilab_command():
        command = command_entry.get()
        output = send_scilab_command(command)
        result_text.configure(state='normal')
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, output)
        result_text.configure(state='disabled')

    # Création de la fenêtre principale
    
    

    # Création de la zone de texte pour entrer la commande Scilab
    command_label = tk.Label(zizi, text="Commande Scilab :")
    command_label.pack()
    command_entry = tk.Entry(zizi, width=50)
    command_entry.pack()

    # Création du bouton pour exécuter la commande
    execute_button = tk.Button(zizi, text="Exécuter", command=execute_scilab_command)
    execute_button.pack()

    # Création de la zone de texte pour afficher le résultat
    result_label = tk.Label(zizi, text="Résultat :")
    result_label.pack()
    result_text = tk.Text(zizi, width=50, height=10)
    result_text.configure(state='disabled')
    result_text.pack()
    zizi.title("Interface de contrôle Scilab")
    zizi.mainloop()

# Lancement de la boucle principale de l'interface graphique

