# программный код быстрой сортировки
def quicksort(list):
    if len(list) < 2:
        return list   # базовый случай: массивы с 0 и 1 элементом уже "отсортированы"
    else:
        pivot = list[0]   # рекурсивный случай
        less = [i for i in list[1:] if i <= pivot]   # подмассив всех элементов, меньших опорного
        greater = [i for i in list[1:] if i > pivot]   # подмассив всех элементов, больших опорного
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
