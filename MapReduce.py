arr1 = [1, 2, 3, 4, 5]
arr2 = map(lambda x: 2 * x, arr1)
print(arr2)


arr2 = reduce(lambda x, y: x+y, arr1)