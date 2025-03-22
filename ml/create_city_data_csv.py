import pandas as pd

def create_city_data_csv():

    # Définition des chemins des fichiers
    descriptions_file = "ml/data/descriptions_list.csv"  # Liste des descriptions
    output_file = "ml/data/combined_city_data.csv"  # Fichier de sortie

    
    Name_city = "app/link/city/city.csv"
    df_Name_city = pd.read_csv(Name_city)
    Name_city_list = df_Name_city["City"].tolist()

    # Charger les descriptions depuis descriptions_list.csv
    df_descriptions = pd.read_csv(descriptions_file)


    # Transformer les descriptions en colonnes
    descriptions_list = df_descriptions["Description"].tolist()
    combined_city_data = pd.DataFrame(index=Name_city_list, columns=descriptions_list)


    # Sauvegarder le CSV avec les colonnes mais sans données
    combined_city_data.to_csv(output_file, index=True, encoding="utf-8")

