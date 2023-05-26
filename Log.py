import logging

def setup_logger():
    logging.basicConfig(filename='Fichier_log.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def log_debug(message):
    logging.debug(message)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message, log_condition=True):
    if log_condition:
        logger = logging.getLogger('my_logger')
        logger.error(message)

        # Vérifier le nombre de lignes dans le fichier de journalisation
        logfile = 'C:\\Users\\flore\\Desktop\\Projet VS\\GitHub\\ViscoMesures\\Fichier_log.log'  # Remplacez par le chemin réel de votre fichier de journalisation
        with open(logfile, 'r') as f:
            lines = f.readlines()
            num_lines = len(lines)

        # Vider le fichier de journalisation si le nombre de lignes atteint 500
        if num_lines >= 500:
            with open(logfile, 'w'):
                pass

def log_critical(message):
    logging.critical(message)
