stations = {
    "Адмиралтейская": {
        "Садовая": 4},
    "Садовая": {
        "Сенная площадь": 4,
        "Спасская": 3,
        "Адмиралтейская": 4,
        "Звенигородская": 5},
    "Сенная площадь": {
        "Садовая": 4,
        "Спасская": 4},
    "Спасская": {
        "Садовая": 3,
        "Сенная площадь": 4,
        "Достоевская": 6},
    "Звенигородская": {
        "Пушкинская": 3,
        "Садовая": 5},
    "Пушкинская": {
        "Звенигородская": 3,
        "Владимирская": 4},
    "Владимирская": {
        "Достоевская": 3,
        "Пушкинская": 4},
    "Достоевская": {
        "Владимирская": 3,
        "Спасская": 6}
}
distances = {distance: 100 for distance in stations.keys()}  # расстояния

start_station = 'Адмиралтейская'  # стартовая вершина

distances[start_station] = 0  # расстояние от нее до самой себя равно нулю

flags = {station: False for station in stations.keys()}  # флаги просмотра вершин

ancestors = {station: None for station in stations.keys()}  # предки

for _ in range(len(distances)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_distance = min([distance for distance in flags.keys() if not flags[distance]], key=lambda x: distances[x])

    for station in stations[min_distance].keys():  # проходимся по всем смежным вершинам
        if distances[station] > distances[min_distance] + stations[min_distance][station]:  # если расстояние от текущей вершины меньше
            distances[station] = distances[min_distance] + stations[min_distance][station]  # то фиксируем его
            ancestors[station] = min_distance  # и записываем как предок
    flags[min_distance] = True  # просмотренную вершину помечаем
print(distances)
print(ancestors)
destination = "Владимирская"  # куда должны прийти
path = []  # список с вершинами пути
while destination is not None:  # перемещаемся, пока не придём в стартовую точку
    path.append(destination)
    destination = ancestors[destination]

path.reverse()  # разворачиваем путь
for station in path:
    print(station)
