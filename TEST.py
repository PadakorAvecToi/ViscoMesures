import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
import serial
import time




def envoyer_commande1(ser, commande):
    ser.write(commande.encode())

def envoyer_commande2(ser, commande):
    ser.write(commande.encode())

def envoyer_commande3(ser, commande):
    ser.write(commande.encode())

def envoyer_commande4(ser, commande):
    ser.write(commande.encode())





def recevoir_reponse(ser):
    monreturn = ser.readlines().decode()
    if monreturn == "\r":  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            print("RC")
    print("monreturn = ")
    print(monreturn)
    return monreturn


############################################

def demander_pas_frequence(ser):
    print("SRAT")
    #time.sleep(5.0)
    envoyer_commande1(ser, "SRAT?\r")
    #time.sleep(5.0)
    return recevoir_reponse(ser)

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
    ser = serial.Serial('COM9', 9600)
    pas_frequence = demander_pas_frequence(ser)
    freq_demarrage = demander_freq_demarrage(ser)
    freq_arret = demander_freq_arret(ser)
    sens_balayage = demander_sens_balayage(ser)
    ser.close()
    return pas_frequence, freq_demarrage, freq_arret, sens_balayage




def sauvegarder_configuration():
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
    root = tk.Tk()
    root.withdraw()
    fichier_config = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("Fichier XML", "*.xml")])
    if fichier_config:
        tree.write(fichier_config)
        print("Configuration sauvegardée avec succès dans le fichier", fichier_config)
    else:
        print("Annulation de la sauvegarde de la configuration")



sauvegarder_configuration()





