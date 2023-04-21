import serial
import time




# Paramètres de communication série
port = 'COM8'  # Remplacez par le nom de port série approprié (ex: '/dev/ttyUSB0' sur Linux)
baudrate = 9600  # Vitesse de communication en bauds




# Ouvrir la connexion série
ser = serial.Serial(port, baudrate)




# Envoyer la commande au détecteur synchrone
commande = "*IDN?"  # Commande à envoyer
ser.write(commande.encode())  # Envoyer la commande encodée en bytes




# Attendre la réponse du détecteur synchrone (max 5 secondes)
timeout = 5  # Temps d'attente maximal en secondes
start_time = time.time()  # Instant initial
while (time.time() - start_time) < timeout:
    if ser.in_waiting > 0:
        reponse = ser.readline().decode().strip()  # Lire la réponse et décoder en str
        print(f"Réponse du détecteur synchrone : {reponse}")
        break


if 'reponse' not in locals():
    print("Pas de réponse")




# Fermer la connexion série
ser.close()





