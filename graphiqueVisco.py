"""
import matplotlib.pyplot as plt

# Créez des données pour le graphique
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Créez un graphique avec les données
plt.plot(x, y)

# Ajoutez des étiquettes pour les axes X et Y et un titre pour le graphique
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.title("Graphique Réel")

# Affichez le graphique
plt.show()

# Créez des données pour le graphique
w = [5, 6, 7, 8, 9]
z = [2, 8, 18, 32, 50]

# Créez un graphique avec les données
plt.plot(w, z)

# Ajoutez des étiquettes pour les axes X et Y et un titre pour le graphique
plt.xlabel("Axe x")
plt.ylabel("Axe Y")
plt.title("Graphique Imaginaire")

# Affichez le graphique
plt.show()
"""

import matplotlib.pyplot as plt

# Ouvrez le fichier TXT contenant les données
with open('ametek air 480.945 etuve 20°.1C fil 0.1mm 0.06V dans cellule.txt', 'r') as f:
    data = f.read().splitlines()

# Créez des listes pour stocker les données
x = []
y = []

# Parcourez chaque ligne du fichier TXT
for line in data:
    # Séparez les valeurs x et y en utilisant la virgule comme séparateur
    split_line = line.split(',')
    x.append(int(split_line[0]))
    y.append(int(split_line[1]))

# Tracez les données dans un graphique
plt.plot(x, y)

# Ajoutez des étiquettes pour les axes X et Y et un titre pour le graphique
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.title("Mon Graphique")

# Affichez le graphique
plt.show()
