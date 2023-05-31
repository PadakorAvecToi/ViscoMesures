import serial.tools.list_ports
import time


def connect_to_device(device_name):
    # Récupérer la liste des ports série disponibles
    ports = serial.tools.list_ports.comports()


    # Parcourir chaque port
    for port in ports:
        try:
            # Ouvrir la connexion série
            ser = serial.Serial(port.device, baudrate=9600, timeout=1)
            time.sleep(1)  # Attendre un court délai pour permettre au détecteur de s'initialiser


            # Envoyer la commande pour récupérer l'IDN
            ser.write(b"*IDN?\r")
            time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur de répondre


            # Lire la réponse de l'appareil
            response = ser.readline().decode().strip()


            # Fermer la connexion série
            ser.close()


            # Vérifier si la réponse contient le nom de l'appareil recherché
            if device_name in response:
                return port.device  # Retourner le port s'il correspond
        except (OSError, serial.SerialException):
            # Ignorer les erreurs de port série non valides
            pass


    return None  # Retourner None si aucun appareil n'est trouvé


# Utilisation de la fonction pour se connecter automatiquement au détecteur
device_name = "SRS SR850"
com_port = connect_to_device(device_name)


if com_port is not None:
    print(f"Connexion réussie au détecteur {device_name} sur le port {com_port}.")
else:
    print(f"Échec de la connexion au détecteur {device_name}. Veuillez vérifier la connexion et les paramètres.")





