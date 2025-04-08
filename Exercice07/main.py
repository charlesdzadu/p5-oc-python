def square(number):
    """Calcule le carré d'un nombre.

    Args:
        number: Le nombre dont on veut calculer le carré (int ou float)

    Returns:
        float ou int: Le carré du nombre
        None: Si le paramètre n'est pas un nombre
    """
    if not isinstance(number, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return number * number


# Test de la fonction
if __name__ == "__main__":
    # Test avec un nombre entier
    resultat1 = square(5)
    print(f"Le carré de 5 est : {resultat1}")

    # Test avec un nombre décimal
    resultat2 = square(2.5)
    print(f"Le carré de 2.5 est : {resultat2}")

    # Test avec une chaîne de caractères (erreur attendue)
    resultat3 = square("test")
    print(f"Le résultat avec 'test' est : {resultat3}")

    # Test avec une liste (erreur attendue)
    resultat4 = square([1, 2, 3])
    print(f"Le résultat avec [1, 2, 3] est : {resultat4}")
