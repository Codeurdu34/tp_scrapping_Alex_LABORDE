import pandas as pd
import os

def create_descriptions_list(
    input_csv=r"D:\cours_Epsi\cours\cours_recupération_des _donner\tp_Alex_LABORDE\data\Acheres_cleaned_data.csv",
    output_csv="ml/data/descriptions_list.csv"
):
        
    if not os.path.exists(input_csv):
        print(f"[ERREUR] Fichier introuvable : {input_csv}")
        return

    
    df = pd.read_csv(input_csv)

    # Choix des colonnes à extraire
    
    columns_to_keep = ["Description"]

    
    df_extract = df[columns_to_keep]

    # Nettoyage éventuel
    df_extract.dropna(subset=["Description"], inplace=True)

    # Sauvegarde du résultat dans 'descriptions_list.csv'
    df_extract.to_csv(output_csv, index=False, encoding='utf-8')

    print(f"Fichier '{output_csv}' créé avec {len(df_extract)} lignes.")


