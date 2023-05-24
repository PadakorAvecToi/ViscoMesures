
import serial.tools.list_ports

# Recherche de tous les ports disponibles
ports = serial.tools.list_ports.comports()

# Affichage des informations sur les ports COM détectés
for port in ports:
    print(f"Port: {port.device} - Description: {port.serial_number}")




'''
import serial

# Paramètres de communication série
port = 'COM9'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds
bytesize = 8  # Taille des octets
parity = 'N'  # Parité (N=aucune, E=pair, O=impair)
stopbits = 1  # Nombre de bits de stop

try:
    # Ouvrir la connexion série
    ser = serial.Serial(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits)

    # Envoyer la commande au détecteur synchrone
    commande = "*IDN?\r"  # Commande à envoyer sans retour chariot à la fin
    ser.write(commande.encode())  # Envoyer la commande encodée en bytes

    # Lire la réponse du détecteur synchrone
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






'''
