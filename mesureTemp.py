#import nidaqmx
#import time

# Création d'une instance du périphérique d'acquisition de données
#with nidaqmx.Task() as task:
    # Configuration du canal d'entrée analogique
    #task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    
    # Configuration de la mesure de température en utilisant une thermistance
    #task.ai_channels.ai_term_cfg = nidaqmx.constants.TerminalConfiguration.DIFF
    #task.ai_channels.add_ai_thrmcpl_chan(
        #physical_channel="Dev1/ai1" ,
        #name_to_assign_to_channel='',
        #min_val=-10.0, 
        #max_val=80.0, 
        #units=nidaqmx.constants.TemperatureUnits.DEG_F, 
        #thermocouple_type=nidaqmx.constants.ThermocoupleType.J
       # )

    # Lecture de la tension du canal d'entrée
    #voltage = task.read()

    # Conversion de la tension en température
    #temperature = nidaqmx.constants.Thermocouple.convert_volts_to_temperature(voltage, nidaqmx.constants.ThermocoupleType.TYPE_J)

    # Affichage de la température
    #print("Température : {:.2f} °C".format(temperature))


import nidaqmx
import nidaqmx.constants
import time

# Création d'une instance du périphérique d'acquisition de données
with nidaqmx.Task() as task:
    # Configuration du canal d'entrée analogique
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0",
    terminal_config=nidaqmx.constants.TerminalConfiguration(10106) , min_val=-10.0, max_val=10.0, units=nidaqmx.constants.VoltageUnits(10348))
    
    # Lecture de la tension du canal d'entrée

<<<<<<< HEAD
    # Affichage de la tension
    print("Voltage : {:.2f} V".format(voltage))
    print (temperature )

'''

import nidaqmx
import nidaqmx.constants
import math


# Création d'une instance du périphérique d'acquisition de données
with nidaqmx.Task() as task:
    # Configuration du canal d'entrée analogique pour la tension
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    # Lecture de la tension du canal d'entrée
    voltage = task.read()


    # Conversion de la tension en température
    resistance = (5.0 * 10000.0 / voltage) - 10000.0 # Remplacez 10000.0 par la valeur de résistance de la thermistance que vous utilisez
    temperature = 20 + (voltage*12)


    # Affichage de la tension
    print("Voltage : {:.2f} V".format(voltage))
=======
    moyenne = 0
    moy = 0
    for i in range(70):
        voltage = task.read()
        temperature = 20 + (voltage*5)
        moy= moy + voltage
        moyenne = moyenne + temperature
        time.sleep(0.1)
    
    result=moyenne/70
    resultVolt=moy/70
    
>>>>>>> a4854da5638f077df8c0bc84b284e4ba6d35d429
    

    # Affichage de la tension
    print(resultVolt)
    print (result)

