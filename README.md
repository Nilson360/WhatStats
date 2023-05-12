# WhatStats V1

# Analyse des messages WhatsApp

Ce dépôt Git contient un code Python qui permet d'analyser les messages exportés à partir de WhatsApp. Le code extrait les noms
des participants, compte le nombre de messages pour chaque participant et génère un graphique représentant les 30 principaux
participants en fonction du nombre de messages.

## Instructions d'utilisation

1. Assurez-vous d'avoir Python installé sur votre système.

2. Clonez ce dépôt Git sur votre machine locale en utilisant la commande suivante :

   ```
   git clone https://github.com/votre-utilisateur/nom-du-depot.git
   ```

3. Placez le fichier de données WhatsApp exporté dans le même répertoire que le code Python. Assurez-vous de spécifier le
 chemin d'accès complet du fichier dans la variable `file_path` à la ligne 7 du fichier `main.py`.

4. Exécutez le fichier `main.py` à l'aide de la commande suivante :

   ```
   python main.py
   ```

5. Le graphique contenant les 30 principaux participants sera généré et s'affichera à l'écran.

## Dépendances

Le code utilise les dépendances suivantes :

- `re`: Une bibliothèque Python pour le traitement des expressions régulières.
- `matplotlib`: Une bibliothèque Python pour la création de graphiques.

Assurez-vous d'installer ces dépendances en utilisant la commande suivante :

```
pip install matplotlib
```

## Avertissement

Veuillez noter que ce code a été conçu pour traiter des fichiers de données WhatsApp spécifiques et utilise une expression 
régulière pour extraire les informations pertinentes. Si le format de vos données est différent, vous devrez peut-être adapter 
le code en conséquence.

## Contribuer

Les contributions à ce projet sont les bienvenues. Si vous souhaitez apporter des améliorations, veuillez suivre les étapes suivantes :

1. Fork ce dépôt Git.

2. Créez une branche pour vos modifications :

   ```
   git checkout -b ameliorations
   ```

3. Faites les modifications souhaitées et committez-les :

   ```
   git commit -m "Description des modifications"
   ```

4. Poussez les modifications vers votre fork :

   ```
   git push origin ameliorations
   ```

5. Ouvrez une pull request vers ce dépôt d'origine.

6. Attendez la revue de code et l'approbation avant de fusionner les modifications.

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.
---
C'est tout ! Profitez de l'analyse de vos messages WhatsApp et n'hésitez pas à contribuer si vous le souhaitez.
