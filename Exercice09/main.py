class Rectangle:
    """Classe représentant un rectangle avec une largeur et une longueur."""

    def __init__(self, width, length):
        """Initialise un nouveau rectangle.

        Args:
            width (float): La largeur du rectangle
            length (float): La longueur du rectangle
        """
        self.width = width
        self.length = length

    def calculate_area(self):
        """Calcule l'aire du rectangle.

        Returns:
            float: L'aire du rectangle (largeur * longueur)
        """
        return self.width * self.length

    def calculate_perimeter(self):
        """Calcule le périmètre du rectangle.

        Returns:
            float: Le périmètre du rectangle (2 * (largeur + longueur))
        """
        return 2 * (self.width + self.length)


# Test de la classe Rectangle
if __name__ == "__main__":
    # Création d'un rectangle de largeur 5 et de longueur 3
    rectangle = Rectangle(5, 3)

    # Calcul et affichage de l'aire
    aire = rectangle.calculate_area()
    print(f"L'aire du rectangle est : {aire}")

    # Calcul et affichage du périmètre
    perimetre = rectangle.calculate_perimeter()
    print(f"Le périmètre du rectangle est : {perimetre}")

    # Test avec un autre rectangle
    grand_rectangle = Rectangle(10, 7)
    print(f"\nPour un grand rectangle de 10x7 :")
    print(f"Aire : {grand_rectangle.calculate_area()}")
    print(f"Périmètre : {grand_rectangle.calculate_perimeter()}")
