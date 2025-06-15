🔐Copieur Automatique de Clé USB (usb_copier.py)

🎯 Objectif
Détecter automatiquement une clé USB donnée (par nom de volume) et en copier tout le contenu dans un répertoire prédéfini sur le système.

🧰 Fonctionnalités
Recherche en boucle la clé USB nommée "WINSETUP" (modifiable)

Copie récursive de tous les fichiers et dossiers

Création automatique du dossier de destination

Gestion des erreurs et affichage des fichiers copiés

⚙️ Prérequis
Windows uniquement

Python 3.x

Module pywin32 :

bash
   pip install pywin32
📝 Configuration
python
 USB_NAME = "WINSETUP"
 DESTINATION_DIR = r"C:\Users\HP\Desktop\kevin"
Changer les valeurs selon le nom réel de la clé USB et l’emplacement voulu.

▶️ Utilisation
bash
     python usb_copier.py
Le script attend que la clé soit insérée, puis lance la copie automatique.
