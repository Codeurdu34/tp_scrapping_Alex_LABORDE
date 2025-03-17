import pandas as pd 
from bs4 import BeautifulSoup

with open('./app/link/index_home/index.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

select_tag = soup.find("select", {"name": "city"})

villes = [option.text.strip() for option in select_tag.find_all("option") if option.text.strip()]

df = pd.DataFrame({"City": villes})

# Sauvegarder en CSV
df.to_csv('./app/link/city/city.csv', index=False, encoding="utf-8")
