## Écrivez votre code ici !

class BankAccount:
    """Classe représentant un compte bancaire."""

    def __init__(self, account_holder, initial_balance=0):
        """Initialise un nouveau compte bancaire.

        Args:
            account_holder (str): Le nom du titulaire du compte
            initial_balance (float, optional): Le solde initial du compte. Defaults to 0.
        """
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Dépose de l'argent sur le compte.

        Args:
            amount (float): Le montant à déposer

        Returns:
            bool: True si le dépôt est réussi, False sinon
        """
        if amount <= 0:
            print("Le montant du dépôt doit être positif.")
            return False
        
        self.balance += amount
        print(f"Dépôt de {amount}€ effectué avec succès.")
        return True

    def withdraw(self, amount):
        """Retire de l'argent du compte.

        Args:
            amount (float): Le montant à retirer

        Returns:
            bool: True si le retrait est réussi, False sinon
        """
        if amount <= 0:
            print("Le montant du retrait doit être positif.")
            return False
        
        if amount > self.balance:
            print("Solde insuffisant pour effectuer ce retrait.")
            return False
        
        self.balance -= amount
        print(f"Retrait de {amount}€ effectué avec succès.")
        return True

    def display_balance(self):
        """Affiche le solde et le nom du propriétaire du compte."""
        print(f"Compte de {self.account_holder}")
        print(f"Solde actuel : {self.balance}€")


# Test de la classe BankAccount
if __name__ == "__main__":
    # Création d'un compte
    compte = BankAccount("Alice", 1000)
    print("=== État initial du compte ===")
    compte.display_balance()

    # Test de dépôt
    print("\n=== Test de dépôt ===")
    compte.deposit(500)
    compte.display_balance()

    # Test de retrait réussi
    print("\n=== Test de retrait réussi ===")
    compte.withdraw(300)
    compte.display_balance()

    # Test de retrait avec montant négatif
    print("\n=== Test de retrait avec montant négatif ===")
    compte.withdraw(-100)

    # Test de retrait avec montant trop élevé
    print("\n=== Test de retrait avec montant trop élevé ===")
    compte.withdraw(2000)
    compte.display_balance()

    # Test de dépôt avec montant négatif
    print("\n=== Test de dépôt avec montant négatif ===")
    compte.deposit(-500)
