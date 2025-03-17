import requests
from bs4 import BeautifulSoup
import pandas as pd 


headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36' }

df = pd.read_csv("./app/link/city/city.csv", encoding="utf-8")

for _, row in df.iterrows():
    city = row["City"].replace(" ", "_")  
    url = row["Link"]
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        
        soup = BeautifulSoup(response.content, 'html.parser')

        if soup.find("h1", string=lambda text: text and "Cannot find city id for" in text):
            url = url + "-France"  
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
        
        with open(f'./app/extract/all_index/index_{city}.html', 'w', encoding="utf-8") as f:
            f.write(soup.prettify())
        
        print(f"Page enregistrée pour {city}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'extraction pour {city}: {e}")