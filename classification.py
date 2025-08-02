import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.patches as mpatches

from sklearn.metrics import silhouette_score

# Lire le fichier CSV
data = pd.read_csv("dataLineaments.csv")

# Nettoyage des azimuts : valeurs entre 0 et 360
azimuths = data["azimuth"] % 360

# Duplication symétrique (180°) pour faire apparaître les familles de plans
azimuths_sym = (azimuths + 180) % 360
all_azimuths = pd.concat([azimuths, azimuths_sym], ignore_index=True)

# Conversion des azimuts en radians
azimuths_rad = np.radians(azimuths)
all_azimuths_rad = np.radians(all_azimuths)

# Transformation en coordonnées polaires unitaires (cosθ, sinθ)
X = np.column_stack((np.cos(azimuths_rad), np.sin(azimuths_rad)))



# Appliquer le clustering (par exemple avec 3 clusters)
n_clusters = 7

# Exemple de centres pour azimuts en degrés
centers_deg = [10, 40, 90, 110, 135, 155, 170]  
centers_rad = np.radians(centers_deg)
initial_centers = np.column_stack((np.cos(centers_rad), np.sin(centers_rad)))

kmeans = KMeans(n_clusters=len(centers_deg), init=initial_centers, n_init=1, random_state=42)


labels = kmeans.fit_predict(X)

# Calcul des directions moyennes de chaque cluster (azimut moyen en radians)
cluster_angles = np.arctan2(kmeans.cluster_centers_[:,1], kmeans.cluster_centers_[:,0]) % (2*np.pi)
cluster_angles_deg = np.degrees (cluster_angles)


# Liste des azimuts pour chaque point
azimuths_clustered = np.array(azimuths_rad)

# Dictionnaire pour stocker l'écart angulaire (en degrés)
cluster_std = {}

for i in range(n_clusters):
	theta_i = azimuths_rad[labels == i]
	sin_mean = np.mean(np.sin(theta_i))
	cos_mean = np.mean(np.cos(theta_i))
	R = np.sqrt(sin_mean**2 + cos_mean**2)
	circular_std_rad = np.sqrt(-2 * np.log(R))
	cluster_std[i] = np.degrees(circular_std_rad)


# Après le clustering
unique, counts = np.unique(labels, return_counts=True)
cluster_counts = dict(zip(unique, counts))




print("\nRésultats du clustering :")
for i in range(n_clusters):
    angle = cluster_angles_deg[i]
    count = cluster_counts[i]
    std = cluster_std[i]
    print(f"Cluster {i+1}: {count} éléments — direction moyenne ≈ {angle:.1f}° ± {std:.1f}°")


score = silhouette_score(X, labels)
print(f"Silhouette score: {score:.3f}")



# Histogramme des données selon les clusters
bin_count = 36
n, bins = np.histogram(all_azimuths_rad, bins=bin_count, range=(0, 2*np.pi))

# Création du diagramme en rosette
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Angles des centres de secteur
angles = np.linspace(0, 2*np.pi, bin_count, endpoint=False)
width = (2 * np.pi) / bin_count

# Affichage des barres grises pour toutes les données
bars = ax.bar(angles, n, width=width, bottom=0.0,
              edgecolor='black', color='lightgray', alpha=0.6)

# Couleurs pour chaque cluster
colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']

# Affichage des directions moyennes des clusters
for i, angle in enumerate(cluster_angles):
    ax.plot([angle, angle], [0, max(n)*1.1], color=colors[i % len(colors)], linewidth=3, label=f'Cluster {i+1}')


for i, angle in enumerate(cluster_angles):
    sigma = np.radians(cluster_std[i])
    start_angle = angle - sigma
    end_angle = angle + sigma

    bar_angle = angle
    bar_width = 2 * sigma
    bar_height = max(n) * 0.1  # hauteur du secteur d’incertitude

    ax.bar(bar_angle, bar_height, width=bar_width,
           bottom=max(n) * 1.05,
           color=colors[i],
           alpha=0.3,
           edgecolor='black',
           linewidth=0.5)



# Orientation du diagramme : 0° en haut, sens horaire
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# Étiquettes toutes les 30°
ax.set_xticks(np.radians(np.arange(0, 360, 30)))
ax.set_xticklabels(['N', '30°', '60°', 'E', '120°', '150°', 'S', '210°', '240°', 'W', '300°', '330°'])

# Titre et légende
ax.set_title("Clustering of Fault Azimuths – Rose Diagram", va='bottom')
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))



# Affichage
plt.show()

