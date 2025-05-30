import os
import shutil
from time import sleep
import ctypes  # Pour la notification Windows

# Configuration
SOURCE_DIR = r"C:\Users\HP\Desktop\KALI"  # Répertoire source
USB_NAME = "WINSETUP"                      # Nom de la clé USB cible

def show_notification(title, message):
    """Affiche une notification Windows"""
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)  # 0x40 = Icône d'information

def find_usb_drive():
    """Trouve le lecteur de la clé USB par son nom"""
    for drive in range(ord('A'), ord('Z') + 1):
        drive_letter = chr(drive) + ":"
        if os.path.exists(drive_letter):
            try:
                import win32api
                vol_name = win32api.GetVolumeInformation(drive_letter + os.sep)[0]
                if vol_name and USB_NAME in vol_name:
                    return drive_letter + "\\"
            except ImportError:
                # Méthode alternative sans win32api
                if os.path.exists(os.path.join(drive_letter, "WINSETUP.tag")):
                    return drive_letter + "\\"
    return None

def copy_to_usb(source, usb_path):
    """Copie récursive du répertoire source vers la clé USB"""
    total_files = 0
    for root, dirs, files in os.walk(source):
        total_files += len(files)
    
    copied_files = 0
    errors = 0
    
    for item in os.listdir(source):
        src = os.path.join(source, item)
        dest = os.path.join(usb_path, item)
        
        try:
            if os.path.isdir(src):
                shutil.copytree(src, dest, dirs_exist_ok=True)
                copied_files += len([f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f))])
            else:
                shutil.copy2(src, dest)
                copied_files += 1
            print(f"✓ {src} → {dest}")
        except Exception as e:
            print(f"✗ Erreur sur {src}: {str(e)}")
            errors += 1
    
    return total_files, copied_files, errors

if __name__ == "__main__":
    print(f"🔍 Recherche de la clé USB '{USB_NAME}'...")
    
    try:
        while True:
            usb_drive = find_usb_drive()
            if usb_drive:
                print(f"✅ Clé trouvée sur {usb_drive}")
                print("🔄 Début de la copie...")
                
                # Vérifie si le répertoire source existe
                if not os.path.exists(SOURCE_DIR):
                    print(f"❌ Erreur: Le répertoire source {SOURCE_DIR} n'existe pas")
                    show_notification("Erreur", f"Le répertoire {SOURCE_DIR} est introuvable")
                    break
                
                # Crée le répertoire sur la clé si nécessaire
                if not os.path.exists(usb_drive):
                    os.makedirs(usb_drive)
                
                total, success, errors = copy_to_usb(SOURCE_DIR, usb_drive)
                
                # Message final détaillé
                result_msg = (
                    f"📊 Résultat de la copie :\n"
                    f"• Fichiers à copier : {total}\n"
                    f"• Fichiers copiés : {success}\n"
                    f"• Erreurs : {errors}\n"
                    f"• Répertoire source : {SOURCE_DIR}\n"
                    f"• Destination : {usb_drive}"
                )
                
                print("\n" + "="*50)
                print("✅ COPIE TERMINÉE AVEC SUCCÈS")
                print(result_msg)
                print("="*50)
                
                # Notification Windows
                show_notification("Copie terminée", 
                    f"La copie de {SOURCE_DIR} vers {usb_drive} est terminée\n"
                    f"{success} fichiers copiés, {errors} erreurs")
                break
            else:
                print("⏳ Clé non détectée. Nouvelle tentative dans 5 secondes... (Ctrl+C pour quitter)")
                sleep(5)
    
    except KeyboardInterrupt:
        print("\n🛑 Opération annulée par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur inattendue : {str(e)}")
        show_notification("Erreur", f"Une erreur est survenue : {str(e)}")