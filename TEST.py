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