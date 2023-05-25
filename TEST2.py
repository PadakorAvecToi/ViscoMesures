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
with open('Fichier/ametek air 480.945 etuve 20°.1C fil 0.1mm 0.06V dans cellule.txt', 'r') as f:
            data = f.read().splitlines()
mesures = data[1:]

fichier_xml = "mesures.xml"
fichier_txt = "mesures.txt"

enregistrer_mesures_xml(mesures, fichier_xml)
enregistrer_mesures_txt(mesures, fichier_txt)

