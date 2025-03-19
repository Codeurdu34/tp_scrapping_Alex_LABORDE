import requests
from bs4 import BeautifulSoup

def extract_html(): 
    url = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=France'

    header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36' }

    reponse = requests.get(url, headers=header)
    soup = BeautifulSoup(reponse.content, 'html.parser')



    f= open('./app/link/index_home/index.html', 'w')
    f.write(soup.prettify())
    f.close()