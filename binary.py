# binary_search
# nearest_value
import math


def binary_search_list(l, v):
    return binary_search(l, 0, len(l) - 1, v)


def binary_search(l, b, e, v):
    mid = math.floor((b + e) / 2)
    if b <= e:
        if v == l[mid]:
            return mid
        elif v < l[mid]:
            return binary_search(l, b, mid - 1, v)
        else:  # v > l[mid]
            return binary_search(l, mid + 1, e, v)
    else:
        return mid

def nearest_value(l, p, v):
    if p == 0:  # very left position
        if l[p + 1] - v < v - l[p]:
            return l[p + 1]
        else:
            return l[p]

    elif p == len(l) - 1:  # very right position
        if v - l[p - 1] < v - l[p]:
            return l[p - 1]
        else:
            return l[p]
    else:  # in between / general case
        if v - l[p-1] < v - l[p]:
            return l[p-1]
        elif l[p+1] - v < v - l[p]:
            return l[p+1]
        else:
            return l[p]

def unil_binary(L, s, r, e):
    if s <= r:
        mid = int((s+r) / 2)
        if L[mid] == e:
            return mid
        elif L[mid] > e:
            return unil_binary(L, s, mid - 1, e)
        else:
            return unil_binary(L, mid + 1, r, e)
    else:
        mid = int((s+r)/2)
        return mid

def unil_binary_list(l, v):
    return binary_search(l, 0, len(l) - 1, v)
