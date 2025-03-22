# Projet de Récupération & Analyse des Coûts de la Vie (Scraping + Machine Learning)



---

## Structure du projet

### 1. `main.py`

- Extraire les noms des villes disponibles
- Récupérer les pages HTML de chaque ville via scraping
- Nettoyer et structurer les données
- Générer des fichiers CSV contenant les données par ville

 **Conseil** :  
Pour **gagner du temps**, vous pouvez **interrompre l’exécution** une fois qu’un certain nombre de fichiers `.csv` ont été générés dans le dossier `data/`.

**faite un Ctrl C** lorsque vous voyez 
``` bash
_____________________________________Antibes__________________________________________________________
Données extraites pour Antibes - 54 lignes enregistrées.
Transformation réussi ! *

Vous pourrez ensuite passer directement à l'étape de machine learning.
```

---

### 2. `ml/main.py` (dans le dossier `ml/`)

Ce second script est **dédié à la partie Machine Learning**, il permet de :
- Charger les données agrégées
- Compléter les valeurs manquantes par des techniques d’imputation
- Normaliser les données si nécessaire
- Sauvegarder un nouveau jeu de données prêt à l’analyse

---

## Prérequis

Assurez-vous d’avoir une bonne conection internet et d'installé les dépendances suivantes :

```bash
pip install -r requirements.txt
