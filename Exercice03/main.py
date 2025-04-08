# Liste de mots initiale
mots = ["openclassrooms", "developpeur", "algorithme"]

# Fonction pour compter les voyelles dans un mot
def compter_voyelles(mot):
    voyelles = "aeiou"
    total = 0
    for lettre in mot:
        if lettre in voyelles:
            total += 1
    return total

# Liste de compréhension qui crée des tuples (mot, nombre_de_voyelles)
resultat = [(mot, compter_voyelles(mot)) for mot in mots]

# Affichage du résultat
print(resultat)
