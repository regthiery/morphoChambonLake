import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lire le fichier CSV avec pandas
data = pd.read_csv("dataLineaments.csv")

# Sélectionner la colonne "azimuth"
azimuths = data["azimuth"]

# Dessiner l'histogramme
n, bins, patches = plt.hist(azimuths, bins=18)  # Vous pouvez ajuster le nombre de "bins" selon vos préférences

# Ajouter des labels et un titre
plt.xlabel("Azimuts (°)")
plt.ylabel("Fréquence")
plt.title("Histogramme des azimuts")

bin_count = 18
colors = plt.cm.plasma(np.linspace(0, 1, bin_count)).tolist()

for i, patch in enumerate(patches):
    patch.set_facecolor(colors[i])
    patch.set_edgecolor('black')
    patch.set_alpha(0.7)

# Afficher l'histogramme
plt.show()
