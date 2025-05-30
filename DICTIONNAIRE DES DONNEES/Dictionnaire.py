import sys
from itertools import permutations

def generate_combinations(nom, prenom, date_naissance):
    # Extraire les composants de la date
    try:
        annee, mois, jour = date_naissance.split("-")
    except ValueError:
        print("\n❌ Format de date incorrect! Utilisez YYYY-MM-DD (ex: 1990-05-15)")
        sys.exit(1)

    date_variants = [annee, mois, jour, annee[2:], mois + jour, jour + mois]

    # Générer des combinaisons
    combinations = []
    combinations.extend([
        prenom + annee,              # Jean1990
        prenom + jour + mois,        # Jean1505
        prenom[0] + nom + annee[2:],  # JDupont90
        nom + mois,                  # Dupont05
        nom[::-1] + jour,            # tnopuD15
        prenom.lower() + "_" + annee, # jean_1990
        nom.upper() + jour,          # DUPONT15
        prenom + "@" + jour,         # jean@15
        nom + prenom[0] + annee[2:], # DupontJ90
    ])

    # Ajouter des permutations avec symboles
    symbols = ["!", "@", "#", "$", "%", "&", "*", "123", "2023"]
    for combo in combinations.copy():
        for symbol in symbols:
            combinations.append(combo + symbol)
            combinations.append(symbol + combo)  # Ajout en préfixe aussi

    return list(set(combinations))  # Éliminer les doublons

def main():
    print("\n=== Générateur de Dictionnaire Personnalisé ===")
    print("Veuillez entrer les informations suivantes :\n")
    
    nom = input("Nom de famille : ").strip()
    prenom = input("Prénom : ").strip()
    date_naissance = input("Date de naissance (YYYY-MM-DD) : ").strip()

    if not nom or not prenom or not date_naissance:
        print("\n❌ Erreur : Tous les champs doivent être remplis!")
        sys.exit(1)

    passwords = generate_combinations(nom, prenom, date_naissance)
    
    with open("custom_dict.txt", "w") as f:
        for pwd in passwords:
            f.write(pwd + "\n")
    
    print(f"\n✅ Dictionnaire généré avec {len(passwords)} mots de passe → 'custom_dict.txt'")

if __name__ == "__main__":
    main()
