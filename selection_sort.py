#Сортировка выбором
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]


arr = [5, 3, 6, 2, 10]
selection_sort(arr)
print(arr)
