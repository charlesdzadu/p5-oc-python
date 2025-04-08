class Book:
    """Classe représentant un livre avec titre, auteur et année de publication."""

    def __init__(self, title, author, year):
        """Initialise un nouveau livre.

        Args:
            title (str): Le titre du livre
            author (str): L'auteur du livre
            year (int): L'année de publication
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Retourne une représentation textuelle du livre.

        Returns:
            str: Description du livre
        """
        return f"{self.title} par {self.author} ({self.year})"


class Library:
    """Classe représentant une bibliothèque avec gestion des livres."""

    def __init__(self):
        """Initialise une nouvelle bibliothèque avec des listes vides."""
        self.books = []  # Livres disponibles
        self.borrowed_books = []  # Livres empruntés

    def add_book(self, book):
        """Ajoute un livre à la bibliothèque.

        Args:
            book (Book): Le livre à ajouter
        """
        self.books.append(book)
        print(f"Livre ajouté : {book}")

    def remove_book(self, book_title):
        """Supprime un livre de la bibliothèque.

        Args:
            book_title (str): Le titre du livre à supprimer
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Livre supprimé : {book}")
                return
        print(f"Livre '{book_title}' non trouvé dans la bibliothèque")

    def borrow_book(self, book_title):
        """Emprunte un livre de la bibliothèque.

        Args:
            book_title (str): Le titre du livre à emprunter
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                print(f"Livre emprunté : {book}")
                return
        print(f"Livre '{book_title}' non disponible")

    def return_book(self, book_title):
        """Rend un livre à la bibliothèque.

        Args:
            book_title (str): Le titre du livre à rendre
        """
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                print(f"Livre rendu : {book}")
                return
        print(f"Livre '{book_title}' non trouvé dans les livres empruntés")

    def available_books(self):
        """Affiche la liste des livres disponibles."""
        if not self.books:
            print("Aucun livre disponible")
            return
        print("\nLivres disponibles :")
        for book in self.books:
            print(f"- {book}")

    def display_borrowed_books(self):
        """Affiche la liste des livres empruntés."""
        if not self.borrowed_books:
            print("Aucun livre emprunté")
            return
        print("\nLivres empruntés :")
        for book in self.borrowed_books:
            print(f"- {book}")


# Test des classes
if __name__ == "__main__":
    # Création de la bibliothèque
    bibliotheque = Library()

    # Création de quelques livres
    livre1 = Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
    livre2 = Book("1984", "George Orwell", 1949)
    livre3 = Book("Notre-Dame de Paris", "Victor Hugo", 1831)

    # Test d'ajout de livres
    print("=== Ajout de livres ===")
    bibliotheque.add_book(livre1)
    bibliotheque.add_book(livre2)
    bibliotheque.add_book(livre3)

    # Affichage des livres disponibles
    print("\n=== Liste des livres disponibles ===")
    bibliotheque.available_books()

    # Test d'emprunt de livre
    print("\n=== Emprunt de livres ===")
    bibliotheque.borrow_book("1984")
    bibliotheque.borrow_book("Le Petit Prince")

    # Affichage des livres après emprunts
    print("\n=== État de la bibliothèque après emprunts ===")
    bibliotheque.available_books()
    bibliotheque.display_borrowed_books()

    # Test de retour de livre
    print("\n=== Retour de livre ===")
    bibliotheque.return_book("1984")

    # Affichage final
    print("\n=== État final de la bibliothèque ===")
    bibliotheque.available_books()
    bibliotheque.display_borrowed_books()

    # Test des cas d'erreur
    print("\n=== Test des cas d'erreur ===")
    bibliotheque.borrow_book("Livre inexistant")
    bibliotheque.return_book("Livre non emprunté")
