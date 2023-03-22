import win32com.client

# Chemin d'accès et nom de fichier PowerPoint
powerpoint_file = r"C:\Users\SN\Desktop\Manuel.pptx"

# Créer une instance de PowerPoint
powerpoint = win32com.client.Dispatch("PowerPoint.Application")

# Ouvrir le fichier PowerPoint
presentation = powerpoint.Presentations.Open(powerpoint_file)

# Afficher la présentation en mode diaporama
presentation.SlideShowSettings.Run()

# Fermer PowerPoint
powerpoint.Quit()
