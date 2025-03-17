import pandas as pd

def transforme_in_csv(df,city):

    df.to_csv(f"data/{city}_cleaned_data.csv", index=False)

    print("Transformation réussi ! ")