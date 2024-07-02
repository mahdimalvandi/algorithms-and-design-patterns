from random import randint as rnd

length = 10

_list = [rnd(0, length) for i in range(length)]

for i in range(length-1):
    _min = i
    for j in range(i+1, length):
        if _list[_min] > _list[j]:
            _list[_min], _list[j] = _list[j], _list[_min]

print(_list)