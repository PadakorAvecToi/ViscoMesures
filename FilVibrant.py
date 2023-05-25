
import serial
import time

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer la fréquence actuelle du détecteur synchrone
    commande = "FREQ?\r"  # Commande pour récupérer la fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Fréquence actuelle du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_frequence = 2000  # Remplacez par la fréquence souhaitée
    commande = f"FREQ {nouvelle_frequence}\r"  # Commande pour modifier la fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Réponse du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()


import serial

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer la tension d'excitation actuelle du détecteur synchrone
    commande = "SLVL?\r"  # Commande pour récupérer la tension d'excitation avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes

    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Tension d'excitation actuelle du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la tension d'excitation du détecteur synchrone
    nouvelle_tension = 2.5  # Remplacez par la valeur de tension souhaitée
    commande = f"SLVL {nouvelle_tension:.2f}\r"  # Commande pour modifier la tension d'excitation avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes

    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Réponse du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Récupérer la nouvelle tension d'excitation du détecteur synchrone
    commande = "SLVL?\r"  # Commande pour récupérer la tension d'excitation avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes

    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Nouvelle tension d'excitation du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()

import serial
import time

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer la fréquence actuelle du détecteur synchrone
    commande = "SLLM?\r"  # Commande pour récupérer la fréquence de demarrage avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Fréquence actuelle du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_frequence = 2000  # Remplacez par la fréquence souhaitée
    commande = f"SLLM {nouvelle_frequence}\r"  # Commande pour modifier la fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Réponse du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()

import serial
import time

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer la fréquence actuelle du détecteur synchrone
    commande = "SULM?\r"  # Commande pour récupérer la fréquence de demarrage avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Fréquence actuelle du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_frequence = 2000  # Remplacez par la fréquence souhaitée
    commande = f"SULM {nouvelle_frequence}\r"  # Commande pour modifier la fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Réponse du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()
        

import serial
import time

# Paramètres de communication série
port = 'COM4'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer le pas de fréquence actuel du détecteur synchrone
    commande = "SRAT?\r"  # Commande pour récupérer le pas de fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Pas de fréquence actuel du détecteur synchrone : {reponse}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier le pas de fréquence du détecteur synchrone
    nouveau_pas = 0.01  # Remplacez par le pas de fréquence souhaité (nombre flottant)
    commande = f"SRAT {nouveau_pas:.2f}\r"  # Commande pour modifier le pas de fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Nouveau pas de fréquence du détecteur synchrone : {nouveau_pas}")
    else:
        print("Aucune réponse du détecteur synchrone")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()




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



     




