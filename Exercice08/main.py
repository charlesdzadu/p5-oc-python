def log_decorator(func):
    """Décorateur qui affiche des messages avant et après l'exécution d'une fonction.

    Args:
        func: La fonction à décorer (doit être sans arguments)

    Returns:
        function: La fonction décorée
    """
    def wrapper():
        print(f"Début de l'exécution de la fonction {func.__name__}")
        result = func()
        print(f"Fin de l'exécution de la fonction {func.__name__}")
        return result
    return wrapper


@log_decorator
def dire_bonjour():
    """Fonction simple qui affiche un message de salutation."""
    print("Bonjour !")


@log_decorator
def calculer_nombre():
    """Fonction simple qui retourne un nombre."""
    return 42


# Test des fonctions décorées
if __name__ == "__main__":
    print("Test de la première fonction :")
    dire_bonjour()
    
    print("\nTest de la deuxième fonction :")
    resultat = calculer_nombre()
    print(f"Résultat retourné : {resultat}")
