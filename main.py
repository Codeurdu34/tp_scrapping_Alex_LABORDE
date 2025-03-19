import pandas as pd 
 
from app.link.extract_all_city import extract_all_city
from app.link.extract_html import extract_html
from app.extract.creat_all_data_frame import creat_all_data_frame
from app.extract.extract_html_all_city import extract_html_all_city 

from app.load.transforme_in_csv import transforme_in_csv




headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36' }
extract_html()
extract_all_city()

cities_csv = pd.read_csv("./app/link/city/city.csv", encoding="utf-8")

if "Link" not in cities_csv.columns:
    cities_csv["Link"] = cities_csv["City"].apply(lambda city: f"https://www.numbeo.com/cost-of-living/in/{city.replace(' ', '-')}")
    cities_csv.to_csv("./app/link/city/city.csv", index=False, encoding="utf-8")
    print("Colonne 'Link' ajoutée automatiquement.")





extract_html_all_city()



for city in cities_csv["City"]:

    print(f"_____________________________________{city}__________________________________________________________")
    
    sade_data = (creat_all_data_frame(city))

    # print(sade_data)

    transforme_in_csv(sade_data,city)

    


