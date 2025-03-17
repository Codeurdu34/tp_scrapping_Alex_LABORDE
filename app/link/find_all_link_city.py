import pandas as pd 
from bs4 import BeautifulSoup
import requests

def find_link(city):
    link = f"https://www.numbeo.com/cost-of-living/in/{city.replace(' ', '-')}"
    header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36' }

    reponse = requests.get(link, headers=header)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    if not soup.find("Cannot find city id for"):
        return f"https://www.numbeo.com/cost-of-living/in/{city.replace(' ', '-')}-France"
    else: return f"https://www.numbeo.com/cost-of-living/in/{city.replace(' ', '-')}"


df = pd.read_csv("./app/link/city/city.csv", encoding="utf-8")


df["Link"] = df["City"].apply(find_link)


df.to_csv("./app/link/city/city.csv", index=False, encoding="utf-8")

