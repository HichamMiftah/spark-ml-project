# Guide d'Exécution du Projet d'Optimisation Énergétique

## Prérequis
1. Assurez-vous que Docker et Docker Compose sont installés
2. Clonez le dépôt :
   ```bash
   git clone https://github.com/HichamMiftah/spark-ml-project.git
   cd spark-ml-project
   ```

## Démarrage de l'Environnement
```bash
# Démarrer les services requis
docker-compose up -d kafka jupyter

# Attendre que les services soient prêts (environ 30 secondes)
docker-compose ps
```

---

## Objectif 1 : Identifier des opportunités d'optimisation énergétique
> Identification des opportunités d'optimisation énergétique par surveillance en temps réel

### Lancement de l'Analyse
```bash
# Démarrer l'analyse d'optimisation énergétique
docker-compose exec jupyter python work/scripts/energy_optimization_analysis.py
```

### Points à Observer
- Surveiller la sortie console pour :
  ```
  +------------------+------------+-----------------+
  | window           | building_id| avg_consumption |
  +------------------+------------+-----------------+
  ```
- L'analyse montrera :
  - Périodes de consommation de pointe
  - Corrélations avec la température
  - Modèles d'occupation

---

## Objectif 2 : Proposer des recommandations basées sur l'analyse
> Fournir des recommandations basées sur les résultats de l'analyse

### Visualisation des Recommandations
```bash
# Les recommandations font partie de la sortie d'analyse
# Elles apparaîtront dans la console comme :
```
Exemple de sortie :
```
+------------------+------------------+
| situation        | recommendation   |
+------------------+------------------+
| Heures de Pointe | 1) Ajuster HVAC |
|                  | 2) Planifier    |
+------------------+------------------+
```

### Types de Recommandations
1. **Heures de Pointe (9h - 17h)**
   ```bash
   # Rechercher les entrées avec :
   "Consommation élevée pendant les heures de pointe : 1) Ajuster les paramètres HVAC..."
   ```

2. **Basées sur la Température**
   ```bash
   # Rechercher les entrées avec :
   "Consommation élevée avec température élevée : 1) Optimiser le système de refroidissement..."
   ```

3. **Basées sur l'Occupation**
   ```bash
   # Rechercher les entrées avec :
   "Consommation élevée avec faible occupation : 1) Installer des capteurs de mouvement..."
   ```

---

## Objectif 3 : Simuler la provenance de données en temps réel
> Simulation de données en temps réel utilisant Apache Kafka et Spark Streaming

### 1. Démarrer la Génération de Données
```bash
# Exécuter le générateur de données
docker-compose exec -d jupyter python work/scripts/energy_data_generator.py
```

### 2. Visualiser le Flux de Données Brutes
```bash
# Surveiller les messages Kafka
docker-compose exec kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic energy_data --from-beginning
```

### 3. Surveiller le Système Complet
```bash
# Terminal 1 - Données brutes
docker-compose exec kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic energy_data

# Terminal 2 - Analyse et recommandations
docker-compose exec jupyter python work/scripts/energy_optimization_analysis.py
```

---

## Outils d'Analyse Supplémentaires

### Interface Jupyter Lab
1. Accéder à Jupyter Lab :
   - Ouvrir le navigateur : http://localhost:8888
   - Token : admin

2. Naviguer vers le répertoire work :
   - Les scripts se trouvent dans le dossier `scripts`
   - Les notebooks d'analyse peuvent être créés ici

### Outils de Surveillance
```bash
# Vérifier l'état des services
docker-compose ps

# Voir les logs des services
docker-compose logs -f jupyter
docker-compose logs -f kafka
```

### Arrêt du Système
```bash
# Arrêter tous les services
docker-compose down

# Pour supprimer aussi les volumes
docker-compose down -v
```

## Dépannage

### Si le Générateur de Données ne Fonctionne Pas
```bash
# Redémarrer le générateur de données
docker-compose restart jupyter
docker-compose exec -d jupyter python work/scripts/energy_data_generator.py
```

### Si l'Analyse ne s'Affiche Pas
```bash
# Vérifier les topics Kafka
docker-compose exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092

# Redémarrer l'analyse
docker-compose exec jupyter python work/scripts/energy_optimization_analysis.py
```

### Problèmes Courants
1. **Pas de Flux de Données**
   ```bash
   # Vérifier que le topic Kafka existe
   docker-compose exec kafka kafka-topics.sh --describe --topic energy_data --bootstrap-server localhost:9092
   ```

2. **Erreurs d'Analyse**
   ```bash
   # Vérifier les dépendances Python
   docker-compose exec jupyter pip list | grep -E "kafka-python|pyspark"
   ```

3. **Santé des Services**
   ```bash
   # Vérifier la santé des services
   docker-compose ps
   ```
