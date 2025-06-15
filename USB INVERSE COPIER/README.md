🎯 Objectif
Ce script détecte automatiquement une clé USB cible par son nom de volume (ex: WINSETUP) et copie dans celle-ci tout le contenu d’un dossier local (ex: C:\Users\HP\Desktop\KALI). C’est l’inverse du comportement d’un copieur classique.

Il est utile pour :

L’automatisation de transferts de données sur clé

La préparation de clés USB avec des fichiers spécifiques

Des démonstrations ou tests de scripts d’exfiltration autorisée

🧰 Fonctionnalités
📦 Copie récursive de tout le contenu d’un dossier local vers la clé USB

🔍 Recherche continue de la clé USB par son nom de volume

✅ Création du répertoire sur la clé si nécessaire

🪟 Affichage de notifications Windows (via ctypes)

📊 Affichage d’un rapport de copie : total, succès, erreurs

🧯 Gestion des erreurs et interruptions utilisateur (Ctrl+C)

⚙️ Prérequis
Système : Windows

Python 3.x

Module Python requis : pywin32

Installer les dépendances :
bash
pip install pywin32
📌 Si pywin32 est absent, le script utilisera une méthode alternative via un fichier .tag (non obligatoire).

📝 Configuration
Modifie ces deux lignes selon tes besoins :

python
SOURCE_DIR = r"C:\Users\HP\Desktop\KALI"  # Dossier à copier
USB_NAME = "WINSETUP"                     # Nom de la clé USB cible
▶️ Utilisation
Branche la clé USB et vérifie que son nom de volume est WINSETUP.

Place les fichiers à transférer dans le dossier spécifié (SOURCE_DIR).

Lance le script :

bash
python usb_Inversecopier.py
Le script détectera la clé automatiquement et démarrera la copie.
