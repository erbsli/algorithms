import math
import sys

def merge_two_arrays(X, Y):
    A = X + Y
    merge(A, 0, len(X), len(A))
    return A

def merge_sort_list(A):
    merge_sort(A, 0, len(A))


def merge_sort(A, p, r): # r is exclusive
    if r - p > 1:
        q = math.floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)


def merge(A, p, q, r): # q and r are exclusive
    n1 = q - p
    n2 = r - q
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j]

    L.append(sys.maxsize)
    R.append(sys.maxsize)

    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
