s = input()
n = int(len(s)/2)

for _ in range(n):
    if '()' in s:
        s = s.replace('()', '')
    elif '[]' in s:
        s = s.replace('[]', '')
    elif '{}' in s:
        s = s.replace('{}', '')

if len(s) == 0:
    print(True)
else:
    print(False)


#flag = True
# my_dict = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
# result = 0
# for elem in s:
#     result += my_dict[elem]
#     if result < 0:
#         flag = False
#         break
# print(flag)
