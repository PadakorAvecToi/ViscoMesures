

import serial

# Paramètres de communication série
port = 'COM8'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
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



import serial

# Paramètres de communication série
port = 'COM1'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

# Ouvrir la connexion série
ser = serial.Serial(port, baudrate)

# Lire les données envoyées par le détecteur synchrone
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()  # Lire la ligne de données et décoder en str
        print(f"Données reçues : {data}")
    else:
        continue

    # Ajoutez ici le traitement des données reçues selon vos besoins

# Fermer la connexion série (en cas d'interruption de la boucle while)
ser.close()







