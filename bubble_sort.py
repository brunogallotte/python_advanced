def bubble_sort(arr):
    for i in range(len(arr)):
        
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Exec
unsorted_list = [4, 9, 15, 25, 31, 2, 1, 16]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)

# Bubble sort organiza uma lista desorganiada comparando os indicies de 2 em 2
