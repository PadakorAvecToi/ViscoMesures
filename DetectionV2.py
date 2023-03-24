import serial.tools.list_ports

# Recherche de tous les ports de communication disponibles
ports = serial.tools.list_ports.comports()

# Vérification de chaque port pour détecter le dispositif RS232
for port in ports:
    try:
        # Récupération des informations sur le port
        port_info = port.__dict__
        # Affichage des informations du port détecté
        print("Port: {}\nFabricant: {}\nDescription: {}\nNuméro de série: {}\n".format(port_info['device'], port_info['manufacturer'], port_info['description'], port_info.get('serial_number', 'N/A')))
    except:
        pass



