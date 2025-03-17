import re 

def clean_data(data):
    cleaned_data = re.sub(r'\s+', ' ', data).strip()
    cleaned_data = cleaned_data.replace('km', '')
    cleaned_data = cleaned_data.replace('"', '')
    cleaned_data = cleaned_data.replace(' €', '')
    cleaned_data = re.sub(r'(?<=\d),(?=\d)', '',cleaned_data)
    cleaned_data = cleaned_data.replace('\xa0€', '')
        
    return cleaned_data.strip()