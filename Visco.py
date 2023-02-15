from tkinter import *

#création de la fenètre
window = Tk()

#Modifications de la fenètre
window.title("Banc de Viscosité")
window.geometry("1080x720")
window.minsize(1080,720)
window.iconbitmap("uppa.ico")
window.config(background="#304562")

#Création d'une image

width = 2560
height = 966
image = PhotoImage(file="logouppa.png").subsample(5)
canvas = Canvas(window, width=width, height=height, bg='#304562', bd=0, highlightthickness=0)
canvas.create_image(width/60, height/30, image=image)
canvas.pack(anchor='nw')

#Création d'un boutton
Premier_boutton = Button(text="test du boutton", font=("Courrier", 15), fg='#B2BE12', bg='#233448', bd=0, highlightthickness=0)
Premier_boutton.pack()
Premier_boutton.place(x=10, y=100)

#Afficher la fenètre
window.mainloop()