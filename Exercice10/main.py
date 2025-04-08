## Écrivez votre code ici !

class Person:
    """Classe représentant une personne avec un nom et un âge."""

    def __init__(self, name, age):
        """Initialise une nouvelle personne.

        Args:
            name (str): Le nom de la personne
            age (int): L'âge de la personne
        """
        self.name = name
        self.age = age

    def display_details(self):
        """Affiche les détails de la personne (nom et âge)."""
        print(f"Nom : {self.name}")
        print(f"Âge : {self.age} ans")


class Employee(Person):
    """Classe représentant un employé, héritant de la classe Person."""

    def __init__(self, name, age, salary):
        """Initialise un nouvel employé.

        Args:
            name (str): Le nom de l'employé
            age (int): L'âge de l'employé
            salary (float): Le salaire de l'employé
        """
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        """Affiche les détails de l'employé (nom, âge et salaire)."""
        super().display_details()
        print(f"Salaire : {self.salary} €")


# Test des classes
if __name__ == "__main__":
    # Test de la classe Person
    print("=== Test de la classe Person ===")
    personne = Person("Alice", 30)
    personne.display_details()

    # Test de la classe Employee
    print("\n=== Test de la classe Employee ===")
    employe = Employee("Bob", 35, 45000)
    employe.display_details()

    # Test avec un autre employé
    print("\n=== Test avec un autre employé ===")
    autre_employe = Employee("Charlie", 28, 38000)
    autre_employe.display_details()
