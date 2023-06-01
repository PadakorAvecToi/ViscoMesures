import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
com_list = []
for p in ports:
    com_list.append(p.device)
    print(p.device)

# Boucle "do while"
port_found = False
while not port_found:
    for com_port in com_list:
        try:
            ser = serial.Serial(com_port, timeout=1)
            ser.write(b'*IDN?\r')
            response = ser.readline().decode().strip()
            if response:
                print(f"Port COM trouvé : {com_port}")
                
                port_found = True
                break
            ser.close()
        except serial.SerialException:
            pass


