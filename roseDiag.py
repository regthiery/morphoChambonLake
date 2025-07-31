import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lire le fichier CSV
data = pd.read_csv("dataLineaments.csv")

# Sélectionner la colonne "azimuth" (valeurs de 0 à 180 ou 360)
azimuths = data["azimuth"] % 360  # au cas où certaines valeurs dépasseraient 360

# Dupliquer chaque azimut en ajoutant 180° modulo 360
azimuths_sym = (azimuths + 180) % 360

# Combiner les directions originales et symétriques
all_azimuths = pd.concat([azimuths, azimuths_sym])

# Conversion en radians
azimuths_rad = np.radians(all_azimuths)

# Paramètres du diagramme
bin_count = 36  # 10° par secteur
n, bins = np.histogram(azimuths_rad, bins=bin_count, range=(0, 2*np.pi))

# Création du diagramme en rose
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Angles au centre de chaque secteur
angles = np.linspace(0, 2*np.pi, bin_count, endpoint=False)
width = (2 * np.pi) / bin_count

# Affichage des barres
#bars = ax.bar(angles, n, width=width, bottom=0.0,
#              edgecolor='black', color=plt.cm.plasma(n / n.max()))

bars = ax.bar(angles, n, width=width, bottom=0.0,
              edgecolor='black', color='lightgray')

# Orientation du diagramme : 0° en haut, sens horaire
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# Étiquettes toutes les 30°
ax.set_xticks(np.radians(np.arange(0, 360, 30)))
ax.set_xticklabels(['N', '30°', '60°', 'E', '120°', '150°', 'S', '210°', '240°', 'W', '300°', '330°'])

# Titre
ax.set_title("Symmetrical Rose Diagram of Fault Orientations", va='bottom')

# Affichage
plt.show()
