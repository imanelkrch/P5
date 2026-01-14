import pandas as pd

#Chargement du fichier
df= pd.read_csv('/Users/imaneelkerrach/Documents/OC/P5/Projet_Migration_MongoDB/healthcare_dataset.csv')

print("TEST AVANT MIGRATION")

#Info Des donnees
print("Info Des donnees", df.info())

#Nombre de lignes totales
print("Nombre de lignes totales", len(df))

#Noms des colonnes
print("Noms des colonne", list(df.columns))

#Vérifier les types de données
print("Vérifier les types de données", df.dtypes)

#Compter les valeurs manquantes par colonne
print("Compter les valeurs manquantes par colonne", df.isnull().sum())

#Compter les doublons
print("Compter les doublons exacts (lignes identiques)", df.duplicated().sum())
