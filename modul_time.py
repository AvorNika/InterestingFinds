# пример работы модуля time
from time import sleep

print('Почти готово', end=' ')
sleep(0.4)
for _ in range(3):
    print('.', end=' ')
    sleep(0.25)
print()
