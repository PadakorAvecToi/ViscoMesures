import serial
import time

# Ouverture de la connexion série
ser = serial.Serial('COM1', 9600, timeout=1)

# Configuration de la fréquence de modulation et de référence
ser.write(b'FREQM 1000\r\n') # Configure la fréquence de modulation à 1000 Hz
ser.write(b'FREQREF 10000\r\n') # Configure la fréquence de référence à 10 kHz

# Configuration de la fréquence d'excitation
ser.write(b'EXCITE 500\r\n') # Configure



