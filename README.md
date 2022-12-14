<p align="center">
    <img src="https://user-images.githubusercontent.com/106987975/192334994-3ebfe092-8481-4d7c-9f46-bf7065d76a74.jpg" height="200">
</p>

<p align="center">
    <a href="#stars">
        <img alt="Étoiles sur GitHub | GitHub Repo stars" src="https://img.shields.io/github/stars/asc-csa/open-data-metadata-analysis">
    </a>
    <a href="#watchers">
        <img alt="Spectateurs sur Github | GitHub watchers" src="https://img.shields.io/github/watchers/asc-csa/open-data-metadata-analysis">
    </a>
    <a href="https://github.com/asc-csa/radarsat1-scripts/commits/main">
        <img alt="Dernier commit sur GitHub | GitHub last commit" src="https://img.shields.io/github/last-commit/asc-csa/open-data-metadata-analysis">
    </a>
    <a href="https://github.com/asc-csa/radarsat1-scripts/graphs/contributors">
        <img alt="Contributeurs sur GitHub | GitHub contributors" src="https://img.shields.io/github/contributors/asc-csa/open-data-metadata-analysis">
    </a>
    <a href="https://twitter.com/intent/follow?screen_name=csa_asc">
        <img alt="Suivre sur Twitter | Twitter Follow" src="https://img.shields.io/twitter/follow/csa_asc?style=social">
    </a>
</p>


# open-data-metadata-analysis

## Contexte

Le nouveau portail de données ouvertes d’ASC, lancé en 2021, permet un meilleur accès aux métadonnées sur le back-end. Les métadonnées de l'ASC comprennent, sans s'y limiter, des informations telles que le nom de l'ensemble de données en anglais et en français, le nom du gestionnaire de données, les ressources, l'organisation des données par projet, direction et division, le nombre de vues et la date de publication. Ce script analyse les métadonnées des ensembles de données ouverts et des ressources pour éclairer les décisions futures liées aux données.

## Exécution du script

1.	Installez les prérequis contenus dans requirements.txt
```
pip install -r requirements.txt
```
2.	Exécutez le script avec la commande suivante
```
python main.py
```

## Comportements attendus
Le script produit les fichiers et la sortie suivants:

- Graphique du nombre d'ensembles de données dans chaque projet enregistré par la date 
- Graphique du nombre d'ensembles de données dans chaque division enregistré par la date 
- Graphique du nombre d'ensembles de données dans chaque direction enregistré par la date 
-	Graphique du nombre d'ensembles de données scientifiques dans chaque division enregistré par la date 
-	Graphique du nombre d'ensembles de données de gestion dans chaque division enregistré par la date 
-	Graphique du nombre d'ensembles de données scientifiques dans chaque direction enregistré par la date 
-	Graphique du nombre d'ensembles de données de gestion dans chaque direction enregistré par la date 
-	Graphique du nombre d'ensembles de données publiés chaque année enregistrés par la date 
-	Liste des directions et divisions qui n'ont pas d'ensembles de données 
-	Tableau du nombre d'ensembles de données dans chaque projet enregistré par la date 
-	Tableau du nombre d'ensembles de données dans chaque division enregistré par la date 
-	Tableau du nombre d'ensembles de données dans chaque direction enregistré par la date 
-	Fichier CSV de tous les ensembles de données avec toutes les variables correspondantes 
-	Graphique des ensembles de données avec des vues supérieures à 30 
-	CSV d'ensembles de données avec moins de 30 vues
- CSV avec gestionnaires de données
- Graphique du nombre de ressources dans chaque projet enregistré par date
- Graphique du nombre de ressources dans chaque division enregistrées par date
- Graphique du nombre de ressources dans chaque direction enregistrées par date
- Tableau du nombre de ressources dans chaque projet enregistré par date
- Tableau du nombre de ressources dans chaque division enregistrées par date
- Tableau du nombre de ressources dans chaque direction sauvegardées par date
- Nuage de mots de description anglaise des jeux de données
- Nuage de mots des titres des ensembles de données en anglais

## About

The new CSA open data portal, launched in 2021, allows better access to metadata on the backend. The CSA metadata includes, but is not limited to, information such as dataset name in English and French, data steward name, resources, organization of data by project, directorate, and division, number of views, and publication date. This script analyzes metadata from the open datasets and resources to inform data-related decisions in the future.

## Run the Script

1.	Install requirements from the requirments.txt file
```
pip install -r requirements.txt
```
2.	Run the script using the following command
```
python main.py
```

## Expected Behaviour

The script should produce the following files and output:
-	Graph of number of datasets in each project saved by date
-	Graph of number of datasets in each division saved by date
-	Graph of number of datasets in each directorate saved by date
-	Graph of number of science datasets in each division saved by date
-	Graph of number of management datasets in each division saved by date
-	Graph of number of science datasets in each directorate saved by date
-	Graph of number of management datasets in each directorate saved by date
-	Graph of number of datasets published in each year saved by date
-	List of directorate and divisions that do not have datasets
-	Table of number of datasets in each project saved by date
-	Table of number of datasets in each division saved by date
-	Table of number of datasets in each directorate saved by date
-	CSV file of all datasets with all corresponding variables
-	Graph of datasets with views above 30
-	CSV of datasets with views less than 30
- CSV with data stewards
- Graph of number of resources in each project saved by date
-	Graph of number of resources in each division saved by date
-	Graph of number of resources in each directorate saved by date
-	Table of number of resources in each project saved by date
-	Table of number of resources in each division saved by date
-	Table of number of resources in each directorate saved by date
-	Word cloud of English description of datasets
-	Word cloud of English dataset titles
