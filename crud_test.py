from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['MedicalDB']
collection = db["patients"]

# CREATE
collection.insert_one({
    "name": "Test Patient",
    "age": 45,
    "gender": "Female",
    "medical_condition": "Diabetes"
})

# READ
print(collection.find_one({"name": "Test Patient"}))

# UPDATE
collection.update_one(
    {"name": "Test Patient"},
    {"$set": {"age": 46}}
)

# DELETE
collection.delete_one({"name": "Test Patient"})