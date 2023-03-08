import serial

# Ouverture de la connexion série
ser = serial.Serial('COM1', 9600, timeout=1)

# Envoi des commandes de configuration
ser.write(b'FREQM 1000\r\n') # Configure la fréquence de modulation à 1000 Hz
ser.write(b'FREQREF 10000\r\n') # Configure la fréquence de référence à 10 kHz
ser.write(b'FREQCUT 2000\r\n') # Configure la fréquence de coupure à 2 kHz

# Lecture de la réponse du détecteur synchrone
response = ser.readline()
print(response)

# Fermeture de la connexion série
ser.close()




