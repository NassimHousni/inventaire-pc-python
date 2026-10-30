# Inventaire de mon PC avec Python

Mon premier projet Python pour apprendre à récupérer des informations
sur un ordinateur et surveiller ses ressources.

## Fonctionnalités

- Afficher le système, sa version et le processeur.
- Afficher la RAM totale et son pourcentage d’utilisation.
- Afficher le pourcentage d’utilisation du disque C:.
- Avertir si le disque dépasse 90 % ou si la RAM dépasse 80 %.
- Enregistrer les résultats dans un rapport texte daté.

## Ce que j’apprends

Utiliser des variables, des conditions et écrire dans un fichier.

## Installation et utilisation sur Windows

Python doit être installé. Dans un terminal PowerShell ouvert dans le dossier du projet :

1. Créer un environnement pour les outils du projet :

   ```powershell
   python -m venv .venv
   ```

2. Installer les outils nécessaires :

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Lancer le script :

   ```powershell
   .\.venv\Scripts\python.exe infos_pc.py
   ```

Le script affiche les résultats et crée `rapport_pc.txt`.
Ce rapport est remplacé à chaque lancement et reste sur le PC grâce au `.gitignore`.

Le script affiche les résultats et crée un rapport dont le nom contient
la date et l’heure, par exemple `rapport_pc_2026-10-30_16-14-01.txt`.

Les anciens rapports sont conservés. Les rapports restent sur le PC
et sont ignorés par Git grâce au fichier `.gitignore`.