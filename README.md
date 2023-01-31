# drug-analysis
## Partie 1 - Python et Data Engineering

`Objectif:` Générer un graphe de liason entre un ensemble de drugs et leurs apparitions dans différentes sources de type article scientifique.

### Solution proposée
`À propos:`
La solution proposé se découpe par taches de type `Task` placés dans une liste. Chaque taches est appelée à la chaine à l'image d'une pipeline.
Toutes les taches prennnent en entrée le résultat de la tache précédente, puis une terminé elle renvoie le résultat de son propre traitement.

L'ensemble des paramètres du projet (path et format) sont stockés dans `config/config.yaml` afin que chacun puisse avoir
les infos clés du projet facilement.

`Éxecutions:` À executer depuis la racine du projet


Installation des package python : 
``` shell
python3 -m venv pipeline_env
source pipeline_env/bin/activate
pip install -r config/requirements.txt
  ```

Lancement de la pipeline (résultat dans /data/result)
``` shell
python3 ./pipeline_main.py
 ```

Test 
``` shell
pytest ./test
```

Ad-hoc
``` shell
python3 ./ad-hoc.py
```

Le dossier test contient un script de test executable depuis la racine du projet avec `pytest

`Architecture:`
```
.
    /config :
        config.yaml : decriptif de tout les paramètre utile au projet (path des dossier/fichier important, format des données des dataset et format d'affichage du logger
        requirements.txt : package python requis 
    /data : contient les données à partir de la source jusqu'au graph de laison final
    /src:
        /task : Ensemble de classes qui von être appelé dans la pipeline. Ils héritent tous de la classe Task (abstract class) pour avoir un format uniforme
        /tools : Diver outils utilisé communémant dans les tasks
    /test:
        /sample: exmeple de data utiles pour les tests
        /script: dossier qui contient les scripts de test
    
    pipeline_main.py : fichier à executer depuis la racine du projet pour lancer le process
    ad-hoc.py : Script de réccurération du journal avec le plus de citation

        
```

`Piste:`
- Changer le format du stockage des données par un système de stockage plus performant (S3, HDFS, MongoDB,...)
- Approfondir les tests à l'ensemble des class du projet
- Mettre en place un système d'exception personnalisé
- Containerisé la solution
- Dans un cas plutôt real-time, placer chaque tache dans worker relié à une fil d'attente de message (Kakfa, RabbitMQ)


## Partie 2 - SQL

### Première Question
`Énoncé :` Trouver le chiffre d’affaires (le montant total des ventes), jour par jour, du 1er janvier 2019 au 31 décembre 2019. Le résultat sera trié sur la date à laquelle la commande a été passée

`Postulat:` Je pars du principe que la colonne `date` dans la table `TRANSACTION` est enregistré au format `VARCHAR`

`Solution:`
``` SQL
    SELECT T.date, SUM(T.prod_price * T.prod_qty) AS ventes
    FROM TRANSACTION AS T
    WHERE TO_DATE(T.date, 'DD/MON/YYYY') BETWEEN TO_DATE('01/01/2019', 'DD/MON/YYYY') AND TO_DATE('31/12/2019', 'DD/MON/YYYY') 
    GROUP BY T.date
    ORDER BY T.date;
```


### Deuxième Question
`Énoncé :` Déterminer, par client et sur la période allant du 1er janvier 2019 au 31 décembre 2019, les ventes meuble et déco réalisées

`Postulat:` Je pars du principe que la colonne `date` dans la table `TRANSACTION` est enregistré au format `VARCHAR`

`Solution:`
``` SQL
    SELECT T.client_id,
        SUM(CASE WHEN PN.product_type = "MEUBLE" THEN T.prod_price * T.prod_qty ) AS ventes_meuble,
        SUM(CASE WHEN PN.product_type = "DECO" THEN T.prod_price * T.prod_qty) AS ventes_deco
    FROM TRANSACTION AS T
    JOIN PRODUCT_NOMENCLATURE AS PN ON T.prop_id = PN.product_id
    WHERE TO_DATE(T.date, 'DD/MON/YYYY') BETWEEN TO_DATE('01/01/2019', 'DD/MON/YYYY') AND TO_DATE('31/12/2019', 'DD/MON/YYYY')
    GROUP BY T.client_id
```
