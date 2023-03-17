import serial

# Configuration des paramètres de communication RS232
ser = serial.Serial(
    port='COM1',  # Modifier le port de communication en fonction de votre configuration
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# Ouverture de la connexion RS232
ser.isOpen()
print("Connexion établie avec succés avec le détecteur synchrone SRS SR850")

# Envoi de commandes au détecteur synchrone
ser.write(b'FREQ?\r\n')  # Demande de la fréquence de mesure actuelle
response = ser.readline()
print(response.decode('ascii'))  # Affichage de la réponse du détecteur synchrone

# Fermeture de la connexion RS232
ser.close()



