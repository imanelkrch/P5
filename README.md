# Migration CSV vers MongoDB

## Objectif

Migrer un dataset médical depuis un fichier CSV vers une base de données NoSQL MongoDB de manière automatisée.

## Technologies

- Python 3
- MongoDB
- Pandas
- PyMongo

## Dataset

healthcare_dataset.csv (55 500 lignes, données médicales)

## Étapes de la migration

1. Chargement et analyse du CSV
2. Vérification de l’intégrité des données
3. Nettoyage (doublons)
4. Transformation en documents JSON
5. Insertion automatisée dans MongoDB

## Tests

Des tests automatisés vérifient la cohérence entre le CSV et MongoDB.

## CRUD

Les opérations CRUD sont réalisées via des scripts Python.

## Sécurité et Rôles

admin_user droit de lecture et d'ecriture pour le script de migration
viewer: Droit de lecture seule
dataengineer: lecture et ecriture

## Execution Docker

docker compose up -d

## initialiser les utilisateurs

docker exec -it mongodb_container mongosh -u root -p rootpassword --eval "
db = db.getSiblingDB('MedicalDB');
db.createUser({user: 'admin_user', pwd: 'adminpassword', roles: [{role: 'readWrite', db: 'MedicalDB'}]});
db.createUser({user: 'viewer', pwd: 'viewerpassword', roles: [{role: 'read', db: 'MedicalDB'}]});
db.createUser({user: 'userdeveloper', pwd: 'devpassword', roles: [{role: 'readWrite', db: 'MedicalDB'}]});
"

## lancement de la migration

docker compose up --build migration_app

## Test et verification :

docker exec -it mongodb_container mongosh -u viewer -p viewerpassword --authenticationDatabase MedicalDB MedicalDB --eval "db.patients.countDocuments()"
