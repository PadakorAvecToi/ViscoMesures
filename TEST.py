import serial.tools.list_ports

# Recherche de tous les ports disponibles
ports = serial.tools.list_ports.comports()

# Affichage des informations sur les ports COM détectés
for port in ports:
    print(f"Port: {port.device} - Description: {port.description}")