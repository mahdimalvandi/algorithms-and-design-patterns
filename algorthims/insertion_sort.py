from random import shuffle, choice

lst = [choice([i for i in range(100)]) for _ in range(10)]
shuffle(lst)

# =================== Type 1 ===================
sorted_lst = []

for i in lst:
    for j in sorted_lst:
        if j > i:
            sorted_lst.insert(sorted_lst.index(j), i)
            break
    else:
        sorted_lst.append(i)

# print(sorted_lst)

# =================== Type 2 ===================

for i in range(1, len(lst)):
    for j in range(i):
        if lst[j] > lst[i]:
            value = lst[i]
            del lst[i]
            lst.insert(j, value)
            break
print(lst)
