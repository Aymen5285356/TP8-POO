class Calculatrice:
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def effectuer_operation(self, operation, a, b):
        if operation == "A":
            return self.addition(a, b)
        elif operation == "S":
            return self.soustraction(a, b)
        elif operation == "M":
            return self.multiplication(a, b)
        elif operation == "D":
            return self.division(a, b)
        else:
            raise ValueError("Opération non reconnue.")

    def lancer(self):
        while True:
            try:
                print("\n--- Calculatrice ---")
                operation = input(
                    "Choisissez une opération (A,S,M,D) : ").lower()

                a = float(input("Entrez le premier nombre : "))
                b = float(input("Entrez le deuxième nombre : "))

                resultat = self.effectuer_operation(operation, a, b)
                print(f"Résultat : {resultat}")

            except ZeroDivisionError:
                print(" ZeroDivisionError : division par zéro impossible.")
            except ValueError as ve:
                print(f"ValueError : {ve}")

            continuer = input("Voulez-vous effectuer un autre calcul ? (oui/non) : ").lower()
            if continuer != "oui":
                print("Au revoir Monsieur!")
                break

if __name__ == "__main__":
    calc = Calculatrice()
    calc.lancer()