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



