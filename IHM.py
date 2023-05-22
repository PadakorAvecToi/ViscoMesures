from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import win32com.client
from tkinter import messagebox
import Log

#fonction permettantr de mettre a jour le fichier log

Log.setup_logger()

Log.log_info('Une action a ete effectuee.')
Log.log_warning('Un probleme peut survenir.')
Log.log_error('Erreur la fonction correspondante ne fonctionne pas.')
Log.log_debug('Ceci est le log de debug.')
Log.log_critical('Erreur critique du systeme.')

# création de la fenêtre
window = Tk()

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
#Fonction d'étalonage

def etalonage():
    
    try:
        
        encadre = tk.LabelFrame(window, text="Encadré")
#====================================================================================================

#Code d'affichege des graphs

def plot_graphs():
    
    try:

        # Ouvrez le fichier TXT contenant les données
        with open('Fichier/ametek air 480.945 etuve 20°.1C fil 0.1mm 0.06V dans cellule.txt', 'r') as f:
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
            y.append(float(split_line[3]))
            w.append(float(split_line[1]))
            z.append(float(split_line[4]))


        # Créez une figure avec deux sous-graphiques
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

        # Tracez les données dans les sous-graphiques correspondants
        ax1.plot(x, y, color='blue', linewidth=2)
        ax2.plot(w, z, color='red', linewidth=2)

        # Ajoutez des étiquettes pour les axes X et Y et un titre pour chaque sous-graphique
        ax1.set_xlabel("Axe X", fontsize=12)
        ax1.set_ylabel("Axe Y", fontsize=12)
        ax1.set_title("Graphique Réel", fontsize=14)
        ax2.set_xlabel("Axe X", fontsize=12)
        ax2.set_ylabel("Axe Y", fontsize=12)
        ax2.set_title("Graphique Imaginaire", fontsize=14)

        # Ajouter une grille aux sous-graphiques
        ax1.grid(True)
        ax2.grid(True)

        # Modifier l'apparence de la grille
        ax1.grid(color='gray', linestyle='-', linewidth=0.7)
        ax2.grid(color='gray', linestyle='-', linewidth=0.7),

        # Ajouter une légende aux sous-graphiques
        ax1.legend(['Données réelles'], loc='upper right', fontsize=12)
        ax2.legend(['Données imaginaires'], loc='upper right', fontsize=12)

        # Modifier la couleur de fond de la figure
        fig.patch.set_facecolor('#233448')

        # Modifier les marges autour des sous-graphiques
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, wspace=0.4, hspace=0.4)


        # Modifier la taille de la fenêtre
        fig.set_size_inches(10, 6)



        # Modifier l'icône de la fenêtre
        #img = plt.imread('logouppa.png')
        #plt.imshow(img)
        #plt.axis('off')
        #fig.canvas.manager.set_window_icon(img)

        # Modifier le nom de la fenêtre
        #fig.canvas.set_window_title('Banc de viscosité')

        # Modifier la couleur de la police affichée sur la fenêtre
        plt.rcParams['text.color'] = 'Yellow'

        # Afficher la fenêtre avec les deux graphiques
        plt.show()
        
    except Exception as error_plot_graph:
        Log.log_error(f"Erreur dans plot_graphs: {str(error_plot_graph)}", log_condition=True)
        # Affichez éventuellement un message d'erreur à l'utilisateur

#====================================================================================================

def open_powerpoint():
    # Chemin d'accès et nom de fichier PowerPoint
    powerpoint_file = r"C:\\Users\\letra\\Documents\\GitHub\\ViscoMesures\\Fichier\\test.pptx"

    try:
        # Créer une instance de PowerPoint
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")

        # Ouvrir le fichier PowerPoint
        presentation = powerpoint.Presentations.Open(powerpoint_file)

    except Exception as error_powerpoint:
        # Si une erreur se produit, afficher un message d'erreur
        Log.log_error(f"Erreur dans open_powerpoint: {str(error_powerpoint)}", log_condition=True)
        messagebox.showerror("Erreur", "Impossible d'ouvrir le fichier PowerPoint.")

#====================================================================================================

# création du bouton pour afficher les graphiques

BUTTON_WIDTH = 25

show_button1 = Button(frameGraphique1, text="Etalonnage", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button1.pack()

show_button2 = Button(frameGraphique2, text="Configuration balayage", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button2.pack()

show_button3 = Button(frameGraphique3, text="Graphe X,Y = f(Freq)", command=plot_graphs, bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button3.pack()

show_button4 = Button(frameGraphique4, text="Graphe Xexp et Yexp = f(Freq)", command=plot_graphs, bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button4.pack()

show_button5 = Button(frameGraphique5, text="Delta0 par vide", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button5.pack()

show_button6 = Button(frameGraphique6, text="Calibration", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button6.pack()

show_button7 = Button(frameGraphique7, text="Visco", bg="#233448", fg="#B1BD11", font=("Arial", 14), width=BUTTON_WIDTH)
show_button7.pack()

buttonvisioneuse = Button(frameVision, text="?", command=open_powerpoint, bg="#233448", fg="#B1BD11", font=("Arial", 16))
buttonvisioneuse.pack()


# modifications de la fenêtre
window.title("Banc de Viscosité")
window.geometry("1920x1080")
window.minsize(1080, 720)
window.iconbitmap("Image/uppa.ico")
window.config(background="#304562")


# afficher la fenêtre
window.mainloop()
