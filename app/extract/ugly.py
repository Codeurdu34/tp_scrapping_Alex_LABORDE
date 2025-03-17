
import pandas as pd 
import re 
from bs4 import BeautifulSoup

def clean_data(data):
    cleaned_data = re.sub(r'\s+', ' ', data).strip()
    cleaned_data = cleaned_data.replace('km', '')
    cleaned_data = cleaned_data.replace('"', '')
    cleaned_data = cleaned_data.replace(' €', '')
    cleaned_data = re.sub(r'(?<=\d),(?=\d)', '',cleaned_data)
    cleaned_data = cleaned_data.replace('\xa0€', '')
        
    return cleaned_data.strip()

def cree_categorie(lignes):
    desc = []
    prix = []
    nearby_cities = []
    nearby_cities_km = []
    prix_min_max = []

    for ligne in lignes:
        cells = ligne.select('td')
        if len(cells) == 1 or len(cells) == 0:
            continue  # Ignore les lignes sans données pertinentes
        elif len(cells) == 3:
            desc.append(clean_data(cells[0].text))
            prix.append(clean_data(cells[1].text))
            prix_min_max.append(clean_data(cells[2].text))
        elif len(cells) == 2:
            nearby_cities.append(clean_data(cells[0].text))
            nearby_cities_km.append(clean_data(cells[1].text))
    
    return desc, prix, prix_min_max, nearby_cities, nearby_cities_km


def trouver_prix_min_max(donnees_epurees):
    prix_min = []
    prix_max = []
    
    for prix in donnees_epurees[2]:  # La liste des plages de prix
        if '-' in prix:  # Vérifie si une plage existe
            parts = prix.split('-')
            prix_min.append(float(parts[0].strip()))  # Supprime les espaces et convertit en float
            prix_max.append(float(parts[1].strip()))
        else:
            prix_min.append(None)  # Aucun prix minimum défini
            prix_max.append(None)  # Aucun prix maximum défini
    
    return prix_min, prix_max

def organiser_data(donnees_epurees):
    structured_data = []
    for i in range(len(donnees_epurees[0])):
        structured_data.append({
            "Description :": donnees_epurees[0][i], 
            "Prix moyen (€) :": float(donnees_epurees[1][i]) if donnees_epurees[5][i] is not None else None,
            "Prix min - max (€) :": donnees_epurees[2][i], 
            "Prix min (€) :": float(donnees_epurees[5][i]) if donnees_epurees[5][i] is not None else None,
            "Prix max (€) :": float(donnees_epurees[6][i]) if donnees_epurees[5][i] is not None else None,
            })
        
    for i in range(len(donnees_epurees[3])):
        structured_data.append({
            "Ville proche :": donnees_epurees[3][i], 
            "Distance (km)": (donnees_epurees[4][i])
            })
    return structured_data


def oorganiser_data(donnees_epurees):
    structured_data = []

    # Ajout des descriptions et des prix
    for i in range(len(donnees_epurees[0])):
        structured_data.append({
            "Description": donnees_epurees[0][i],
            "Prix moyen (€)": float(donnees_epurees[1][i]),
            "Prix min - max (€)": donnees_epurees[2][i],
            "Prix min (€)": float(donnees_epurees[5][i]) if donnees_epurees[5][i] is not None else None,
            "Prix max (€)": float(donnees_epurees[6][i]) if donnees_epurees[6][i] is not None else None,
        })

    # Ajout des villes proches et distances
    villes_proches = []
    for i in range(len(donnees_epurees[3])):
        villes_proches.append({
            "Ville proche": donnees_epurees[3][i],
            "Distance (km)": float(donnees_epurees[4][i])
        })

    return {"Produits": structured_data, "Villes proches": villes_proches}


def transformer_dataframe(structured_data):
    df = pd.DataFrame(structured_data)
    print(df)
    df.to_csv("cleaned_data.csv", index=False)
    return df


def split_csv(file_path):
    df = pd.read_csv(file_path, encoding="utf-8")
    
    
    price_columns = ["Ville proche :","Distance (km)"]
    df_price = df.drop(columns=price_columns)

    
    if "Prix moyen (€) :" in df_price.columns:
        df_price = df_price[df_price["Prix moyen (€) :"].notna()]

    df_price.to_csv("cl_data_price.csv", index=False, encoding="utf-8")
    
  
    size_columns = ["Description :","Prix moyen (€) :","Prix min - max (€) :","Prix min (€) :","Prix max (€) :"]
    df_size = df.drop(columns=size_columns)
    if "Distance (km)" in df_size.columns:
        df_size = df_size[df_size["Distance (km)"].notna()]
    df_size.to_csv("cl_data_size.csv", index=False, encoding="utf-8")

    
    

lignes = soup.select('tr') 
donnees_epurees = cree_categorie(lignes)
print(donnees_epurees)

# Extraire les lignes du tableau
lignes = soup.select('tr')

# Nettoyer et extraire les données
donnees_epurees = cree_categorie(lignes)

# Extraire les prix minimum et maximum
prix_min, prix_max = trouver_prix_min_max(donnees_epurees)

# Ajouter les prix min/max aux données épurées
desc, prix, prix_min_max, nearby_cities, nearby_cities_km = donnees_epurees
donnees_completes = desc, prix, prix_min_max, nearby_cities, nearby_cities_km, prix_min, prix_max

# Afficher les résultats
print("Données complètes :", donnees_completes)

lignes = soup.select('tr') 
donnees_epurees = cree_categorie(lignes)
structured_data = organiser_data(donnees_completes)
# print(structured_data)

lignes = soup.select('tr') 
donnees_epurees = cree_categorie(lignes)
structured_data = organiser_data(donnees_completes)
# print(structured_data)
# a =transformer_dataframe(structured_data)

split_csv("./cleaned_data.csv")