import xml.etree.ElementTree as ET #Importe le module xml.etree.ElementTree sous le nom ET pour travailler avec des fichiers XML.
import tkinter as tk #Importe le module tkinter pour créer une interface graphique.
from tkinter import filedialog #Importe la fonction filedialog du module tkinter pour ouvrir une boîte de dialogue de sauvegarde de fichier.
from FilVibrant import reponse   #Importe des fonctions depuis le module FilVibrant. Les fonctions spécifiques importées sont reponse, nouvelle_tension, nouvelle_frequence1, nouveau_pas, nouvelle_frequence2, et nouveau_sens.
from FilVibrant import nouvelle_tension
from FilVibrant import nouvelle_frequence1
from FilVibrant import nouveau_pas
from FilVibrant import nouvelle_frequence2
from FilVibrant import nouveau_sens


def sauvegarder_configuration():
    # Créer l'élément racine du fichier XML
    root = ET.Element("configuration")


    # Récupérer les valeurs de configuration définies précédemment
    frequence_demarrage = nouvelle_frequence1  
    frequence_arret = nouvelle_frequence2  
    pas_frequence = nouveau_pas  
    sens_balayage = nouveau_sens  
    #Affecte les valeurs des variables en utilisant les fonctions importées depuis le module FilVibrant.


    # Créer les éléments correspondant aux paramètres de configuration
    freq_demarrage_elem = ET.SubElement(root, "frequence_demarrage")
    freq_demarrage_elem.text = frequence_demarrage
    #Crée un sous-élément <frequence_demarrage> sous l'élément racine root et lui attribue la valeur de frequence_demarrage.

    freq_arret_elem = ET.SubElement(root, "frequence_arret")
    freq_arret_elem.text = frequence_arret


    pas_freq_elem = ET.SubElement(root, "pas_frequence")
    pas_freq_elem.text = pas_frequence


    sens_balayage_elem = ET.SubElement(root, "sens_balayage")
    sens_balayage_elem.text = sens_balayage


    # Créer l'arbre XML ,Crée un objet ElementTree à partir de l'élément racine root.
    tree = ET.ElementTree(root)


    # Demander à l'utilisateur de choisir le nom et l'emplacement du fichier
    root = tk.Tk()
    root.withdraw()
    fichier_config = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("Fichier XML", "*.xml")])


    # Enregistrer le fichier XML , Crée une fenêtre Tkinter et la masque pour l'utilisateur.
    #Ouvre une boîte de dialogue pour enregistrer le fichier, avec une extension .xml par défaut et en limitant
    # les types de fichiers à des fichiers XML.



    if fichier_config:
        tree.write(fichier_config)
        print("Configuration sauvegardée avec succès dans le fichier", fichier_config)
    else:
        print("Annulation de la sauvegarde de la configuration")




# Appeler la fonction pour sauvegarder la configuration
sauvegarder_configuration()





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

import serial
import time
import xml.etree.ElementTree