import serial

# Paramètres de communication série
port = 'COM8'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

# Ouvrir la connexion série
ser = serial.Serial(port, baudrate)

# Récupérer la fréquence actuelle du détecteur synchrone
commande = "FREQ?\r"  # Commande pour récupérer la fréquence avec un retour chariot à la fin
ser.write(commande.encode())  # Envoyer la commande encodée en bytes
reponse = ser.readline().decode().rstrip()  # Lire la réponse sans conversion en str, en supprimant le retour chariot en fin de ligne
if reponse:
    print(f"Fréquence actuelle du détecteur synchrone : {reponse}")
else:
    print("Aucune réponse du détecteur synchrone")

# Modifier la fréquence du détecteur synchrone
commande = "FREQ 1000\r"  # Commande pour modifier la fréquence avec un retour chariot à la fin
ser.write(commande.encode())  # Envoyer la commande encodée en bytes
reponse = ser.readline().decode().rstrip()  # Lire la réponse sans conversion en str, en supprimant le retour chariot en fin de ligne
if reponse:
    print(f"Réponse du détecteur synchrone : {reponse}")
else:
    print("Aucune réponse du détecteur synchrone")

# Récupérer la nouvelle fréquence du détecteur synchrone
commande = "FREQ?\r"  # Commande pour récupérer la fréquence avec un retour chariot à la fin
ser.write(commande.encode())  # Envoyer la commande encodée en bytes
reponse = ser.readline().decode().rstrip()  # Lire la réponse sans conversion en str, en supprimant le retour chariot en fin de ligne
if reponse:
    print(f"Nouvelle fréquence du détecteur synchrone : {reponse}")
else:
    print("Aucune réponse du détecteur synchrone")

# Fermer la connexion série
ser.close()



