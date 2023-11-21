def binary_search(arr, target):
    low, high = 0, len(arr) -1
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_target = 8

result = binary_search(lista, number_target)
print(f'Elemento {number_target} encontrado no indice {result}')

# A busca é realizada a partir do meio da lista, e há como pré-requisito que seja uma lista ordenada.
