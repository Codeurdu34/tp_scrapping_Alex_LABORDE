import pandas as pd
import glob
import os

def combine_city_data():
    data_folder = r"D:\cours_Epsi\cours\cours_recupération_des _donner\tp_Alex_LABORDE\data\*.csv"
    output_file = r"D:\cours_Epsi\cours\cours_recupération_des _donner\tp_Alex_LABORDE\ml\data\combined_city_data.csv"

    # glob.glob récupère la liste de tous les fichiers correspondant au pattern (*.csv)
    csv_files = glob.glob(data_folder)
    

    if not csv_files:
        print("Aucun fichier CSV trouvé dans :", data_folder)
        return

    all_dataframes = []

    # Parcourt chaque fichier CSV récupéré
    for file in csv_files:
        try:
            df_temp = pd.read_csv(file)
            
            filename = os.path.basename(file)  
            city_name = filename.replace("_cleaned_data.csv", "")  
            
            df_temp.rename(columns={
                "Description": "description",
                "Prix Moyen (€)": "price"
            }, inplace=True)
            
            df_temp["city"] = city_name

            
            if "price" not in df_temp.columns or "description" not in df_temp.columns:
                print(f"[AVERTISSEMENT] Fichier ignoré (colonnes incorrectes) : {file}")
                print("Colonnes présentes :", df_temp.columns.tolist())
                continue

            
            df_temp = df_temp[["city", "description", "price"]]

            df_temp["price"] = df_temp["price"].apply(lambda x: str(x).replace(",", "."))
            df_temp["price"] = pd.to_numeric(df_temp["price"], errors="coerce")

            all_dataframes.append(df_temp)

        except Exception as e:
            print(f"Erreur de lecture du fichier {file} : {e}")

    # Concaténation de tous les DataFrames dans un seul DataFrame
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    

    # On pivote
    grouped = combined_df.groupby(["city", "description"])["price"].mean().reset_index()

    
    pivot_df = grouped.pivot(index="city", columns="description", values="price")

    
    pivot_df.to_csv(output_file)


