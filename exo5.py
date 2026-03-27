class ConvertisseurDistance:
    def __init__(self):
        pass

    def metres_vers_km(self, metres):
        return metres / 1000

    def km_vers_metres(self, km):
        return km * 1000

    def lancer(self):
        while True:
            try:
                print("\n--- Convertisseur de distance ---")
                print("1. Mètres → Kilomètres")
                print("2. Kilomètres → Mètres")
                print("3. Quitter")

                choix = input("Choisissez une option : ")

                if choix == "3":
                    print("Au revoir !")
                    break

                valeur = float(input("Entrez la valeur : "))

                if choix == "1":
                    resultat = self.metres_vers_km(valeur)
                    print(f"{valeur} m = {resultat} km")

                elif choix == "2":
                    resultat = self.km_vers_metres(valeur)
                    print(f"{valeur} km = {resultat} m")

                else:
                    print("Choix invalide, veuillez réessayer.")

            except ValueError:
                print("ValueError : veuillez entrer une valeur numérique valide.")

if __name__ == "__main__":
    convertisseur = ConvertisseurDistance()
    convertisseur.lancer()