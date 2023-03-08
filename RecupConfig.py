import serial
import configparser

# Lecture du fichier de configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Tentative d'ouverture de la connexion série
try:
    ser = serial.Serial('COM1', 9600, timeout=1)
except serial.SerialException as e:
    print(f"Erreur de connexion série : {e}")
else:
    # Récupération des configurations précédemment utilisées ou proposées
    freqm = config.getint('config', 'freqm', fallback=1000)
    freqref = config.getint('config', 'freqref', fallback=10000)
    freqcut = config.getint('config', 'freqcut', fallback=500)

    # Configuration de la fréquence de modulation et de référence
    try:
        ser.write(f'FREQM {freqm}\r\n'.encode()) # Configure la fréquence de modulation
        ser.write(f'FREQREF {freqref}\r\n'.encode()) # Configure la fréquence de référence
    except serial.SerialException as e:
        print(f"Erreur d'envoi de commande : {e}")
    else:
        # Lecture de la réponse du détecteur synchrone
        response = ser.readline()
        if b'OK' not in response:
            print(f"Erreur de réception de réponse : {response}")
        
        # Configuration de la fréquence de coupure
        try:
            ser.write(f'FREQCUT {freqcut}\r\n'.encode()) # Configure la fréquence de coupure
        except serial.SerialException as e:
            print(f"Erreur d'envoi de commande : {e}")
        else:
            # Lecture de la réponse du détecteur synchrone
            response = ser.readline()
            if b'OK' not in response:
                print(f"Erreur de réception de réponse : {response}")
        
        # Sauvegarde des configurations utilisées
        config.set('config', 'freqm', str(freqm))
        config.set('config', 'freqref', str(freqref))
        config.set('config', 'freqcut', str(freqcut))
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        
        # Fermeture de la connexion série
        ser.close()



