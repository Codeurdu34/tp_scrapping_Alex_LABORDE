import pandas as pd
import numpy as np


from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def impute_missing_values(input_csv="ml/data/combined_city_data.csv", output_csv="ml/data/data_imputed.csv"):

    # Lit le CSV 'ml/data/combined_city_data.csv'
    df = pd.read_csv(input_csv)
    

    # Identification des types de colonne qu'on veut manipuler 
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

    iter_imputer = IterativeImputer(random_state=42, max_iter=20)

    
    # Imputation des valeurs manquantes dans les numeric_cols 
    ''' l'imputation désigne le processus de remplacement des données manquantes avec des valeurs substituées'''

    if numeric_cols:
        df_numeric = df[numeric_cols]
        df_numeric_imputed = iter_imputer.fit_transform(df_numeric)
        df[numeric_cols] = df_numeric_imputed
    else:
        print("Aucune colonne numérique à imputer.")

    # Imputation des valeurs manquantes dans les categorical_cols 
    if categorical_cols:
        cat_imputer = SimpleImputer(strategy='most_frequent')
        df_categorical = df[categorical_cols]
        df_categorical_imputed = cat_imputer.fit_transform(df_categorical)
        df[categorical_cols] = df_categorical_imputed
    else:
        print("Aucune colonne catégorielle à imputer.")

    # Export du CSV imputé
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"\n→ Imputation terminée. Fichier sauvegardé : {output_csv}")

