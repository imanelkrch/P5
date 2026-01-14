import pandas as pd
from pymongo import MongoClient

def migration():
    # Connexion au conteneur MongoDB
    #client = MongoClient('mongodb://mongodb:27017/')
    #client = MongoClient('mongodb://localhost:27017/')

    uri = "mongodb://admin_user:adminpassword@mongodb:27017/MedicalDB?authSource=MedicalDB"
    client = MongoClient(uri)
    db = client['MedicalDB']
    collection = db['patients']

    # Chargement du fichier CSV
    df = pd.read_csv('healthcare_dataset.csv')

    # Liste pour stocker les documents
    documents = []

    for _, row in df.iterrows():
        # Création d'un document
        doc = {
            "name": str(row['Name']).title().strip(),
            "age": int(row['Age']),
            "gender": row['Gender'],
            "blood_type": row['Blood Type'],
            "medical_condition": row['Medical Condition'],
            "date_of_admission": row['Date of Admission'],
            "doctor": row['Doctor'],
            "hospital": row['Hospital'],
            "insurance_provider": row['Insurance Provider'],
            "billing_amount": float(row['Billing Amount']),
            "medication": row['Medication'],
            "admission_type": row['Admission Type'],
            "discharge_date": row['Discharge Date'],
            "room_number": row['Room Number'],
            "test_results": row['Test Results']
        }
        documents.append(doc)

    # Insertion dans MongoDB
    if documents:
        collection.insert_many(documents)
    
    # On compte le total actuel après l'ajout
    total_final = collection.count_documents({})
    print(f"{len(documents)} nouvelles lignes ajoutées.")
    print(f"Total actuel en base : {total_final} documents.")

if __name__ == "__main__":
    migration()