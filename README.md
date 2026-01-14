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

## Exécution

```bash
python3 src/migrate.py
```
