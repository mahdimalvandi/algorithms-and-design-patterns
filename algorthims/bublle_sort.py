from random import randint as rnd
import matplotlib.pyplot as plt

length = 20

_list = [rnd(0, length) for i in range(length)]

for j in range(length):
    flag = True
    for i in range(length - 1):
        if _list[i] > _list[i + 1]:
            flag = False
            _list[i], _list[i + 1] = _list[i + 1], _list[i]
        plt.bar(range(length), _list)
        plt.pause(0.005)
        plt.clf()
    if flag:
        break

plt.bar(range(length), _list)
plt.show()