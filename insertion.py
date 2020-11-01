def insertion_sort(L):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                sorted = False
                tmp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = tmp