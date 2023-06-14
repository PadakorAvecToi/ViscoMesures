import nidaqmx
import nidaqmx.constants
import time
import tkinter as tk

def label_temperature():
    def update_temperature_label():
        voltage = task.read()
        temperature = 20 + (voltage * 4)
        arrondi = "{:.1f}".format(temperature)
        temperature_label.config(text="Température mesurée: " + arrondi)
        root.after(10000, update_temperature_label)  # Update temperature every 10 seconds


    # Création d'une instance du périphérique d'acquisition de données
    with nidaqmx.Task() as task:
        # Configuration du canal d'entrée analogique
        min_val = 0  # Définition de la valeur minimale de mesure
        max_val = 10  # Définition de la valeur maximale de mesure

        task.ai_channels.add_ai_voltage_chan(
            "Dev1/ai0",
            terminal_config=nidaqmx.constants.TerminalConfiguration.RSE,
            min_val=min_val,
            max_val=max_val,
            units=nidaqmx.constants.VoltageUnits.VOLTS
        )

        # Création de la fenêtre tkinter
        root = tk.Tk()
        temperature_label = tk.Label(root, text="Température mesurée: ")
        temperature_label.pack()

        # Lancement de la mise à jour de la température
        update_temperature_label()

        # Démarrage de la boucle principale tkinter
        root.mainloop()