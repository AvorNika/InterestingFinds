# рекурсивная функция для нахождения наибольшего числа в списке
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    new_list = max(list[1:])
    return list[0] if list[0] > new_list else new_list


print(max([5, 8, 6, 1, 0]))
