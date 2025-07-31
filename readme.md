# Analyse de Linéaments – Scripts Python

Ce dossier contient un ensemble de scripts Python permettant de traiter, visualiser et classifier des linéaments géologiques à partir de données stockées dans un fichier CSV.

## Contenu du dossier

### Données
- **`dataLineaments.csv`**  
  Fichier de données contenant la liste des linéaments (avec les coordonnées, longueurs, azimuts, etc.).  
  Ce fichier sert d'entrée aux différents scripts Python du dossier.

### Scripts Python

- **`histoLength.py`**  
  Génère un histogramme des longueurs des linéaments présents dans le fichier CSV.  
  Permet d’analyser la distribution des longueurs.

- **`histoAzimut.py`**  
  Crée un histogramme des azimuts des linéaments.  
  Utile pour repérer les directions dominantes.

- **`roseDiag.py`**  
  Produit un diagramme en rose (rose des directions) basé sur les azimuts.  
  Ce script met en évidence la symétrie directionnelle des linéaments et les orientations préférentielles.

- **`classification.py`**  
  Réalise une classification automatique des linéaments en familles directionnelles.  
  Utilise des techniques statistiques ou d’apprentissage non supervisé pour regrouper les linéaments similaires (ex. k-means, DBSCAN, etc.).

## Utilisation

Assurez-vous d’avoir un environnement Python activé (ex. : `source env/bin/activate`) avec les bibliothèques nécessaires installées (`pandas`, `matplotlib`, `numpy`, etc.).

Exemple d'exécution d'un script :
```bash
python histoLength.py

## 🧩 Dépendances

Les scripts utilisent les bibliothèques Python suivantes :

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn` (optionnel, pour des graphiques plus esthétiques)
- `scikit-learn` (utilisé dans `classification.py` pour l’algorithme de clustering)

---

## Installation

1. **Créer un environnement virtuel** (optionnel mais recommandé) :
   ```bash
   python -m venv env
   source env/bin/activate        # Linux / macOS
   .\env\Scripts\activate         # Windows

## 👤 Auteur

**Régis Thiéry**  
Maître de conférences en géologie – Université Clermont Auvergne  
Spécialisé en géologie structurale, thermodynamique des fluides et SIG appliqué aux géosciences.

- Chaîne YouTube : [@Geo-Cool](https://www.youtube.com/@Geo-Cool)
- Contact : regthiery[at]gmail.com (remplacer [at] par @)
