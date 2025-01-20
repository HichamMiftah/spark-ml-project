# Implémentation des Objectifs d'Optimisation Énergétique

## 1. Identifier des opportunités d'optimisation énergétique

### Implémentation :
- Création d'un système de surveillance de la consommation d'énergie en temps réel :
  ```python
  def generate_recommendations(df):
      return df.withColumn("recommendations",
          when((col("hour_of_day").between(9, 17)) & (col("avg_consumption") > 150),
              "Consommation élevée pendant les heures de pointe...") \
          .when((col("temperature") > 25) & (col("avg_consumption") > 130),
              "Consommation élevée avec température élevée...") \
          .when((col("occupancy") < 30) & (col("avg_consumption") > 100),
              "Consommation élevée avec faible occupation..."))
  ```

### Fonctionnalités Clés :
1. **Détection des Heures de Pointe**
   - Surveille la consommation entre 9h et 17h
   - Signale les périodes de forte consommation (>150 kWh)

2. **Corrélation avec la Température**
   - Analyse la relation entre température et consommation d'énergie
   - Identifie les modèles de refroidissement inefficaces

3. **Analyse de l'Occupation**
   - Suit la consommation d'énergie par rapport à l'occupation du bâtiment
   - Met en évidence le gaspillage pendant les périodes de faible occupation

## 2. Proposer des recommandations basées sur les résultats de l'analyse

### Implémentation :
```python
def calculate_peak_hours_impact(df):
    return df \
        .withColumn("cost_impact", 
            when(col("is_peak_hour") == "Peak", col("avg_consumption") * 1.5)
            .otherwise(col("avg_consumption"))) \
        .withColumn("potential_savings",
            when(col("is_peak_hour") == "Peak", 
                (col("avg_consumption") * 1.5) - (col("avg_consumption") * 0.8))
            .otherwise(0))
```

### Recommandations Générées :
1. **Optimisation des Heures de Pointe**
   - Ajustements des paramètres HVAC
   - Planification des tâches pour les heures creuses
   - Contrôles d'éclairage automatisés

2. **Recommandations Basées sur la Température**
   - Optimisation du système de refroidissement
   - Installation de protection solaire
   - Stratégies de ventilation naturelle

3. **Solutions Basées sur l'Occupation**
   - Mise en place de capteurs de mouvement
   - Réduction de la charge de base
   - Audit des équipements toujours allumés

## 3. Simuler la provenance de données en temps réels

### Implémentation :
```python
def create_energy_data():
    data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'building_id': random.randint(1, 10),
        'energy_consumption': random.uniform(50, 200),
        'temperature': random.uniform(15, 35),
        'humidity': random.uniform(30, 80),
        'occupancy': random.randint(0, 100)
    }
    return data
```

### Stack Technologique :
1. **Apache Kafka**
   - Streaming de données en temps réel
   - File d'attente de messages
   - Distribution des données

2. **Apache Spark Streaming**
   - Traitement des données en temps réel
   - Analyses basées sur des fenêtres temporelles
   - Recommandations continues

### Flux de Données :
1. Générateur de Données → Topic Kafka
2. Spark Streaming ← Topic Kafka
3. Analyse & Recommandations
4. Stockage dans HDFS

## Résultats et Visualisation

### Surveillance en Temps Réel :
- Accès Jupyter Lab : http://localhost:8888 (token : admin)
- Visualisation des flux de données en direct
- Suivi des recommandations

### Sortie d'Analyse :
```
+------------------+------------+-----------------+------------------+
| fenêtre          | building_id| avg_consumption | recommendations  |
+------------------+------------+-----------------+------------------+
| 2025-01-20 14:55 |     1     |     175.5      | Consommation    |
| 2025-01-20 15:00 |     2     |     120.3      | Niveaux normaux |
+------------------+------------+-----------------+------------------+
```

## Test de l'Implémentation

1. **Visualiser les Données Brutes** :
   ```bash
   docker-compose exec kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic energy_data
   ```

2. **Surveiller l'Analyse** :
   ```bash
   docker-compose exec jupyter python work/scripts/energy_optimization_analysis.py
   ```

3. **Accéder aux Résultats** :
   - Sortie console en temps réel
   - Stockage HDFS pour analyse historique
   - Notebooks Jupyter pour analyse personnalisée
