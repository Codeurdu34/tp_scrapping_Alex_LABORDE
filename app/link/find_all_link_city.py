import pandas as pd 
import os

print("Chemin actuel :", os.getcwd())

def find_link(city):
    
    return f"https://www.numbeo.com/cost-of-living/in/{city.replace(' ', '-')}"

df = pd.read_csv("./app/link/info_csv/city.csv")#, encoding="utf-8")



print("Chemin actuel :", os.getcwd())


with open('./app/link/all_link_city.csv', "w", encoding="utf-8") as f:
    for city in df.iloc[:, 0]: 
        f.write(find_link(city) + "\n")  
