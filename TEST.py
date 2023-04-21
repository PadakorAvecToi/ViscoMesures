

import serial

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

# Ouvrir la connexion série
ser = serial.Serial(port, baudrate)

# Envoyer la commande au détecteur synchrone
commande = "*IDN?"  # Commande à envoyer
ser.write(commande.encode())  # Envoyer la commande encodée en bytes

# Lire la réponse du détecteur synchrone
reponse = ser.readline().decode().strip()  # Lire la réponse et décoder en str
print(f"Réponse du détecteur synchrone : {reponse}")

# Fermer la connexion série
ser.close()


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









