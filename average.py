def function(list):
    somme = 0
    numbers = 0
    for element in list :
        somme += element
        numbers += 1
    return somme/numbers if numbers != 0 else 0
