import pandas as pd 
import re 
from bs4 import BeautifulSoup
from app.extract.features.clean_data import clean_data
from app.extract.features.min_max import trouver_prix_min_max
import os 

def creat_all_data_frame(city):
    
    
    city_filename = city.replace(",", "").replace(" ", "_")  # Supprime les virgules et remplace espaces par "_"
    file_path = f'./app/extract/all_index/index_{city_filename}.html'

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")

    try:
        with open(file_path, encoding="utf-8") as fp:
            soup = BeautifulSoup(fp, 'html.parser')
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la lecture du fichier {file_path} : {e}")
    
    lignes_sale = soup.select('tr')

    desc = []
    prix = []
    prix_min_max = []

    for ligne in lignes_sale:
        cells = ligne.select('td')
        if len(cells) == 1:
            continue 
        elif len(cells) == 3:
            desc.append(clean_data(cells[0].text))
            prix.append(clean_data(cells[1].text))
            prix_min_max.append(clean_data(cells[2].text))
        elif len(cells) == 2:
            continue
    
    # Calculer les prix min et max
    prix_min, prix_max = trouver_prix_min_max(prix_min_max)
    
    # Créer un DataFrame avec les données extraites
    df = pd.DataFrame({
        "Description": desc,
        "Prix Moyen (€)": prix,
        "Prix Min-Max (€)": prix_min_max,
        "Prix Min (€)": prix_min,
        "Prix Max (€)": prix_max
    })
    
    # Supprimer les lignes vides
    df.dropna(inplace=True)

    print(f" Données extraites pour {city} - {len(df)} lignes enregistrées.")

    return df
