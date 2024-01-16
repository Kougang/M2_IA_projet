import pandas as pd
import random
import csv

# Liste des matières et des moyennes pour le cycle secondaire et universitaire
matieres = [
    "M_3_MATH", "M_3_PHYSIQUE", "M_3_CHIMIE", "M_3_INFO", "M_3_BIOLOGIE",
    "M_3_FRANCAIS", "M_3_ANGLAIS", "M_3_LANGUE_E", "M_3_HIST", "M_3_GEO", "M_3_PHILO"
]
moyennes = ["moy_level1", "moy_level2", "moy_level3"]

# generation aleatoire des valeurs pour notre jeu de donnees
def generer_donnees_aleatoires():
  # generation des notes du secondaire, la plus petite note autorisables est 8 et max 20
    notes = [random.randint(8, 20) for _ in range(len(matieres))]
  # autre
    grade_probatoire = random.randint(10, 20)
    grade_bac = random.randint(10, 20)
    serie = random.randint(1, 5)
    redoublant_secondaire = random.randint(0, 1)
    age_obtention_bac = random.randint(14, 25)
    sexe = random.randint(0, 1)
    region_etude_secondaire = random.randint(1, 11)

    moy = [random.randint(10, 20) for _ in range(len(moyennes))]

    formation_sci = random.randint(1, 15)
    nbr_echec_univ = random.randint(0, 4)
    reussi_etudiant_diplome = random.randint(0, 1)
    carriere_domaine_form = random.randint(0, 1)
    max_level = random.randint(1, 3)

#  retourne l'enregistrement aleatoire a stocker dans notre fichier csv
    return notes + [
        grade_probatoire, grade_bac, serie, redoublant_secondaire,
        age_obtention_bac, sexe, region_etude_secondaire] + moy + [
        formation_sci, nbr_echec_univ, reussi_etudiant_diplome,
        carriere_domaine_form, max_level]

# Enregistre les combinaisons de notes et attributs dans un fichier CSV
with open('dataset_generat.csv', 'w', newline='') as fichier_csv:
    instance = csv.writer(fichier_csv)

    # En-tête du fichier CSV
    entetes = matieres + ["grade_probatoire", "grade_bac", "serie", "redoublant_secondaire",
                          "age_obtention_bac", "sexe", "region_etude_secondaire"] + moyennes + [
                          "formation_sci", "nbr_echec_univ", "reussi_etudiant_diplome",
                          "carriere_domaine_form", "max_level"]

    instance.writerow(entetes)

    # Génèration de 5000 enregistrement
    nombre_combinaisons = 5000  
    for _ in range(nombre_combinaisons):
        enregistrement = generer_donnees_aleatoires()
        instance.writerow(enregistrement)

# fichier = pd.read_csv('/content/drive/MyDrive/PROJET_MASTER2/dataset_generat.csv')
# print(fichier)