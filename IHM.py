from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import win32com.client
from tkinter import messagebox
import Log
import tkinter as tk
import serial
import time
from main import open_powerpoint
from Essai import fonctionpowerpoint

#====================================================================================================

#fonction permettantr de mettre a jour le fichier log

Log.setup_logger()
Log.log_info('Une action a ete effectuee.')
Log.log_warning('Un probleme peut survenir.')
Log.log_error('Erreur la fonction correspondante ne fonctionne pas.')
Log.log_debug('Ceci est le log de debug.')
Log.log_critical('Erreur critique du systeme.')

# création de la fenêtre
window = Tk()

#====================================================================================================

# création des frames
framelogo = ttk.Frame(window)
framelogo.place(x=-180, y=-50)

frameGraphique1 = ttk.Frame(window)
frameGraphique1.place(x=20, y=80)

frameGraphique2 = ttk.Frame(window)
frameGraphique2.place(x=20, y=160)

frameGraphique3 = ttk.Frame(window)
frameGraphique3.place(x=20, y=240)

frameGraphique4 = ttk.Frame(window)
frameGraphique4.place(x=20, y=320)

frameGraphique5 = ttk.Frame(window)
frameGraphique5.place(x=20, y=400)

frameGraphique6 = ttk.Frame(window)
frameGraphique6.place(x=20, y=480)

frameGraphique7 = ttk.Frame(window)
frameGraphique7.place(x=20, y=560)

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
logo_resize = logo.resize((450, 150), Image.ANTIALIAS)

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

def appel_graphique():
    TEST.plot_graphs

#====================================================================================================

#open_powerpoint
fonctionpowerpoint

#====================================================================================================

# création du bouton pour afficher les graphiques

BUTTON_WIDTH = 25

show_button1 = Button(frameGraphique1, text="Etalonnage", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button1.pack()

show_button2 = Button(frameGraphique2, text="Configuration balayage", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button2.pack()

show_button3 = Button(frameGraphique3, text="Graphe X,Y = f(Freq)", command=appel_graphique, bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button3.pack()

show_button4 = Button(frameGraphique4, text="Graphe Xexp et Yexp = f(Freq)", command=appel_graphique, bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button4.pack()

show_button5 = Button(frameGraphique5, text="Delta0 par vide", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button5.pack()

show_button6 = Button(frameGraphique6, text="Calibration", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button6.pack()

show_button7 = Button(frameGraphique7, text="Visco", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button7.pack()

buttonvisioneuse = Button(frameVision, text="?", command=fonctionpowerpoint, bg="#233448", fg="#B1BD11", font=("Arial", 16))
buttonvisioneuse.pack()

#====================================================================================================

# modifications de la fenêtre
window.title("Banc de Viscosité")
window.geometry("1920x1080")
window.minsize(1080, 720)
window.iconbitmap("Image/uppa.ico")
window.config(background="#304562")

#====================================================================================================

# afficher la fenêtre
window.mainloop()