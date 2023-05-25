import serial.tools.list_ports
import serial

# Paramètres de l'appareil détecté
reponse_attendue = "Stanford_Research_Systems,SR850,s/n27818,ver1.09"

# Recherche des ports série disponibles
ports_disponibles = list(serial.tools.list_ports.comports())

# Recherche du port COM de l'appareil
port_appareil = None
for port in ports_disponibles:
    try:
        # Tentative d'ouverture du port COM
        ser = serial.Serial(port.device)
        ser.write(b'*IDN?\n')
        reponse = ser.readline().strip().decode()

        if reponse == reponse_attendue:
            port_appareil = port.device
            break

        ser.close()  # Fermeture du port COM
    except serial.SerialException:
        pass

# Vérification de la présence de l'appareil
if port_appareil is None:
    print("Appareil introuvable.")
    exit()

# Affichage du port sur lequel l'appareil est connecté
print(f"L'appareil SR850 est connecté sur le port COM {port_appareil}")

# Paramètres de communication série
port = port_appareil  # Port COM de l'appareil
baudrate = 9600  # Vitesse de communication en bauds

try:
    # Ouvrir la connexion série avec l'appareil
    ser = serial.Serial(port, baudrate)

    # Envoyer la commande au détecteur synchrone
    commande = "*IDN?\r"  # Commande à envoyer sans retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes

    # Lire la réponse de l'appareil
    reponse = ""
    while True:
        caractere = ser.read().decode()
        if caractere == "\r":
            break
        reponse += caractere

    if reponse:
        print(f"Réponse de l'appareil : {reponse}")
    else:
        print("Aucune réponse de l'appareil")

except serial.SerialException as e:
    print(f"Erreur de communication série : {e}")

finally:
    # Fermer la connexion série
    if 'ser' in locals():
        ser.close()



