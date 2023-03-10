import serial

# Configuration de la connexion série
ser = serial.Serial(
    port='COM1', # port COM utilisé par le détecteur synchrone
    baudrate=9600, # vitesse de transmission
    parity=serial.PARITY_NONE, # pas de bit de parité
    stopbits=serial.STOPBITS_ONE, # un bit d'arrêt
    bytesize=serial.EIGHTBITS # huit bits de données
)

# Ouverture de la connexion série
ser.open()

# Vérification que la connexion est ouverte
if ser.is_open:
    print("Connexion RS232 établie avec succès.")

# Envoi de données au détecteur synchrone
ser.write(b'Ma commande\r\n') # envoyer une commande au détecteur synchrone

# Lecture de données provenant du détecteur synchrone
data = ser.readline() # lire une ligne de données provenant du détecteur synchrone
print("Données reçues : ", data)

# Fermeture de la connexion série
ser.close()


