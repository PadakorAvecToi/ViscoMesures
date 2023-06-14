import xml.etree.ElementTree as ET #manipulation des fichier XML
import tkinter as tk #interface graphique
from tkinter import filedialog #manipulation de l'explorateur de fichier 
import serial #communication série
import time #pauses 




def envoyer_commande1(ser, commande):
    ser.write(commande.encode())
    #fonction qui permet d'envoyer une commande au détecteur synchrone

def envoyer_commande2(ser, commande):
    ser.write(commande.encode())

def envoyer_commande3(ser, commande):
    ser.write(commande.encode())

def envoyer_commande4(ser, commande):
    ser.write(commande.encode())





def recevoir_reponse(ser):
    reponse="" #variable pour stocker la réponse
    while True:
        caractere = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere == "\r":  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            reponse += "RC" #ajouter RC a notre réponse
            print("RC") #on affiche RC à l'écran
            break #instruction pour quitter la boucle
        print(caractere)#on affiche caractére
        reponse += caractere  # Ajouter le caractère à la réponse
    print("reponse = ") #on affiche la réponse compléte
    print(reponse)
    #time.sleep(5.0)
    return reponse


############################################

def demander_pas_frequence(ser):
    print("SRAT") #afficher la commande que l'on envoie
    #time.sleep(5.0)
    envoyer_commande1(ser, "SRAT?\r") #on envoie la commande au détecteur
    #time.sleep(5.0)
    return recevoir_reponse(ser) #on retourne la réponse 

def demander_freq_demarrage(ser):
    print("SLLM")
    envoyer_commande2(ser, "SLLM?\r")
    #time.sleep(5.0)
    return recevoir_reponse(ser)


def demander_freq_arret(ser):
    print("SULM")
    envoyer_commande3(ser, "SULM?\r")
    #time.sleep(5.0)
    return recevoir_reponse(ser)


def demander_sens_balayage(ser):
    print("RSLP")
    envoyer_commande4(ser, "RSLP?\r")
    time.sleep(5.0)
    return recevoir_reponse(ser)


def demander_informations_detecteur():####################################################################################
    ser = serial.Serial('COM9', 9600) #ouvrir la connexipn série
    pas_frequence = demander_pas_frequence(ser) #appelle des fonctions pour récuperer les informations du détecteur 
    freq_demarrage = demander_freq_demarrage(ser)
    freq_arret = demander_freq_arret(ser)
    sens_balayage = demander_sens_balayage(ser)
    ser.close() #fin de la connexion série
    return pas_frequence, freq_demarrage, freq_arret, sens_balayage #on retourne les informations




def sauvegarder_configuration():
    #Cette fonction sauvegarder_configuration appelle la fonction demander_informations_detecteur pour obtenir 
    # les informations du détecteur. Ensuite, elle crée un élément racine "configuration" pour le fichier XML et ajoute des 
    # sous-éléments correspondant aux paramètres de configuration. 


    pas_frequence, freq_demarrage, freq_arret, sens_balayage = demander_informations_detecteur()
    root = ET.Element("configuration")
    pas_freq_elem = ET.SubElement(root, "pas_frequence")
    pas_freq_elem.text = pas_frequence
    freq_demarrage_elem = ET.SubElement(root, "frequence_demarrage")
    freq_demarrage_elem.text = freq_demarrage
    freq_arret_elem = ET.SubElement(root, "frequence_arret")
    freq_arret_elem.text = freq_arret
    sens_balayage_elem = ET.SubElement(root, "sens_balayage")
    sens_balayage_elem.text = sens_balayage
    tree = ET.ElementTree(root)
    #Ensuite, elle crée un objet ElementTree à partir de l'élément racine et demande à l'utilisateur de choisir le nom 
    # et l'emplacement du fichier XML de sauvegarde. Si un fichier est sélectionné, la configuration est écrite dans le 
    # fichier XML et un message de succès est affiché. Sinon, un message d'annulation est affiché.
    root = tk.Tk() #root = tk.Tk(): Cette ligne crée une instance de la classe Tk dans la variable root, qui représente la fenêtre 
    #principale de l'application.
    root.withdraw() #Cette ligne masque la fenêtre principale, ce qui signifie qu'elle ne sera pas affichée à l'écran
    fichier_config = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("Fichier XML", "*.xml")])
    #Cette ligne affiche une boîte de dialogue de sauvegarde de fichier. L'argument defaultextension=".
    # xml" spécifie que si l'utilisateur ne fournit pas d'extension de fichier, l'extension .xml sera automatiquement ajoutée.
    if fichier_config: #Cette condition vérifie si l'utilisateur a sélectionné un emplacement et un nom de fichier 
        #valide dans la boîte de dialogue.
        tree.write(fichier_config) #Si un fichier valide a été sélectionné, cette ligne enregistre l'arbre XML (tree) dans le fichier 
        #spécifié par fichier_config.

        print("Configuration sauvegardée avec succès dans le fichier", fichier_config)
    else:
        print("Annulation de la sauvegarde de la configuration")



sauvegarder_configuration() #appelle de la fonction pour sauvegarder la configuration du détecteur 










'''
from asyncore import read
import xml.etree.ElementTree as ET


def enregistrer_mesures_xml(mesures, fichier):
    # Créer l'élément racine du fichier XML
    root = ET.Element("mesures")

    # Parcourir les mesures et les ajouter en tant qu'éléments dans le fichier XML
    for mesure in mesures:
        mesure_element = ET.SubElement(root, "mesure")
        ET.SubElement(mesure_element, "valeur").text = str(mesure)

    # Créer un objet ElementTree à partir de l'élément racine
    tree = ET.ElementTree(root)

    # Enregistrer le fichier XML
    tree.write(fichier)


def enregistrer_mesures_txt(mesures, fichier):
    # Ouvrir le fichier en mode écriture
    with open(fichier, "w") as f:
        # Écrire les mesures dans le fichier, une mesure par ligne
        for mesure in mesures:
            f.write(str(mesure) + "\n")


# Exemple d'utilisation
with open('Fichier/releve.txt', 'r') as f:
            data = f.read().splitlines()
mesures = data[1:]

fichier_xml = "mesures.xml"
fichier_txt = "mesures.txt"

enregistrer_mesures_xml(mesures, fichier_xml)
enregistrer_mesures_txt(mesures, fichier_txt)
'''