def open_powerpoint():
    # Chemin d'accès et nom de fichier PowerPoint
    powerpoint_file = r"Fichier/test.pptx"

    # Créer une instance de PowerPoint
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")

    try:
        # Ouvrir le fichier PowerPoint
        presentation = powerpoint.Presentations.Open(powerpoint_file)

        # Afficher la présentation en mode diaporama
        presentation.SlideShowSettings.Run()
    except:
        # Si une erreur se produit, afficher un message d'erreur
        messagebox.showerror("Erreur", "Impossible d'ouvrir le fichier PowerPoint.")