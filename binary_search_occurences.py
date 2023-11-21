def bubble_sort(arr):
    for i in range(len(arr)):

        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def count_occurrences(arr, target):
    def binary_search_first(arr, target):
        low, high = 0, len(arr) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == target:
                result = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return result
    
    def binary_search_last(arr, target):
        low, high = 0, len(arr) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                result = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result
    
    first_ocurrence = binary_search_first(arr, target)
    last_ocurrence = binary_search_last(arr, target)

    if first_ocurrence != -1:
        count = last_ocurrence - first_ocurrence + 1
        return count
    else: 
        return 0
    
unorded_list = [3, 1, 5, 15, 7, 29, 29, 31, 42, 56, 42, 10]
order_list = bubble_sort(unorded_list)
target_number = 42

ocurrences = count_occurrences(order_list, target_number)
print(f'O número {target_number} ocorre {ocurrences} vezes na lista.')
