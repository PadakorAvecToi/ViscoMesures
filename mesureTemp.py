# import nidaqmx
# import time

# #Création d'une instance du périphérique d'acquisition de données
# with nidaqmx.Task() as task:
#     # Configuration du canal d'entrée analogique
#     task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    
#     # Configuration de la mesure de température en utilisant une thermistance
#     task.ai_channels.ai_term_cfg = nidaqmx.constants.TerminalConfiguration.DIFF
#     task.ai_channels.add_ai_thrmcpl_chan(
#         physical_channel="Dev1/ai1" ,
#         name_to_assign_to_channel='',
#         min_val=-0, 
#         max_val=10, 
#         units=nidaqmx.constants.TemperatureUnits.DEG_F, 
#         thermocouple_type=nidaqmx.constants.ThermocoupleType.J)

#     # Lecture de la tension du canal d'entrée
#     voltage = task.read()

#     # Conversion de la tension en température
#     temperature = nidaqmx.constants.Thermocouple.convert_volts_to_temperature(voltage, nidaqmx.constants.ThermocoupleType.TYPE_J)

#     # Affichage de la température
#     print("Température : {:.2f} °C".format(temperature))


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
    
    #Lecture de la tension du canal d'entrée

    moyenne = 0
    moy = 0
    for i in range(50):
        voltage = task.read()
        temperature = 20 + (voltage*4)
        moy= moy + voltage
        moyenne = moyenne + temperature
        time.sleep(0.1)
    
    result=moyenne/50
    resultVolt=moy/50
    
    

    # Affichage de la tension
    print(resultVolt)
    print (result)

