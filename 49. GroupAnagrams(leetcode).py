strs = [user_word for user_word in input().split()]
result = {}
new_result = []

for word in strs:
    new_word = str(sorted(word))
    if new_word not in result:
        result[new_word] = [word]
    else:
        result[new_word].append(word)

for elem in result.values():
    new_result.append(elem)

print(new_result)
