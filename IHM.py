from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Event
from PIL import ImageTk, Image
import subprocess
import threading
import Log
from main import open_powerpoint
from TESTSCILAB import test_command
from mesureTemp import label_temperature
from Grapique import test_graph1
from test_fenetre_XY import graphique_numero2


#====================================================================================================

#fonction permettantr de mettre a jour le fichier log

Log.setup_logger()
Log.log_error('Erreur la fonction correspondante ne fonctionne pas.')


#Fonction pour gérer l'évènement "pression de la touche F11"
def toggle_fullscreen(event: Event):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))

# création de la fenêtre
window = Tk()

#====================================================================================================

# création des frames
framelogo = ttk.Frame(window)
framelogo.place(x=-180, y=-50)

frameButtonEtalonnage = ttk.Frame(window)
frameButtonEtalonnage.place(x=20, y=70)

frameButtonBalayage = ttk.Frame(window)
frameButtonBalayage.place(x=20, y=190)

frameButtonGraphique1 = ttk.Frame(window)
frameButtonGraphique1.place(x=20, y=310)

frameButtonGraphique2 = ttk.Frame(window)
frameButtonGraphique2.place(x=20, y=430)

frameButtonDelta0 = ttk.Frame(window)
frameButtonDelta0.place(x=20, y=550)

frameButtonCalibration = ttk.Frame(window)
frameButtonCalibration.place(x=20, y=670)

frameButtonVisco = ttk.Frame(window)
frameButtonVisco.place(x=20, y=790)

frameVision = ttk.Frame(window)
frameVision.place(x=1650, y=40)



#====================================================================================================

#insertion du logo
logo = Image.open("Image/logouppa.png")
logo_resize = logo.resize((480, 180), Image.ANTIALIAS)

#Création de l'image
imglogo = ImageTk.PhotoImage(logo_resize)

#création du label pour le logo
labellogo = Label(framelogo, image=imglogo, background="#304562")
labellogo.pack()

#====================================================================================================

#Code de détection automatique des ports

#====================================================================================================
           
#Code de l'etalonage   
def execute_test():
    label_temperature()

#====================================================================================================

#Fonction des graphiques

def fonction_graphique1():
    test_graph1()
    
def fonction_graphique2():
    graphique_numero2()
    
#====================================================================================================
def manual():
    open_powerpoint()

#====================================================================================================

# création du bouton

BUTTON_WIDTH = 25
BUTTON_HEIGHT = 3

Button_etalonnage = Button(frameButtonEtalonnage, text="Etalonnage", command=execute_test, bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
Button_etalonnage.pack()


Button_ConfigBalayage = Button(frameButtonBalayage, text="Configuration balayage", command=test_command, bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
Button_ConfigBalayage.pack()

Button_graph1 = Button(frameButtonGraphique1, command=fonction_graphique1, text="Graphe X,Y = f(Freq)", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
Button_graph1.pack()

Button_graph2 = Button(frameButtonGraphique2, text="Graphe Xexp et Yexp = f(Freq)", command=fonction_graphique2, bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
Button_graph2.pack()

Button_delta0 = Button(frameButtonDelta0, text="Delta0 par vide", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
Button_delta0.pack()

Button_Calibration = Button(frameButtonCalibration, text="Calibration", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
Button_Calibration.pack()

Button_Visco = Button(frameButtonVisco, text="Visco", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
Button_Visco.pack()

buttonvisioneuse = Button(frameVision, text="?", command=manual, bg="#233448", fg="#B1BD11", font=("Arial", 16))
buttonvisioneuse.pack()

#====================================================================================================

# modifications de la fenêtre
window.title("Banc de Viscosité")
largeur_ecran = window.winfo_screenwidth()
hauteur_ecran = window.winfo_screenheight()
window.geometry(f"{largeur_ecran}x{hauteur_ecran}")
window.minsize(largeur_ecran, hauteur_ecran)
window.iconbitmap("Image/uppa.ico")
window.config(background="#304562")
window.attributes('-fullscreen', False)
window.bind('<F11>', toggle_fullscreen)

#====================================================================================================

# afficher la fenêtre
window.mainloop()