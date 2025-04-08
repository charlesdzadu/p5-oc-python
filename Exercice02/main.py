# Dictionnaire contenant les informations des étudiants et leurs notes
etudiants = {
    "Alice": {
        "Mathématiques": 15,
        "Physique": 14,
        "Informatique": 16
    },
    "Bob": {
        "Mathématiques": 13,
        "Physique": 12,
        "Informatique": 15
    },
    "Charlie": {
        "Mathématiques": 17,
        "Physique": 16,
        "Informatique": 18
    }
}

# Demander le nom de l'étudiant
nom_etudiant = input("Entrez le nom de l'étudiant : ")

# Vérifier si l'étudiant existe dans le dictionnaire
if nom_etudiant in etudiants:
    # Afficher l'en-tête avec le nom de l'étudiant
    print(f"Notes de {nom_etudiant} : ")
    
    # Afficher les notes pour chaque matière
    for matiere, note in etudiants[nom_etudiant].items():
        print(f"{matiere} : {note}")
    
    # Calculer et afficher la moyenne
    notes = etudiants[nom_etudiant].values()
    moyenne = sum(notes) / len(notes)
    print(f"Moyenne de {nom_etudiant} : {moyenne}")
else:
    # Message si l'étudiant n'existe pas
    print(f"L'étudiant {nom_etudiant} n'existe pas dans la liste.")
