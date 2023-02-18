import matplotlib.pyplot as plt

# Créez des données pour le graphique
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Créez un graphique avec les données
plt.plot(x, y)

# Ajoutez des étiquettes pour les axes X et Y et un titre pour le graphique
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.title("Mon Graphique")

# Affichez le graphique
plt.show()
