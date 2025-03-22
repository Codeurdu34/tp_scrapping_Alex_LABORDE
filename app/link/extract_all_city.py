import pandas as pd
from bs4 import BeautifulSoup

def extract_all_city():
    try:
        with open('./app/link/index_home/index.html', encoding='utf-8') as fp:
            content = fp.read()
    except UnicodeDecodeError:
        with open('./app/link/index_home/index.html', encoding='latin-1') as fp:
            content = fp.read()

    soup = BeautifulSoup(content, 'html.parser')
    select_tag = soup.find("select", {"name": "city"})

    if select_tag is None:
        print("[ERREUR] Aucune balise <select name='city'> trouvée dans le HTML.")
        return

    villes = []
    for option in select_tag.find_all("option"):
        ville = option.text.strip()
        if "Select city" in ville:
            continue
        # Nettoyage du nom
        ville = ville.replace(",", "").replace(" ", "-").replace("(", "").replace(")", "")
        villes.append(ville)

    df = pd.DataFrame({"City": villes})
    df.to_csv('./app/link/city/city.csv', index=False, encoding="utf-8")
    print(f"[OK] Fichier city.csv créé avec {len(villes)} villes.")
