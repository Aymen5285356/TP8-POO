class AccesListe:
    def __init__(self):
        self.langages = ["Python", "Javascript", "C", "C++"]

    def demander_indice(self):
        while True:
            try:
                indice = int(input("Entrez un indice : "))
                element = self.langages[indice]
                print(f"Élément trouvé : {element}")
                break

            except ValueError:
                print("ValueError : veuillez entrer un nombre entier valide.")

            except IndexError:
                print("indexError : indice hors de la plage de la liste.")

if __name__ == "__main__":
    programme = AccesListe()
    programme.demander_indice()