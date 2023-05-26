import serial
import time

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer le sens de balayage actuel du détecteur synchrone
    commande = "RSLP?\r"  # Commande pour récupérer le sens de balayage avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Sens de balayage actuel du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier le sens de balayage du détecteur synchrone
    nouveau_sens = input("Choisissez le sens de balayage (1 pour montant, 2 pour descendant) : ")
    if nouveau_sens == "1":
        commande = "RSLP 1\r"  # Commande pour définir le sens de balayage à montant avec un retour chariot à la fin
    elif nouveau_sens == "2":
        commande = "RSLP 2\r"  # Commande pour définir le sens de balayage à descendant avec un retour chariot à la fin
    else:
        print("Choix invalide.")
        exit()

    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Nouveau sens de balayage du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()