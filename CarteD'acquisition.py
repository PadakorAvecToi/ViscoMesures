import serial.tools.list_ports

# Obtenir la liste des ports série disponibles
ports = serial.tools.list_ports.comports()

# Vérifier s'il y a des ports disponibles
if len(ports) == 0:
    print("Aucun port série disponible.")
else:
    print("Ports série disponibles :")

    # Afficher chaque port disponible
    for port in ports:
        print(f"- {port.device} : {port.description}")








'''

import serial


# Paramètres de communication série
port = 'COM8'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds
bytesize = 8  # Taille des octets
parity = 'N'  # Parité (N=aucune, E=pair, O=impair)
stopbits = 1  # Nombre de bits de stop


# Ouvrir la connexion série
ser = serial.Serial(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits)


# Envoyer la commande au détecteur synchrone
commande = "*IDN?\r"  # Commande à envoyer avec un retour chariot à la fin
ser.write(commande.encode())  # Envoyer la commande encodée en bytes


# Lire la réponse du détecteur synchrone
reponse = ser.readline().decode().strip()  # Lire la réponse et décoder en str
if reponse:
    print(f"Réponse du détecteur synchrone : {reponse}")
else:
    print("Aucune réponse du détecteur synchrone")


# Fermer la connexion série
ser.close()


'''


