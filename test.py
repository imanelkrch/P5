from pymongo import MongoClient

#Connexion à MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['MedicalDB']
collection = db['patients']

print("RECHERCHE D'UN PATIENT")

#Le nom que l'on cherche
nom_recherche = "Paul Henderson"

#On récupère tous les documents correspondant à ce nom
resultats = list(collection.find({"name": nom_recherche}))

#Résultat
if len(resultats) > 0:
    print(f"Patient trouvé")
    
    # On prend les infos générales du premier document trouvé
    infos_generales = resultats[0]
    print(f"Nom : {infos_generales['name']}")
    print(f"Age : {infos_generales['age']}")
    print(f"Genre : {infos_generales['gender']}")
    
    # Le nombre d'admissions
    print(f"Nombre d'admissions enregistrées : {len(resultats)}")
    
else:
    print(f"Aucun patient trouvé avec le nom : {nom_recherche}")