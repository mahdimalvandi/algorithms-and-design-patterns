from random import randint as rnd

length = 10

_list = [rnd(0, length) for i in range(length)]

for i in range(length):
    _min = i
    for j in range(i, length):
        if _list[_min] > _list[j]:
            _min = j
        
    _list[i], _list[_min] =  _list[_min],_list[i]







