def merge(a, b):
    l = []

    i = 0
    j = 0

    while True:
        if a[i] <= b[j]:
            l.append(a[i])
            i += 1
        else:
            l.append(b[j])
            j += 1

        if i >= len(a):
            l.extend(b[j:])
            break

        if j >= len(b):
            l.extend(a[i:])
            break

    return l


def insertion_sort(l):
    while True:
        swapped = False

        for i in range(len(l)-1):
            if l[i] > l[i + 1]:
                swapped = True
                m = l[i + 1]
                l[i + 1] = l[i]
                l[i] = m

        if not swapped:
            break
