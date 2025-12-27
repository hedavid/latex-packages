import csv
import os

from unidecode import unidecode

def enlever_accents(texte):
    return unidecode(texte)

# Dictionnaire pour compter les occurrences de chaque annotation
compteur_annotations = {}
compteur_OK = 0
compteur_KO = 0

with open('openmoji.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        code_actuel = row['hexcode']  # adapter le nom de colonne
        annotation = row['annotation']
        for char in [':', '/', '\\', '*', '?', '"', '<', '>', '|', '“', '”']:
            annotation = annotation.replace(char, '-')
        annotation = enlever_accents(annotation)
        annotation = annotation.replace('â€œ', '').replace('â€', '')
        
        # Gestion des doublons
        if annotation in compteur_annotations:
            compteur_annotations[annotation] += 1
            suffixe = f" {compteur_annotations[annotation]}"
            annotation_finale = annotation + suffixe
        else:
            compteur_annotations[annotation] = 1
            annotation_finale = annotation

        fichier_source = f"{code_actuel}.svg"
        fichier_destination = f"{annotation_finale}.svg"
        
        # Renommer le fichier
        if os.path.exists(fichier_source):
            if not os.path.exists(fichier_destination):
                os.rename(fichier_source, fichier_destination)
                print(f"✓ {fichier_source} → {fichier_destination}")
                compteur_OK += 1
            else:
                print(f"⚠ {fichier_destination} existe déjà")
        else:
            print(f"✗ {fichier_source} non trouvé")
    print('-------')
    print(compteur_OK)