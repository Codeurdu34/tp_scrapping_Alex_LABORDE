from app.extract.creat_all_data_frame import creat_all_data_frame
from app.load.transforme_in_csv import transforme_in_csv
from app.extract.extract_html_all_city import extract_html_all_city 

import pandas as pd 


headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36' }
cities_csv = pd.read_csv("./app/link/city/city.csv", encoding="utf-8")

extract_html_all_city()

for city in cities_csv["City"]:

    print(f"_____________________________________{city}__________________________________________________________")
    
    sade_data = (creat_all_data_frame(city))

    # print(sade_data)

    transforme_in_csv(sade_data,city)

    

    
