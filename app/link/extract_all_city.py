import pandas as pd 
import requests
from bs4 import BeautifulSoup



with open('./app/link/code_html/index.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

select_tag = soup.find("select", {"name": "city"})

villes = [option.text.strip() for option in select_tag.find_all("option") if option.text.strip()]

# df. to_csv('votre_nom_de_fichier. csv', index=False)
# for ville in villes:
#     print(ville)

with open('./app/link/info_csv/city.csv', "w", encoding="utf-8") as f:
        f.write("\n".join(villes))

