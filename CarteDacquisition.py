#Fonction permettant la connexion et la reconnaisance automatique de mon Port COM
import serial.tools.list_ports #import serial.tools.list_ports: Cette ligne importe le module serial.tools.list_ports qui 
#fournit des outils pour la gestion des ports série.
import time #import time: Cette ligne importe le module time qui fournit des fonctions pour gérer les délais.

ports = serial.tools.list_ports.comports()
#Cette ligne utilise la fonction comports() du module serial.tools.list_ports pour obtenir une liste des ports COM disponibles.
com_list = []
#Cette ligne crée une liste vide com_list pour stocker les noms des ports COM.
for p in ports:
    #Cette ligne commence une boucle for qui itère sur chaque port COM de la liste ports.
    com_list.append(p.device)
    # Cette ligne ajoute le nom du port COM (p.device) à la liste com_list.
    print(p.device)
    #Cette ligne affiche le nom du port COM.
    
# Boucle "do while" executer tant que la condition est vrai 
port_found = False 
#Cette ligne initialise la variable port_found à False, indiquant qu'aucun port n'a été trouvé pour le moment.
while not port_found:
    #Cette ligne commence une boucle while qui se répète tant que port_found est False.
    for com_port in com_list:
        #Cette ligne commence une boucle for qui itère sur chaque nom de port COM de la liste com_list.
        try:
            ser = serial.Serial(com_port, timeout=1)
            #Cette ligne crée une instance de la classe Serial du module serial en utilisant le nom du port COM com_port.
            ser.write(b'*IDN?\r')
            #envoie de la commande IDN
            response = ser.readline().decode().strip()
            #Cette ligne lit la réponse du périphérique connecté en utilisant la méthode readline() de l'instance ser.
            time.sleep(0.2)
            if response:
                print(f"Port COM trouvé : {com_port}")
                #Cette ligne vérifie si une réponse a été reçue du périphérique en vérifiant si response est une chaîne de caractères non vide.
                port_found = True 
                #Cette ligne affecte True à la variable port_found, indiquant que le port a été trouvé.
                break
            ser.close()
        except serial.SerialException:
            pass


