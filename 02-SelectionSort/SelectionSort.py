# Ordenar array de numeros por meio da selection sort
# OBS: Futuramente fazer um algoritmo que ordene uma lista de artistas por numero de plays utilizando esse algoritmo e array de objetos.

# funcao auxiliar para buscar o menor elemento em um array

def searchSmaller(arr):
    smaller = arr[0]
    smallerindex = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smallerindex = i
    return smallerindex

def selectionSort(arr):
    newArray = []
    for i in range(len(arr)):  
        smallerIndex = searchSmaller(arr)
        newArray.append(arr.pop(smallerIndex)) # aplicar o pop mesmo por meio de parametro de uma funcao já altera a base de dados, difrerentemente de js/ts onde eu preciso passar o valor mas tambem alterar a base a cada iteracao
    return newArray

myArray = [5,3,6,2,10]

print(selectionSort(myArray))  # Saída: [2, 3, 5, 6, 10]