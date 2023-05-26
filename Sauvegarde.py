import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from FilVibrant import reponse
from FilVibrant import nouvelle_tension
from FilVibrant import nouvelle_frequence1
from FilVibrant import nouveau_pas
from FilVibrant import nouvelle_frequence2
from FilVibrant import nouveau_sens

def sauvegarder_configuration():
    # Créer l'élément racine du fichier XML
    root = ET.Element("configuration")


    # Récupérer les valeurs de configuration définies précédemment
    frequence_demarrage = nouvelle_frequence1  # Exemple de valeur pré-définie
    frequence_arret = nouvelle_frequence2  # Exemple de valeur pré-définie
    pas_frequence = nouveau_pas  # Exemple de valeur pré-définie
    sens_balayage = nouveau_sens  # Exemple de valeur pré-définie


    # Créer les éléments correspondant aux paramètres de configuration
    freq_demarrage_elem = ET.SubElement(root, "frequence_demarrage")
    freq_demarrage_elem.text = frequence_demarrage


    freq_arret_elem = ET.SubElement(root, "frequence_arret")
    freq_arret_elem.text = frequence_arret


    pas_freq_elem = ET.SubElement(root, "pas_frequence")
    pas_freq_elem.text = pas_frequence


    sens_balayage_elem = ET.SubElement(root, "sens_balayage")
    sens_balayage_elem.text = sens_balayage


    # Créer l'arbre XML
    tree = ET.ElementTree(root)


    # Demander à l'utilisateur de choisir le nom et l'emplacement du fichier
    root = tk.Tk()
    root.withdraw()
    fichier_config = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("Fichier XML", "*.xml")])


    # Enregistrer le fichier XML
    if fichier_config:
        tree.write(fichier_config)
        print("Configuration sauvegardée avec succès dans le fichier", fichier_config)
    else:
        print("Annulation de la sauvegarde de la configuration")




# Appeler la fonction pour sauvegarder la configuration
sauvegarder_configuration()





