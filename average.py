def function(valeurs):
    somme = 0
    numbers = 0
    for element in valeurs :
        somme += element
        numbers += 1
    return somme/numbers if numbers != 0 else 0
