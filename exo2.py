while True:
    try:
        nom_fichier = input("Entrez le nom du fichier à ouvrir : ")

        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            print("Fichier ouvert avec succès !")
            print(contenu)

        break

    except FileNotFoundError:
        print("FileNotFoundError : le fichier n'existe pas. Veuillez réessayer.")

    except PermissionError:
        print("PermissionError : vous n'avez pas la permission de lire ce fichier.")