import copy

a = [1, 2, 3, 4]

b = a.copy()   # deep copy

c = copy.deepcopy(a)   # deep copy
d = a   # shallow copy

c.append(10)
a[0] = 89

print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))
