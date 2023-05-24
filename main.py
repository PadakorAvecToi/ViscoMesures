import win32com.client
from tkinter import messagebox
import Log

def open_powerpoint():
    # Chemin d'accès et nom de fichier PowerPoint
    powerpoint_file = r"C:\\Users\\letra\\Documents\\GitHub\\ViscoMesures\\Fichier\\test.pptx"

    try:
        # Créer une instance de PowerPoint
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")

        # Ouvrir le fichier PowerPoint
        presentation = powerpoint.Presentations.Open(powerpoint_file)

    except Exception as error_powerpoint:
        print(str(error_powerpoint))