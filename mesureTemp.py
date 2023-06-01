
import nidaqmx
import nidaqmx.constants
import time

# Création d'une instance du périphérique d'acquisition de données
with nidaqmx.Task() as task:
    
    #Configuration du canal d'entrée analogique
    
    min = 0 #definition de 
    max = 10 #la plage de mesure
    
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0", 
    terminal_config=nidaqmx.constants.TerminalConfiguration.RSE,
    min_val=min,
    max_val=max,
    units=nidaqmx.constants.VoltageUnits.VOLTS)
    

    def mesurer_temp():
        voltage = 0
        voltage = task.read()
        temperature = 20 + (voltage*4)
        arrondi = "{:.1f}".format(temperature)
        return arrondi
    
    while True:
        temp = mesurer_temp()
        print("Température mesurée :", temp)
        time.sleep(10)  # Pause de 10 secondes entre les mesures
