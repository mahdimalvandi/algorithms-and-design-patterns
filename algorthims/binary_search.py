lst = [2, 4, 5, 7, 9, 14, 16, 18, 23, 53]


num = int(input("Enter:"))

def binary_search(lst, k):
    low = 0
    high = len(lst)
    mid = (low + high) // 2

    while True:
        if lst[mid] == k:
            return mid
        elif lst[mid] > k:
            high = mid
            mid = (low + high) // 2
        elif lst[mid] < k:
            low = mid
            mid = (low + high) // 2
