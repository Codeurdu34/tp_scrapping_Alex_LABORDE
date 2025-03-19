import pandas as pd 
from bs4 import BeautifulSoup
import requests

def find_link(city):
    """Génère le bon lien pour une ville en testant si elle est trouvée sur Numbeo."""
    
    # Remplacement des espaces et des virgules pour un format d'URL correct
    city_url = city.replace(" ", "-").replace(",", "-")
    link = f"https://www.numbeo.com/cost-of-living/in/{city_url}"
    
    # User-Agent pour éviter d'être bloqué
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }

    # Récupérer la page HTML
    try:
        response = requests.get(link, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Vérifier si la ville est introuvable
        if "Cannot find city id for" in soup.text:
            return f"https://www.numbeo.com/cost-of-living/in/{city_url}-France"
        else:
            return link
    except requests.exceptions.RequestException as e:
        print(f"Erreur pour {city}: {e}")
        return None  # Retourne None en cas d'erreur réseau

# Charger le fichier CSV contenant les villes
df = pd.read_csv("./app/link/city/city.csv", encoding="utf-8")

# Vérifier si la colonne "Link" existe, sinon l'ajouter
if "Link" not in df.columns:
    df["Link"] = ""

# Appliquer la fonction pour générer les liens corrects
df["Link"] = df["City"].apply(find_link)

# Sauvegarder les résultats
df.to_csv("./app/link/city/city.csv", index=False, encoding="utf-8")

print("Liens mis à jour avec succès dans city.csv")
