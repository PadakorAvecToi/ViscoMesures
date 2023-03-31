import xml.etree.ElementTree as ET

# Création d'un élément racine
root = ET.Element("configurations")

# Ajout d'un élément pour chaque configuration
config1 = ET.SubElement(root, "configuration")
config1.set("nom", "Config 1")

freq_modulation = ET.SubElement(config1, "frequence_modulation")
freq_modulation.text = "1000"

freq_reference = ET.SubElement(config1, "frequence_reference")
freq_reference.text = "5000"

freq_coupure = ET.SubElement(config1, "frequence_coupure")
freq_coupure.text = "2000"

config2 = ET.SubElement(root, "configuration")
config2.set("nom", "Config 2")

freq_modulation = ET.SubElement(config2, "frequence_modulation")
freq_modulation.text = "2000"

freq_reference = ET.SubElement(config2, "frequence_reference")
freq_reference.text = "6000"

freq_coupure = ET.SubElement(config2, "frequence_coupure")
freq_coupure.text = "3000"

# Écriture des configurations dans un fichier XML
tree = ET.ElementTree(root)
tree.write("configurations.xml")

#=========================================================================================================================

import serial.tools.list_ports

# Recherche de tous les ports de communication disponibles
ports = serial.tools.list_ports.comports()

# Vérification de chaque port pour détecter le dispositif RS232
for port in ports:
    try:
        # Création d'une instance de connexion série
        ser = serial.Serial(port.device)
        # Vérification du dispositif connecté
        if ser.isOpen():
            # Si le port est ouvert, affichage du nom du port
            print("Dispositif détecté sur le port :", port.device)
            # Fermeture de la connexion série
            ser.close()
    except:
        pass


#====================================================================================================

import serial

# Configuration des paramètres de communication RS232
ser = serial.Serial(
    port='COM1',  # Modifier le port de communication en fonction de votre configuration
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# Ouverture de la connexion RS232
ser.isOpen()
print("Connexion établie avec succés avec le détecteur synchrone SRS SR850")

# Envoi de commandes au détecteur synchrone
ser.write(b'FREQ?\r\n')  # Demande de la fréquence de mesure actuelle
response = ser.readline()
print(response.decode('ascii'))  # Affichage de la réponse du détecteur synchrone

# Fermeture de la connexion RS232
ser.close()


#====================================================================================================

import serial
import configparser

# Lecture du fichier de configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Tentative d'ouverture de la connexion série
try:
    ser = serial.Serial('COM1', 9600, timeout=1)
except serial.SerialException as e:
    print(f"Erreur de connexion série : {e}")
else:
    # Récupération des configurations précédemment utilisées ou proposées
    freqm = config.getint('config', 'freqm', fallback=1000)
    freqref = config.getint('config', 'freqref', fallback=10000)
    freqcut = config.getint('config', 'freqcut', fallback=500)

    # Configuration de la fréquence de modulation et de référence
    try:
        ser.write(f'FREQM {freqm}\r\n'.encode()) # Configure la fréquence de modulation
        ser.write(f'FREQREF {freqref}\r\n'.encode()) # Configure la fréquence de référence
    except serial.SerialException as e:
        print(f"Erreur d'envoi de commande : {e}")
    else:
        # Lecture de la réponse du détecteur synchrone
        response = ser.readline()
        if b'OK' not in response:
            print(f"Erreur de réception de réponse : {response}")
        
        # Configuration de la fréquence de coupure
        try:
            ser.write(f'FREQCUT {freqcut}\r\n'.encode()) # Configure la fréquence de coupure
        except serial.SerialException as e:
            print(f"Erreur d'envoi de commande : {e}")
        else:
            # Lecture de la réponse du détecteur synchrone
            response = ser.readline()
            if b'OK' not in response:
                print(f"Erreur de réception de réponse : {response}")
        
        # Sauvegarde des configurations utilisées
        config.set('config', 'freqm', str(freqm))
        config.set('config', 'freqref', str(freqref))
        config.set('config', 'freqcut', str(freqcut))
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        
        # Fermeture de la connexion série
        ser.close()







