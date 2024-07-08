from random import choice

lst = [0, 1, 2, 2, 8, 9, 13, 52, 66, 73]



def merge(lst1, lst2):
    slst = []

    l1 = len(lst1)
    l2 = len(lst2)

    i = j = 0

    while i < l1 and j < l2:
        if lst1[i] < lst2[j]:
            slst.append(lst1[i])
            i += 1
        else:
            slst.append(lst2[j])
            j += 1

    slst += lst2[j:]
    slst += lst1[i:]
    return slst


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

print(merge_sort(lst))