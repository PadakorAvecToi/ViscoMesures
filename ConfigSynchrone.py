import xml.etree.ElementTree as ET

# Création d'un élément racine
root = ET.Element("configurations")

# Ajout d'un élément pour chaque configuration
config1 = ET.SubElement(root, "configuration")
config1.set("nom", "Config 1")

freq_modulation = ET.SubElement(config1, "frequence_modulation")
freq_modulation.text = "1000"

freq_reference = ET.SubElement(config1, "frequence_reference")
freq_reference.text = "5000"

freq_coupure = ET.SubElement(config1, "frequence_coupure")
freq_coupure.text = "2000"

config2 = ET.SubElement(root, "configuration")
config2.set("nom", "Config 2")

freq_modulation = ET.SubElement(config2, "frequence_modulation")
freq_modulation.text = "2000"

freq_reference = ET.SubElement(config2, "frequence_reference")
freq_reference.text = "6000"

freq_coupure = ET.SubElement(config2, "frequence_coupure")
freq_coupure.text = "3000"

# Écriture des configurations dans un fichier XML
tree = ET.ElementTree(root)
tree.write("configurations.xml")



