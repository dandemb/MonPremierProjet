def function(valeurs):
    somme = 0
    numbers = 0
    for element in valeurs :
        somme += element
        numbers += 1
    return somme/numbers if numbers != 0 else 0


def main() : 
    print("Entrez vos valeurs séparées par des virgules (ex: 10,20,30) :")
    entree = input("")

    if not entree.strip():
        print("Aucune valeur entrée. La moyenne est 0.")
        return

    try :
     user_input = [float(x) for x in entree.split(",")]
    except ValueError:
        print("Entrée invalide. Veuillez entrer des nombres valides séparés par des virgules.")
        return

    resultat = function(user_input)
    print("La moyenne est :", resultat)

if __name__ == "__main__":
    main()