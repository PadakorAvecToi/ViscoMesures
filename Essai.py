import tkinter as tk
import threading

def fonction1():
    # Code pour la première fonction
    fenetre1 = tk.Toplevel()
    fenetre1.title("Fenêtre 1")
    # ... Autres configurations et widgets pour la fenêtre 1 ...

def fonction2():
    # Code pour la deuxième fonction
    fenetre2 = tk.Toplevel()
    fenetre2.title("Fenêtre 2")
    # ... Autres configurations et widgets pour la fenêtre 2 ...

def lancer_fonctions():
    # Création des threads pour lancer les fonctions simultanément
    thread1 = threading.Thread(target=fonction1)
    thread2 = threading.Thread(target=fonction2)

    # Lancement des threads
    thread1.start()
    thread2.start()

# Création de la fenêtre principale
fenetre_principale = tk.Tk()

# Création du bouton pour lancer les fonctions
bouton = tk.Button(fenetre_principale, text="Lancer les fonctions", command=lancer_fonctions)
bouton.pack()

# Lancement de la boucle principale de l'interface graphique
fenetre_principale.mainloop()
