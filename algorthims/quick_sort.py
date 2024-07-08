from random import shuffle

length = 20

lst = [i for i in range(length)]
shuffle(lst)


def quick_sort(lst, low, high):
    if low < high:
        pivot = low
        i = low
        j = high

        while i < j:
            while lst[i] <= lst[pivot] and i < high:
                i += 1

            while lst[j] > lst[pivot]:
                j -= 1

            if i < j:
                lst[i], lst[j] = lst[j], lst[i]

        lst[j], lst[pivot] = lst[pivot], lst[j]

        quick_sort(lst, low, j - 1)
        quick_sort(lst, j + 1, high)

    return lst


print(quick_sort(lst, 0, len(lst) - 1))
