import serial
import time

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer le le mode de numérisation actuel du détecteur synchrone
    commande = "SWPT?\r"  # Commande pour récupérer le type de balyage interne avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse22 = ""
    while True:
        caractere22 = ser.read().decode()
        if caractere22 == "\r":
            break
        reponse22 += caractere22

    if reponse22:
        print(f"Mode de numérisation actuel du détecteur synchrone : {reponse22}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier le sens de balayage du détecteur synchrone
    nouveau_typebalayage = input("Choisissez le type de balyage interne (0 pour linéaire , 1 pour logarithmique) : ")
    if nouveau_typebalayage == "0":
        commande5 = "SWPT 0\r"  # Commande pour définir le sens de balayage à montant avec un retour chariot à la fin
    elif nouveau_typebalayage == "1":
        commande5 = "SWPT 1\r"  # Commande pour définir le sens de balayage à descendant avec un retour chariot à la fin
    else:
        print("Choix invalide.")
        exit()

    ser.write(commande5.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse23 = ""
    while True:
        caractere23 = ser.read().decode()
        if caractere23 == "\r":
            break
        reponse23 += caractere23

    if reponse23:
        print(f"Nouveau sens de balayage du détecteur synchrone : {reponse23}")
    else:
        print("Aucune réponse du détecteur synchrone")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()