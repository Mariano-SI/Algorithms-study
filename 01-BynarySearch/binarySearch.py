def binary_search(list, item):
    low = 0
    high = len(list) - 1
    """ low e high representam respectivamente os indices do menor e do maior elemento dentro do conjunto a ser analisado
        isso porque, a busca binaria é apliicada em conjuntos ordenados então o menor possivel sempre esta no inicio e o maior no fim
    """
    while low <= high:
        mid = (low + high)//2 # verifica o elemento central, capturando seu indice e fazendo um chute
        test = list[mid]
        if test == item: # compara se ele é o item buscado, se sim, retornaremos seu indice
            return mid
        if test > item: #chute muito alto então o novo limite é no meio da lista
            high = mid - 1
        else:           #chute muito baixo então o limite inferior é o meio
            low = mid + 1
    return None

# Testes
my_list = [1,2,3,4,5,6,7,8]      
print( binary_search(my_list, 7) )#6

another_list = [5, 15, 30, 42, 57, 61, 75, 80, 88, 99]
print( binary_search(another_list, 57) )#4

