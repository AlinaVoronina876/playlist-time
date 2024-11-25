  # 1 commit (task info)
#-----------------------------------------------------INFO------------------------------------------------------------------
# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * список списков с парами значений строка-вещественное число
#   * кортеж строк
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
#get_duration(playlist: Iterable, n: int) -> Any


# --------------------------------------------------PLAYLISTS-------------------------------------------------------------------
#   # 2 commit (add list playlist_a)
playlist_a = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
    ]
# 3 commit (add tuple playlist_c)
playlist_c = (
    "Happy Nation; 3.32",
    "It's My Life; 3.59",
    "Lady(Hear Me Tonight); 5.07",
    "Fields Of Gold; 3.38",
    "The Winner Takes It All; 4.54",
    "Self Control; 4.06",
    "I Shot The Sheriff; 4.57",
    "Don't Give Up; 6.34",
    "Relax, Take It Easy; 4.30",
    "Dancing Queen; 3.36",
)


#----------------------------------------------------MAIN-----------------------------------------------------------------
  # 4 commit (libraries)
import random as rn
from typing import Iterable, Any

  # 5 commit (add func get_time_list)
def get_time_list(playlist, n):
    time = 0
    for _ in range(n):
        time += (rn.choice(playlist))[1]
    return time

 # 6 commit (add func get_time_tuple)
def get_time_tuple(playlist, n):
    time = 0
    for _ in range(n):
        time += float(rn.choice(playlist)[-4:])
    return time

  # 7 commit (main func)
def get_duration(playlist: Iterable, n: int) -> Any:
    if type(playlist) == tuple:
        return get_time_tuple(playlist, n)
    elif type(playlist) == list:
        return get_time_list(playlist, n)

 # 8 commit (func call)
choose_playlist = input('''Введите цифру вашего плейлиста: 
1. playlist_a (list)
2. playlist_c (tuple)
 - ''')

numb = int(input('Введите параметр n - '))

if choose_playlist == '1':
    print(get_duration(playlist_a, numb))
else:
    print(get_duration(playlist_c, numb))
