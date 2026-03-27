while True:
    try:

        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))

        if num2 == 0:
            raise ZeroDivisionError

        resultat = num1 / num2

        print(f"Résultat : {resultat}")
        break

    except ZeroDivisionError:
        print("Erreur : division par zéro impossible.")

    except ValueError:
        print("Erreur : veuillez entrer des valeurs numériques valides.")