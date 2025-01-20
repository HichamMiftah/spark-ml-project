# Projet d'Optimisation Énergétique avec Spark ML

Ce projet utilise Apache Spark, Kafka et le Machine Learning pour analyser et optimiser la consommation d'énergie en temps réel.

## Prérequis
- Docker et Docker Compose
- Python 3.8+
- PySpark 3.5.0
- Kafka-Python

## Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/HichamMiftah/spark-ml-project.git
   cd spark-ml-project
   ```

2. Construire et démarrer les conteneurs :
   ```bash
   docker-compose up -d
   ```

## Structure du Projet
```
spark-ml-project/
│
├── docker/                  # Fichiers Docker
├── notebooks/              # Notebooks Jupyter
├── scripts/               # Scripts Python
│   ├── energy_data_generator.py
│   └── energy_optimization_analysis.py
├── docker-compose.yml    # Configuration Docker Compose
└── README.md
```

## Services

### Jupyter Lab
- Interface de développement interactive
- Accessible sur http://localhost:8888
- Token : `admin`

### Apache Spark
- Traitement des données en temps réel
- Interface Web Spark sur http://localhost:8080

### Apache Kafka
- Streaming de données en temps réel
- Port : 9092

## Utilisation

1. Accéder à Jupyter Lab :
   - Ouvrir http://localhost:8888
   - Utiliser le token : `admin`

2. Exécuter les scripts :
   ```bash
   # Générer des données
   python scripts/energy_data_generator.py

   # Lancer l'analyse
   python scripts/energy_optimization_analysis.py
   ```

## Test du Projet

### Utilisation de Jupyter Notebook
Nous fournissons un notebook complet pour tester tous les aspects du projet :

1. Accès à Jupyter Lab :
   ```bash
   # Le notebook est disponible sur http://localhost:8888
   # Token : admin
   ```

2. Naviguer vers `notebooks/energy_optimization_test.ipynb`

3. Tester chaque objectif :
   - Objectif 1 : Identification des optimisations énergétiques
   - Objectif 2 : Recommandations automatisées
   - Objectif 3 : Simulation de données en temps réel

### Scénarios de Test
Le notebook inclut divers scénarios de test :
- Consommation en heures de pointe (9h-17h)
- Scénarios de température élevée
- Situations de faible occupation
- Simulation de données en temps réel

### Documentation
Pour plus d'informations détaillées, voir :
- `run.md` : Instructions d'exécution détaillées
- `presentation.md` : Présentation du projet et détails d'implémentation

## Objectifs du Projet

1. **Identifier des opportunités d'optimisation énergétique**
   - Surveillance en temps réel de la consommation d'énergie
   - Détection des heures de pointe (9h-17h)
   - Analyse de corrélation avec la température
   - Reconnaissance des modèles d'occupation

2. **Proposer des recommandations**
   - Suggestions d'optimisation HVAC
   - Gestion de charge en heures de pointe
   - Recommandations basées sur la température
   - Conseils d'économie d'énergie basés sur l'occupation

3. **Simuler la provenance de données en temps réels**
   - Streaming de données en temps réel avec Kafka
   - Génération de données aléatoires avec motifs réalistes
   - Simulation de plusieurs bâtiments
   - Diverses conditions environnementales

## Notes
- Le token Jupyter Lab est : `admin`
- Le Worker Spark est configuré avec 1G de mémoire et 1 cœur
