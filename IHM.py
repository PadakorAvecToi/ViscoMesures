from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Event
from PIL import ImageTk, Image
import subprocess
import Log
from main import open_powerpoint
from mesureTemp import mesure_de_temperature



#====================================================================================================

#fonction permettantr de mettre a jour le fichier log

Log.setup_logger()
Log.log_info('Une action a ete effectuee.')
Log.log_warning('Un probleme peut survenir.')
Log.log_error('Erreur la fonction correspondante ne fonctionne pas.')
Log.log_debug('Ceci est le log de debug.')
Log.log_critical('Erreur critique du systeme.')

#Fonction pour gérer l'évènement "pression de la touche F11"
def toggle_fullscreen(event: Event):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))

# création de la fenêtre
window = Tk()

#====================================================================================================

# création des frames
framelogo = ttk.Frame(window)
framelogo.place(x=-180, y=-50)

frameGraphique1 = ttk.Frame(window)
frameGraphique1.place(x=20, y=70)

frameGraphique2 = ttk.Frame(window)
frameGraphique2.place(x=20, y=190)

frameGraphique3 = ttk.Frame(window)
frameGraphique3.place(x=20, y=310)

frameGraphique4 = ttk.Frame(window)
frameGraphique4.place(x=20, y=430)

frameGraphique5 = ttk.Frame(window)
frameGraphique5.place(x=20, y=550)

frameGraphique6 = ttk.Frame(window)
frameGraphique6.place(x=20, y=670)

frameGraphique7 = ttk.Frame(window)
frameGraphique7.place(x=20, y=790)

framePlacement1 = ttk.Frame(window)
framePlacement1.place(x=500, y=100)

framePlacement2 = ttk.Frame(window)
framePlacement2.place(x=1000, y=100)

frameVision = ttk.Frame(window)
frameVision.place(x=1650, y=40)

#framecalibration =
#encadre_label =

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

#====================================================================================================

#Fonction  des graphiques et de la température

#====================================================================================================

open_powerpoint

#====================================================================================================

# création du bouton

BUTTON_WIDTH = 25
BUTTON_HEIGHT = 3

show_button1 = Button(frameGraphique1, text="Etalonnage", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
show_button1.pack()


show_button2 = Button(frameGraphique2, text="Configuration balayage", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
show_button2.pack()

show_button3 = Button(frameGraphique3, text="Graphe X,Y = f(Freq)", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
show_button3.pack()

show_button4 = Button(frameGraphique4, text="Graphe Xexp et Yexp = f(Freq)", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
show_button4.pack()

show_button5 = Button(frameGraphique5, text="Delta0 par vide", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
show_button5.pack()

show_button6 = Button(frameGraphique6, text="Calibration", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
show_button6.pack()

show_button7 = Button(frameGraphique7, text="Visco", bg="#233448", fg="#B1BD11", font=("Arial", 16), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
show_button7.pack()

buttonvisioneuse = Button(frameVision, text="?", command=open_powerpoint, bg="#233448", fg="#B1BD11", font=("Arial", 16))
buttonvisioneuse.pack()

#====================================================================================================

# modifications de la fenêtre
window.title("Banc de Viscosité")
window.geometry("1920x1080")
window.minsize(1080, 720)
window.iconbitmap("Image/uppa.ico")
window.config(background="#304562")
window.attributes('-fullscreen', True)
window.bind('<F11>', toggle_fullscreen)

#====================================================================================================

# afficher la fenêtre
window.mainloop()