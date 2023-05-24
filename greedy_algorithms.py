# Жадные алгоритмы
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])   #создали множество штатов для покрытия

stations = {}   # создали хеш-таблицу с информацией о покрытии штатов станциями
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["ktour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()   # создали пустое множество для итогового списка станций

while states_needed:   # до тех пор, пока не охвачены все штаты
    best_station = None   # создаём переменную, в которую будем передавать имя наиболее подходящей станции на каждом этапе
    states_covered = set()   # создаём множество, в котором будут указаны все штаты, покрываемые станцией best_station
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station   # передаём в переменную множество штатов, покрываемых станцией
        if len(covered) > len(states_covered):   # если покрываемых штатов больше, чем уже покрытых
            best_station = station   # присваиваем переменной значение наиболее подходящей станции
            states_covered = covered   # передаём в переменную список покрытых штатов

    states_needed -= states_covered   # исключаем из списка для проверки уже покрытые штаты
    final_stations.add(best_station)   # передаём в итоговый список имя наиболее подходящей станции

print(final_stations)
