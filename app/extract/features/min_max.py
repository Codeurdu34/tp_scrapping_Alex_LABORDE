def trouver_prix_min_max(donnees_epurees):
    prix_min = []
    prix_max = []
    
    for prix in donnees_epurees:  
        if '-' in prix: 
            parts = prix.split('-')
            prix_min.append(float(parts[0].strip()))  
            prix_max.append(float(parts[1].strip()))
        else:
            prix_min.append(None)  
            prix_max.append(None)  
    
    return prix_min, prix_max