from tkinter import *

#création de la fenètre
window = Tk()

#Modifications de la fenètre
window.title("Banc de Viscosité")
window.geometry("1080x720")
window.minsize(1080,720)
window.iconbitmap("uppa.ico")
window.config(background="#304562")

#Création d'un boutton
Premier_boutton = Button(text="test du boutton", font=("Courrier", 15), fg='#B2BE12', bg='#233448')
Premier_boutton.pack(side=LEFT,)

#Création d'une image



#Afficher la fenètre
window.mainloop()