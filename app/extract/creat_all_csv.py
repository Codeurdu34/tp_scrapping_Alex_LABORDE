import pandas as pd 
import re 
from bs4 import BeautifulSoup
from clean_data import clean_data

cities_csv = pd.read_csv("./app/link/city/city.csv", encoding="utf-8")



    
def extract_data_line_html(city):
    with open(f'./app/extract/all_index/index_{city}.html') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    lignes_sale = soup.select('tr')

    desc = []
    prix = []
    prix_min_max = []


    for ligne in lignes_sale:
        cells = ligne.select('td')
        if len(cells) == 1 :
            desc.append(clean_data(cells[0].text)) 
        elif len(cells) == 3:
            desc.append(clean_data(cells[0].text))
            prix.append(clean_data(cells[1].text))
            prix_min_max.append(clean_data(cells[2].text))
        elif len(cells) == 2:
            desc.append(clean_data(cells[0].text))
            prix.append(clean_data(cells[1].text))
    
    return desc, prix, prix_min_max









for city in cities_csv["City"]:

    print(f"_______________________{city}__________________________________________________________")
    
    print(extract_data_line_html(city))