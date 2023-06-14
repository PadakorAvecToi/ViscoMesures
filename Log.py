import logging
import os


def setup_logger():
    log_dir = "Fichier"
    log_file = os.path.join(log_dir, "Fichier_log.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def log_error(message, log_condition=True):
    if log_condition:
        logger = logging.getLogger('my_logger')
        logger.error(message)

        # Vérifier le nombre de lignes dans le fichier de journalisation
        logfile = 'Fichier\\Fichier_log.log'  # Remplacez par le chemin réel de votre fichier de journalisation
        with open(logfile, 'r') as f:
            lines = f.readlines()
            num_lines = len(lines)

        # Vider le fichier de journalisation si le nombre de lignes atteint 500
        if num_lines >= 500:
            with open(logfile, 'w'):
                pass
