from create_city_data_csv import create_city_data_csv
from combine_city_data import combine_city_data
from impute_data import impute_missing_values
from creat_description_data import create_descriptions_list

if __name__ == "__main__":
    
    create_descriptions_list()
    create_city_data_csv()
    
    combine_city_data()
    # Un seul appel, avec virgule entre les paramètres
    impute_missing_values(
        input_csv="ml/data/combined_city_data.csv",
        output_csv="ml/data/data_imputed.csv"
    )
