
import serial
import time

# Paramètres de communication série
port = 'COM8'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer la fréquence actuelle du détecteur synchrone
    commande = "FREQ?\r"  # Commande pour récupérer la fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse1 = ""
    while True:
        caractere1 = ser.read().decode()
        if caractere1 == "\r":
            break
        reponse1 += caractere1

    if reponse1:
        print(f"Fréquence actuelle du détecteur synchrone : {reponse1}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_frequence = 2000  # Remplacez par la fréquence souhaitée
    commande = f"FREQ {nouvelle_frequence}\r"  # Commande pour modifier la fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse2 = ""
    while True:
        caractere2 = ser.read().decode()
        if caractere2 == "\r":
            break
        reponse2 += caractere2

    if reponse2:
        print(f"Réponse du détecteur synchrone : {reponse2}")
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

    reponse3 = ""
    while True:
        caractere3 = ser.read().decode()
        if caractere3 == "\r":
            break
        reponse3 += caractere3

    if reponse3:
        print(f"Réponse du détecteur synchrone : {reponse3}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Récupérer la nouvelle tension d'excitation du détecteur synchrone
    commande = "SLVL?\r"  # Commande pour récupérer la tension d'excitation avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes

    reponse4 = ""
    while True:
        caractere4 = ser.read().decode()
        if caractere4 == "\r":
            break
        reponse4 += caractere4

    if reponse4:
        print(f"Nouvelle tension d'excitation du détecteur synchrone : {reponse4}")
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
    
    reponse4 = ""
    while True:
        caractere4 = ser.read().decode()
        if caractere4 == "\r":
            break
        reponse4 += caractere4

    if reponse4:
        print(f"Fréquence de démmarage actuelle du détecteur synchrone : {reponse4}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_frequence1 = 2000  # Remplacez par la fréquence souhaitée
    commande = f"SLLM {nouvelle_frequence1}\r"  # Commande pour modifier la fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse5 = ""
    while True:
        caractere5 = ser.read().decode()
        if caractere5 == "\r":
            break
        reponse5 += caractere5

    if reponse5:
        print(f"Réponse du détecteur synchrone : {reponse5}")
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
    
    reponse6 = ""
    while True:
        caractere6 = ser.read().decode()
        if caractere6 == "\r":
            break
        reponse6 += caractere6

    if reponse6:
        print(f"Fréquence actuelle du détecteur synchrone : {reponse6}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_frequence2 = 2000  # Remplacez par la fréquence souhaitée
    commande = f"SULM {nouvelle_frequence2}\r"  # Commande pour modifier la fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse7 = ""
    while True:
        caractere7 = ser.read().decode()
        if caractere7 == "\r":
            break
        reponse7 += caractere7

    if reponse7:
        print(f"Réponse du détecteur synchrone : {reponse7}")
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
    nouveau_pas = Option_4  # Remplacez par le pas de fréquence souhaité (nombre flottant)
    commande = f"SRAT {nouveau_pas:.9f}\r"  # Commande pour modifier le pas de fréquence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre


    reponse9 = ""
    while True:
        caractere9 = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere9 == '\r':  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            break
        reponse9 += caractere9  # Ajouter le caractère à la réponse


    if reponse9:
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

    reponse10 = ""
    while True:
        caractere10 = ser.read().decode()
        if caractere10 == "\r":
            break
        reponse10 += caractere10

    if reponse10:
        print(f"Sens de balayage actuel du détecteur synchrone : {reponse10}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier le sens de balayage du détecteur synchrone
    nouveau_sens = input("Choisissez le sens de balayage (1 pour montant, 2 pour descendant) : ")
    if nouveau_sens == "1":
        commande2 = "RSLP 1\r"  # Commande pour définir le sens de balayage à montant avec un retour chariot à la fin
    elif nouveau_sens == "2":
        commande2 = "RSLP 2\r"  # Commande pour définir le sens de balayage à descendant avec un retour chariot à la fin
    else:
        print("Choix invalide.")
        exit()

    ser.write(commande2.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse11 = ""
    while True:
        caractere11 = ser.read().decode()
        if caractere11 == "\r":
            break
        reponse11 += caractere11

    if reponse11:
        print(f"Nouveau sens de balayage du détecteur synchrone : {reponse11}")
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
port = 'COM9'  # Remplacez par le nom du port série approprié (par exemple, '/dev/ttyUSB0' sous Linux)
baudrate = 9600  # Vitesse de communication en bauds





try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)


    # Récupérer l'harmonique de détection actuel du détecteur synchrone
    commande = "HARM?\r"  # Commande pour récupérer l'harmonique de détection avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre


    reponse12 = ""
    while True:
        caractere12 = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere12 == "\r":  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            break
        reponse12 += caractere12  # Ajouter le caractère à la réponse


    if reponse12:
        print(f"Harmonique de détecteur actuel du détecteur synchrone : {reponse12}")
    else:
        print("Aucune réponse du détecteur synchrone")


    # Modifier l'harmonique de détection du détecteur synchrone
    nouveau_harmondetec = 14  # Remplacez par l'harmonique de détection souhaité (nombre flottant)
    commande = f"HARM {nouveau_harmondetec:.9f}\r"  # Commande pour modifier l'harmonique de détection avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre


    reponse13 = ""
    while True:
        caractere13 = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere13 == "\r":  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            break
        reponse13 += caractere13  # Ajouter le caractère à la réponse


    if reponse13:
        print(f"Nouvelle harmonique de détection du détecteur synchrone : {nouveau_harmondetec}")
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


import serial
import time

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer le le mode de numérisation actuel du détecteur synchrone
    commande = "SEND?\r"  # Commande pour récupérer le mode de numérisation avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse16 = ""
    while True:
        caractere16 = ser.read().decode()
        if caractere16 == "\r":
            break
        reponse16 += caractere16

    if reponse16:
        print(f"Mode de numérisation actuel du détecteur synchrone : {reponse16}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier le sens de balayage du détecteur synchrone
    nouveau_mode = input("Choisissez le sens de balayage (1 pour montant, 2 pour descendant) : ")
    if nouveau_mode == "1":
        commande3 = "RSLP 1\r"  # Commande pour définir le sens de balayage à montant avec un retour chariot à la fin
    elif nouveau_mode == "2":
        commande3 = "RSLP 2\r"  # Commande pour définir le sens de balayage à descendant avec un retour chariot à la fin
    else:
        print("Choix invalide.")
        exit()

    ser.write(commande3.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse17 = ""
    while True:
        caractere17 = ser.read().decode()
        if caractere17 == "\r":
            break
        reponse17 += caractere17

    if reponse17:
        print(f"Nouveau sens de balayage du détecteur synchrone : {reponse17}")
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

    # Récupérer le le mode de numérisation actuel du détecteur synchrone
    commande = "FMOD?\r"  # Commande pour récupérer la source de référence avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse18 = ""
    while True:
        caractere18 = ser.read().decode()
        if caractere18== "\r":
            break
        reponse18 += caractere18

    if reponse18:
        print(f"Mode de numérisation actuel du détecteur synchrone : {reponse18}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la source de référence du détecteur synchrone
    nouveau_sourcerefe = input("Choisissez le sens de balayage (1 pour interne, 2 pour balayage et 3 pour externe) : ")
    if nouveau_sourcerefe == "1":
        commande4 = "RSLP 1\r"  # Commande pour définir la source de référence  à montant avec un retour chariot à la fin
    elif nouveau_sourcerefe == "2":
        commande4 = "RSLP 2\r"  # Commande pour définir la source de référence à descendant avec un retour chariot à la fin
    elif nouveau_sourcerefe == "3":
        commande4 = "RSLP 3\r"  # Commande pour définir la source de référence à descendant avec un retour chariot à la fin
    else:
        print("Choix invalide.")
        exit()

    ser.write(commande4.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre

    reponse19 = ""
    while True:
        caractere19 = ser.read().decode()
        if caractere19 == "\r":
            break
        reponse19 += caractere19

    if reponse19:
        print(f"Nouveau mode de numérisation du détecteur synchrone : {reponse19}")
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
port = 'COM9'  # Remplacez par le nom du port série approprié (par exemple, '/dev/ttyUSB0' sous Linux)
baudrate = 9600  # Vitesse de communication en bauds





try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)


    # Récupérer l'harmonique de détection actuel du détecteur synchrone
    commande = "PHAS?\r"  # Commande pour récupérer le degrés de déphasage avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre


    reponse20 = ""
    while True:
        caractere20 = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere20 == "\r":  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            break
        reponse20 += caractere20  # Ajouter le caractère à la réponse


    if reponse20:
        print(f"Degrés de déphasage du détecteur synchrone : {reponse20}")
    else:
        print("Aucune réponse du détecteur synchrone")


    # Modifier l'harmonique de détection du détecteur synchrone
    nouveau_degrés = 0.000000  # Remplacez par le degrés de déphasage souhaité 
    commande = f"PHAS {nouveau_degrés:.7f}\r"  # Commande pour modifier le degrés de déphasage avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(0.1)  # Attendre un court délai pour permettre au détecteur synchrone de répondre


    reponse21 = ""
    while True:
        caractere21 = ser.read().decode()  # Lire un caractère depuis le port série et le décoder en une chaîne de caractères
        if caractere21 == "\r":  # Si le caractère est un retour chariot ("\r"), sortir de la boucle
            break
        reponse21 += caractere21  # Ajouter le caractère à la réponse


    if reponse21:
        print(f"Nouvelle degrés de déphasage du détecteur synchrone : {nouveau_degrés}")
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
        
        
        
        
        import serial
import time

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer la fréquence actuelle du détecteur synchrone
    commande = "ISRC?\r"  # Commande pour la configuration d'entrée avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse24 = ""
    while True:
        caractere24 = ser.read().decode()
        if caractere24 == "\r":
            break
        reponse24 += caractere24

    if reponse24:
        print(f"Configuration d'entrée actuelle du détecteur synchrone : {reponse24}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_config = 1  # Remplacez par la configuration d'entrée souhaitée
    commande = f"ISRC {nouvelle_config}\r"  # Commande pour modifier la configuration d'entrée avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse25 = ""
    while True:
        caractere25 = ser.read().decode()
        if caractere25 == "\r":
            break
        reponse25 += caractere25

    if reponse25:
        print(f"Réponse du détecteur synchrone : {reponse25}")
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
    commande = "IGND?\r"  # Commande pour récuperer la grille de blindage d'entrée  avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse26= ""
    while True:
        caractere26 = ser.read().decode()
        if caractere26 == "\r":
            break
        reponse26 += caractere26

    if reponse26:
        print(f"Grille de blindage d'entrée actuelle du détecteur synchrone : {reponse26}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_grille = 1  # Remplacez par la la grille de blindage d'entrée d'entrée souhaitée
    commande = f"IGND {nouvelle_grille}\r"  # Commande pour modifier la la grille de blindage d'entrée avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse27 = ""
    while True:
        caractere27 = ser.read().decode()
        if caractere27 == "\r":
            break
        reponse27 += caractere27

    if reponse27:
        print(f"Réponse du détecteur synchrone : {reponse27}")
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
    commande = "ICPL?\r"  # Commande pour récuperer le couplage d'entrée  avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse28= ""
    while True:
        caractere28 = ser.read().decode()
        if caractere28 == "\r":
            break
        reponse28 += caractere28

    if reponse28:
        print(f"Fréquence de démmarage actuelle du détecteur synchrone : {reponse28}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouveau_couplage = 0  # Remplacez par le couplage d'entrée souhaitée
    commande = f"ICPL {nouveau_couplage}\r"  # Commande pour modifier le couplage d'entrée avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse29 = ""
    while True:
        caractere29 = ser.read().decode()
        if caractere29 == "\r":
            break
        reponse29 += caractere29

    if reponse29:
        print(f"Réponse du détecteur synchrone : {reponse29}")
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
    commande = "ILIN?\r"  # Commande pour récuperer les filtres d'encoche de ligne avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse30= ""
    while True:
        caractere30 = ser.read().decode()
        if caractere30 == "\r":
            break
        reponse30 += caractere30

    if reponse30:
        print(f"Filtres d'encoche de ligne actuelle du détecteur synchrone : {reponse30}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouveau_filtre = 2  # Remplacez par les filtres d'encoche de ligne  souhaitée
    commande = f"ILIN {nouveau_filtre}\r"  # Commande pour modifier les filtres d'encoche de ligne  avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse31 = ""
    while True:
        caractere31 = ser.read().decode()
        if caractere31 == "\r":
            break
        reponse31 += caractere31

    if reponse31:
        print(f"Réponse du détecteur synchrone : {reponse31}")
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
    commande = "OFSL?\r"  # Commande pour récuperer les filtres d'encoche de ligne avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse32= ""
    while True:
        caractere32 = ser.read().decode()
        if caractere32 == "\r":
            break
        reponse32 += caractere32

    if reponse32:
        print(f" Pente du filtre passe-bas actuelle du détecteur synchrone : {reponse32}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_pente = 1  # Remplacez par la Pente du filtre passe-bas souhaitée
    commande = f"OFSL {nouvelle_pente}\r"  # Commande pour modifier la Pente du filtre passe-bas avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse33 = ""
    while True:
        caractere33 = ser.read().decode()
        if caractere33 == "\r":
            break
        reponse33 += caractere33

    if reponse33:
        print(f"Réponse du détecteur synchrone : {reponse33}")
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
    commande = "SYNC?\r"  # Commande pour récuperer l'état du filtre synchrone avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse34= ""
    while True:
        caractere34 = ser.read().decode()
        if caractere34 == "\r":
            break
        reponse34 += caractere34

    if reponse34:
        print(f" Etat du filtre synchrone actuelle du détecteur synchrone : {reponse34}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouveau_etatfiltre = 1  # Remplacez par l'état du filtre synchrone souhaitée
    commande = f"SYNC {nouveau_etatfiltre}\r"  # Commande pour modifier l'état du filtre synchrone avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse35 = ""
    while True:
        caractere35 = ser.read().decode()
        if caractere35 == "\r":
            break
        reponse35 += caractere35

    if reponse35:
        print(f"Réponse du détecteur synchrone : {reponse35}")
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
    commande = "OFLT?\r"  # Commande pour récuperer la constante de temps avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse36= ""
    while True:
        caractere36 = ser.read().decode()
        if caractere36 == "\r":
            break
        reponse36 += caractere36

    if reponse36:
        print(f" Etat du filtre synchrone actuelle du détecteur synchrone : {reponse36}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouveau_temps = 8  # Remplacez par la constante de temps souhaitée
    commande = f"OFLT {nouveau_temps}\r"  # Commande pour modifier la constante de temps avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse37 = ""
    while True:
        caractere37 = ser.read().decode()
        if caractere37 == "\r":
            break
        reponse37 += caractere37

    if reponse37:
        print(f"Réponse du détecteur synchrone : {reponse37}")
    else:
        print("Aucune réponse du détecteur synchrone")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()
    
    
    
import serial

# Spécifiez le port COM sur lequel vous souhaitez envoyer la commande
port = "COM9"

# Spécifiez la commande que vous souhaitez envoyer
command = "ARSV"

try:
    ser = serial.Serial(port, timeout=1)
    ser.write(command.encode())
    ser.close()
    print(f"Commande '{command}' envoyée au port {port} avec succès.")
except serial.SerialException as e:
    print(f"Erreur lors de l'envoi de la commande : {e}")
    
    
    
import serial

# Spécifiez le port COM sur lequel vous souhaitez envoyer la commande
port = "COM9"

# Spécifiez la commande que vous souhaitez envoyer
command = "AGAN"

try:
    ser = serial.Serial(port, timeout=1)
    ser.write(command.encode())
    ser.close()
    print(f"Commande '{command}' envoyée au port {port} avec succès.")
except serial.SerialException as e:
    print(f"Erreur lors de l'envoi de la commande : {e}")
   


import serial
import time

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port, baudrate)

    # Récupérer la fréquence actuelle du détecteur synchrone
    commande = "SMOD?\r"  # Commande pour récuperer le format d'écran avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse38= ""
    while True:
        caractere38 = ser.read().decode()
        if caractere38 == "\r":
            break
        reponse38 += caractere38

    if reponse38:
        print(f" Format d'écran actuelle du détecteur synchrone : {reponse38}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_ecran = 1  # Remplacez par le format d'écran souhaitée
    commande = f"SMOD {nouvelle_ecran}\r"  # Commande pour modifier le format d'écran avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse39 = ""
    while True:
        caractere39 = ser.read().decode()
        if caractere39 == "\r":
            break
        reponse39 += caractere39

    if reponse39:
        print(f"Réponse du détecteur synchrone : {reponse39}")
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
    commande = "ADSP?\r"  # Commande pour récuperer  l'affichage actif avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse40= ""
    while True:
        caractere40 = ser.read().decode()
        if caractere40 == "\r":
            break
        reponse40 += caractere40

    if reponse40:
        print(f"  Affichage actif actuelle du détecteur synchrone : {reponse40}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_actif = 1  # Remplacez par  l'affichage actif souhaitée
    commande = f"ADSP {nouvelle_actif}\r"  # Commande pour modifier  l'affichage actif avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse41 = ""
    while True:
        caractere41 = ser.read().decode()
        if caractere41 == "\r":
            break
        reponse41 += caractere41

    if reponse41:
        print(f"Réponse du détecteur synchrone : {reponse41}")
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
    commande = "DTYP?\r"  # Commande pour récuperer le type d'affichage complet avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse42= ""
    while True:
        caractere42 = ser.read().decode()
        if caractere42 == "\r":
            break
        reponse42 += caractere42

    if reponse42:
        print(f"  Affichage actif actuelle du détecteur synchrone : {reponse42}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_affichage = 1  # Remplacez par le type d'affichage complet souhaitée
    commande = f"DTYP {nouvelle_affichage}\r"  # Commande pour modifier le type d'affichage complet avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse43 = ""
    while True:
        caractere43 = ser.read().decode()
        if caractere43 == "\r":
            break
        reponse43 += caractere43

    if reponse43:
        print(f"Réponse du détecteur synchrone : {reponse43}")
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
    commande = "DTRC?\r"  # Commande pour récuperer le type d'affichage complet avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse44= ""
    while True:
        caractere44 = ser.read().decode()
        if caractere44 == "\r":
            break
        reponse44 += caractere44

    if reponse44:
        print(f"  Affichage actif actuelle du détecteur synchrone : {reponse44}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_affichagecomp = 1  # Remplacez par le type d'affichage complet souhaitée
    commande = f"DTYP {nouvelle_affichagecomp}\r"  # Commande pour modifier le type d'affichage complet avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse45 = ""
    while True:
        caractere45 = ser.read().decode()
        if caractere45 == "\r":
            break
        reponse45 += caractere45

    if reponse45:
        print(f"Réponse du détecteur synchrone : {reponse45}")
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
    commande = "DSCL?\r"  # Commande pour récuperer la plage d'affichage complete avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse46= ""
    while True:
        caractere46 = ser.read().decode()
        if caractere46 == "\r":
            break
        reponse46 += caractere46

    if reponse46:
        print(f"  Plage d'affichage actuelle du détecteur synchrone : {reponse46}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_plage = 1  # Remplacez par la plage d'affichage complete souhaitée
    commande = f"DTYP {nouvelle_plage}\r"  # Commande pour modifier la plage d'affichage complete avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse47 = ""
    while True:
        caractere47 = ser.read().decode()
        if caractere47 == "\r":
            break
        reponse47 += caractere47

    if reponse45:
        print(f"Réponse du détecteur synchrone : {reponse47}")
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
    commande = "DOFF?\r"  # Commande pour récuperer la valeur du centre d'affichage complet avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse48= ""
    while True:
        caractere48 = ser.read().decode()
        if caractere48 == "\r":
            break
        reponse48 += caractere48

    if reponse48:
        print(f"valeur du centre d'affichage complet actuelle du détecteur synchrone : {reponse48}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouveau_centre = 1  # Remplacez par la valeur du centre d'affichage complet souhaitée
    commande = f"DOFF {nouveau_centre}\r"  # Commande pour modifier la valeur du centre d'affichage complet avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse49 = ""
    while True:
        caractere49 = ser.read().decode()
        if caractere49 == "\r":
            break
        reponse49 += caractere49

    if reponse45:
        print(f"Réponse du détecteur synchrone : {reponse49}")
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
    commande = "DHZS?\r"  # Commande pour récuperer l'échelle horizontale de l'affichage complet avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse50= ""
    while True:
        caractere50 = ser.read().decode()
        if caractere50 == "\r":
            break
        reponse50 += caractere50

    if reponse50:
        print(f" Echelle horizontale de l'affichage complet actuelle du détecteur synchrone : {reponse50}")
    else:
        print("Aucune réponse du détecteur synchrone")

    # Modifier la fréquence de référence du détecteur synchrone
    nouvelle_horizon = 1  # Remplacez par l'échelle horizontale de l'affichage complet souhaitée
    commande = f"DHZS {nouvelle_horizon}\r"  # Commande pour modifier l'échelle horizontale de l'affichage complet avec un retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes
    time.sleep(3.0)  # Attendre un court délai pour permettre au détecteur synchrone de répondre
    
    reponse51 = ""
    while True:
        caractere51 = ser.read().decode()
        if caractere51 == "\r":
            break
        reponse51 += caractere51

    if reponse51:
        print(f"Réponse du détecteur synchrone : {reponse51}")
    else:
        print("Aucune réponse du détecteur synchrone")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()