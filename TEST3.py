import serial
import time


# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom du port série approprié (par exemple, '/dev/ttyUSB0' sous Linux)
baudrate = 9600  # Vitesse de communication en bauds
Option_0 =0.0000625
Option_1=0.000125
Option_2 =0.00025
Option_3=0.0005
Option_4 =1.0
Option_5 =2.0
Option_6 =4.0
Option_7 =8.0
Option_8 =16.0
Option_9 =32.0
Option_10 =64.0
Option_11 =128.0
Option_12=256.0
Option_13=512.0




try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)


    # Récupérer le pas de fréquence actuel du détecteur synchrone
    commande = "SRAT?\r"  # Commande pour récupérer le pas de fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre


    reponse8 = ""
    while True:
        caractere8 = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere8 == "\r":  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            break
        reponse8 += caractere8  # Ajouter le caractère à la réponse


    if reponse8:
        print(f"Pas de fréquence actuel du détecteur synchrone : {reponse8}")
    else:
        print("Aucune réponse du détecteur synchrone")


    # Modifier le pas de fréquence du détecteur synchrone
    nouveau_pas = 3  # Remplacez par le pas de fréquence souhaité (nombre flottant)
    commande = f"SRAT {nouveau_pas:.9f}\r"  # Commande pour modifier le pas de fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre



    # Récupérer le pas de fréquence actuel du détecteur synchrone
    commande = "SRAT?\r"  # Commande pour récupérer le pas de fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse9 = ""
    while True:
        caractere9 = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere9 == '\r':  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            break
        reponse9 += caractere9  # Ajouter le caractère à la réponse
        
        
        
        
        
    


    if reponse9:
        print(f"Nouveau pas de fréquence du détecteur synchrone : {reponse9}")
    else:
        print("Aucune réponse du détecteur synchrone")


except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")


finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()
