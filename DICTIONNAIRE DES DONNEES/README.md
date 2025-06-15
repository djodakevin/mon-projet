# 🔐 Générateur de Dictionnaire Personnalisé

Ce script Python permet de générer automatiquement un dictionnaire de mots de passe personnalisés à partir du **nom**, **prénom** et **date de naissance** d'une personne. Il est utile dans des contextes de tests de sécurité ou pour créer des dictionnaires adaptés à une cible spécifique (ex: test de robustesse de mots de passe).

## 🧰 Fonctionnalités

- Génère des combinaisons basées sur :
  - Nom et prénom
  - Date de naissance (année, mois, jour, formats abrégés)
  - Miroirs de noms, majuscules, minuscules
  - Inclusion de symboles courants (`!`, `@`, `#`, etc.)
- Génère automatiquement un fichier `custom_dict.txt` contenant toutes les combinaisons uniques

## 📦 Prérequis

- Python 3.x

Aucune bibliothèque externe requise.

## ▶️ Utilisation

python Dictionnaire.py
