import pandas as pd
import numpy as np

# Pour l'imputation avancée
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def impute_missing_values(input_csv="data.csv", output_csv="data_imputed.csv"):
    """
    1) Charge le CSV (input_csv).
    2) Détecte les colonnes numériques et catégorielles.
    3) Impute les colonnes numériques avec un algorithme ML (IterativeImputer ou KNNImputer).
    4) Impute les colonnes catégorielles avec la valeur la plus fréquente (SimpleImputer).
    5) Enregistre le CSV complété (output_csv).
    """

    # 1) Chargement du CSV
    df = pd.read_csv(input_csv)
    print("=== Aperçu du dataset avant imputation ===")
    print(df.head())
    print(df.info())

    # 2) Séparer les colonnes selon leur type
    #    - On considère "numériquement" toute colonne de type int ou float
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    #    - Les autres colonnes sont considérées comme catégorielles (object, string, bool, etc.)
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

    print(f"Colonnes numériques détectées : {numeric_cols}")
    print(f"Colonnes catégorielles détectées : {categorical_cols}")

    # 3) Imputation pour les colonnes numériques
    # Vous pouvez choisir : IterativeImputer (méthode MICE) ou KNNImputer
    # -------------------
    # Ex. : IterativeImputer
    iter_imputer = IterativeImputer(random_state=42)
    # ou : KNNImputer(n_neighbors=5)
    # knn_imputer = KNNImputer(n_neighbors=5)

    if numeric_cols:
        df_numeric = df[numeric_cols]
        df_numeric_imputed = iter_imputer.fit_transform(df_numeric)
        df[numeric_cols] = df_numeric_imputed
    else:
        print("Aucune colonne numérique à imputer.")

    # 4) Imputation pour les colonnes catégorielles
    # On peut simplement prendre la valeur la plus fréquente
    if categorical_cols:
        cat_imputer = SimpleImputer(strategy='most_frequent')
        df_categorical = df[categorical_cols]
        df_categorical_imputed = cat_imputer.fit_transform(df_categorical)
        df[categorical_cols] = df_categorical_imputed
    else:
        print("Aucune colonne catégorielle à imputer.")

    # 5) Enregistrement du CSV complété
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"\n=== Imputation terminée. Fichier sauvegardé : {output_csv} ===")
    print("=== Aperçu du dataset après imputation ===")
    print(df.head())

if __name__ == "__main__":
    # Adaptez les chemins selon votre environnement
    impute_missing_values(
        impute_missing_values(
            input_csv="ml/data/combined_city_data.csv"
            output_csv="ml/data/data_imputed.csv"
        )
    )
