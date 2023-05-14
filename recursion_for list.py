# рекурсивная функция для подсчёта суммы элементов в списке
def sum(mass):
    if mass == []:
        return 0
    else:
        return mass[0] + sum(mass[1:])


print(sum([2, 4, 6]))
