import os
import shutil
from time import sleep

# Configuration
USB_NAME = "WINSETUP"  # Nom de la clé USB
DESTINATION_DIR = r"C:\Users\HP\Desktop\kevin"  # Répertoire de destination

def find_usb_drive():
    """Trouve le lecteur de la clé USB"""
    for drive in range(ord('A'), ord('Z') + 1):
        drive_letter = chr(drive) + ":"
        usb_path = os.path.join(drive_letter, os.sep)
        if os.path.exists(usb_path):
            volume_name = get_volume_name(drive_letter)
            if volume_name and USB_NAME in volume_name:
                return usb_path
    return None

def get_volume_name(drive_letter):
    """Récupère le nom du volume d'un lecteur"""
    try:
        import win32api
        return win32api.GetVolumeInformation(drive_letter + os.sep)[0]
    except ImportError:
        # Fallback si win32api n'est pas installé
        return None

def copy_usb_contents(usb_path, dest_dir):
    """Copie récursivement le contenu de la clé USB"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for item in os.listdir(usb_path):
        src = os.path.join(usb_path, item)
        dest = os.path.join(dest_dir, item)
        
        try:
            if os.path.isdir(src):
                shutil.copytree(src, dest, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dest)
            print(f"Copié : {src} -> {dest}")
        except Exception as e:
            print(f"Erreur lors de la copie de {src}: {e}")

if __name__ == "__main__":
    print(f"Recherche de la clé USB '{USB_NAME}'...")
    
    while True:
        usb_path = find_usb_drive()
        if usb_path:
            print(f"Clé USB trouvée sur {usb_path}")
            print("Début de la copie...")
            copy_usb_contents(usb_path, DESTINATION_DIR)
            print("Copie terminée avec succès !")
            break
        else:
            print("Clé USB non détectée. Nouvelle tentative dans 5 secondes...")
            sleep(5)