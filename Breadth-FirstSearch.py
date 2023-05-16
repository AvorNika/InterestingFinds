# Поиск в ширину
def search(name):
    from collections import deque
    search_queue = deque()   # создание новой очереди
    search_queue += graph[name]   # все соседи добавляются в очередь поиска
    searched = []   # это массив используется для отслеживания уже проверенных людей
    while search_queue:   # пока очередь не пуста...
        person = search_queue.popleft()   # из очереди извлекается первый человек
        if not person in searched:   # человек проверяется только в том случае, если он не проверялся ранее
            if person_is_seller(person):   # проверяем, является ли это человек продавцом манго
                print(person + ' is a mango seller!')   # да, это продавец манго
                return True
            else:
                search_queue += graph[person]   # нет, человек не является продавцом. Все его друзья добавляются в очередь списка
                searched.append(person)   # человек помечается как уже проверенный
    return False   # если выполнение дошло до этой строки, значит в очереди нет продавца манго


def person_is_seller(name):   # функция проверяет, является ли человек из очереди продавцом
    return len(name) == 10


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

search('you')
