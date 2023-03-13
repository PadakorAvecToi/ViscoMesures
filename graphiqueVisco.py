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
w = []
z = []

# Parcourez chaque ligne du fichier TXT
for line in data[1:]:
    # Séparez les valeurs x, y, w et z en utilisant la tabulation comme séparateur
    split_line = line.split('\t')
    x.append(float(split_line[0]))
    y.append(float(split_line[3]))
    w.append(float(split_line[1]))
    z.append(float(split_line[4]))

# Créez une figure avec deux sous-graphiques
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Tracez les données dans les sous-graphiques correspondants
ax1.plot(x, y, color='blue', linewidth=2)
ax2.plot(w, z, color='red', linewidth=2)

# Ajoutez des étiquettes pour les axes X et Y et un titre pour chaque sous-graphique
ax1.set_xlabel("Axe X", fontsize=12)
ax1.set_ylabel("Axe Y", fontsize=12)
ax1.set_title("Graphique Réel", fontsize=14)
ax2.set_xlabel("Axe X", fontsize=12)
ax2.set_ylabel("Axe Y", fontsize=12)
ax2.set_title("Graphique Imaginaire", fontsize=14)

# Ajouter une grille aux sous-graphiques
ax1.grid(True)
ax2.grid(True)

# Modifier l'apparence de la grille
ax1.grid(color='gray', linestyle='-', linewidth=0.5)
ax2.grid(color='gray', linestyle='-', linewidth=0.5)

# Ajouter une légende aux sous-graphiques
ax1.legend(['Données réelles'], loc='upper right', fontsize=12)
ax2.legend(['Données imaginaires'], loc='upper right', fontsize=12)

# Modifier la couleur de fond de la figure
fig.patch.set_facecolor('#f2f2f2')

# Modifier les marges autour des sous-graphiques
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

# Afficher la fenêtre avec les deux graphiques
plt.show()
