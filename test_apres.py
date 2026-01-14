from pymongo import MongoClient

#Connexion à MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['MedicalDB']
collection = db['patients']

#Compter le nombre de documents
nombre_documents = collection.count_documents({})
print(f"Nombre total de lignes insérées : {nombre_documents}")

