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



