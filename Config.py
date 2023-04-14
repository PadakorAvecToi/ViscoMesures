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
        # Récupération des informations sur le port
        port_info = port.__dict__
        # Affichage des informations du port détecté
        print("Port: {}\nFabricant: {}\nDescription: {}\nNuméro de série: {}\n".format(port_info['device'], port_info['manufacturer'], port_info['description'], port_info.get('serial_number', 'N/A')))
    except:
        pass





#====================================================================================================


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





#====================================================================================================
import serial
import time

# Définir les paramètres de communication RS232
ser = serial.Serial('COM1', 9600, timeout=1)

# Attendre 2 secondes pour que le détecteur synchrone SRS SR850 démarre
time.sleep(2)

# Choisir la fréquence de référence (par exemple, 10 kHz)
freq_ref = 'FRQREF 10.000E3\n'

# Envoyer la commande RS232 pour choisir la fréquence de référence
ser.write(freq_ref.encode())

# Attendre 500 ms pour que le détecteur synchrone SRS SR850 prenne en compte la nouvelle fréquence de référence
time.sleep(0.5)

# Vérifier que la fréquence de référence a été mise à jour
ser.write(b'FRQREF?\n')
response = ser.readline().decode().strip()
print(f'La fréquence de référence actuelle est {response}')

# Fermer la connexion RS232
ser.close()


#====================================================================================================
import serial
import time

# Définir les paramètres de communication RS232
ser = serial.Serial('COM1', 9600, timeout=1)

# Attendre 2 secondes pour que le détecteur synchrone SRS SR850 démarre
time.sleep(2)

# Choisir la tension d'excitation (par exemple, 1 V)
v_exc = 'AUXV1 1\n'

# Envoyer la commande RS232 pour choisir la tension d'excitation
ser.write(v_exc.encode())

# Attendre 500 ms pour que le détecteur synchrone SRS SR850 prenne en compte la nouvelle tension d'excitation
time.sleep(0.5)

# Vérifier que la tension d'excitation a été mise à jour
ser.write(b'AUXV1?\n')
response = ser.readline().decode().strip()
print(f'La tension d excitation actuelle est {response} V')

# Fermer la connexion RS232
ser.close()





#====================================================================================================
import serial
import time

# Définir les paramètres de communication RS232
ser = serial.Serial('COM1', 9600, timeout=1)

# Attendre 2 secondes pour que le détecteur synchrone SRS SR850 démarre
time.sleep(2)

# Choisir le pas de fréquence (par exemple, 10 Hz)
freq_step = 'FSTEP 10\n'

# Envoyer la commande RS232 pour choisir le pas de fréquence
ser.write(freq_step.encode())

# Attendre 500 ms pour que le détecteur synchrone SRS SR850 prenne en compte le nouveau pas de fréquence
time.sleep(0.5)

# Vérifier que le pas de fréquence a été mis à jour
ser.write(b'FSTEP?\n')
response = ser.readline().decode().strip()
print(f'Le pas de fréquence actuel est de {response} Hz')

# Fermer la connexion RS232
ser.close()





