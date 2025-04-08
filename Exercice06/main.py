def calculate_average(numbers):
    """Calcule la moyenne d'une liste de nombres.

    Args:
        numbers (list): Une liste de nombres

    Returns:
        float: La moyenne des nombres de la liste
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Test de la fonction
if __name__ == "__main__":
    # Exemple d'utilisation
    liste_nombres = [10, 20, 30, 40, 50]
    moyenne = calculate_average(liste_nombres)
    print(f"La moyenne des nombres {liste_nombres} est : {moyenne}")

    # Test avec une liste vide
    liste_vide = []
    moyenne_vide = calculate_average(liste_vide)
    print(f"La moyenne d'une liste vide est : {moyenne_vide}")
