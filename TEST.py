import serial
import time


# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom du port série approprié (par exemple, '/dev/ttyUSB0' sous Linux)
baudrate = 9600  # Vitesse de communication en bauds





try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)


    # Récupérer l'harmonique de détection actuel du détecteur synchrone
    commande = "SLEN?\r"  # Commande pour récupérer la longeur de balayage avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre


    reponse14 = ""
    while True:
        caractere14 = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere14 == "\r":  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            break
        reponse14 += caractere14  # Ajouter le caractère à la réponse


    if reponse14:
        print(f"Longeur de balayage du détecteur synchrone : {reponse14}")
    else:
        print("Aucune réponse du détecteur synchrone")


    # Modifier l'harmonique de détection du détecteur synchrone
    nouvelle_longeur = 12  # Remplacez par la longeur de balayage en secondesouhaité 
    commande = f"SLEN {nouvelle_longeur:.9f}\r"  # Commande pour modifier la longeur de balayage en seconde avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre


    reponse15 = ""
    while True:
        caractere15 = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere15 == "\r":  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            break
        reponse15 += caractere15  # Ajouter le caractère à la réponse


    if reponse15:
        print(f"Nouvelle longeur de balayage du détecteur synchrone : {nouvelle_longeur}")
    else:
        print("Aucune réponse du détecteur synchrone")


except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")


finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()

