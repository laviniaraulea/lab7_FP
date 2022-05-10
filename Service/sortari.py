from Domain.entities import student


def cmp(x, y):
    return x < y


def cmpd(x, y):
    return x > y


def selection_sort(lista, key=lambda x: x, reverse=False):
    n = len(lista) - 1
    for i in range(n):
        elem_nou = i
        for j in range(i, n + 1):
            if reverse:
                if cmpd(key(lista[j]), key(lista[elem_nou])):
                    elem_nou = j
            else:
                if cmp(key(lista[j]), key(lista[elem_nou])):
                    elem_nou = j
        lista[elem_nou], lista[i] = lista[i], lista[elem_nou]
    return lista


def test_sort():
    s1 = student(50947, "dahafjw", 234)
    s2 = student(3563, "fsdbgjnkhm", 3725)
    s3 = student(32, "fysfa", 345)
    s4 = student(3563, "fsdbgjnkhm", 1725)
    lista = [7, 4, 6]
    lista = ShakeSort(lista)
    assert (lista == [4, 6, 7])


def ShakeSort(lista, key=lambda x: x, reverse=False):
    n = len(lista)
    ok = True
    inceput = 0
    final = n - 1
    while ok == True:
        ok = False
        for i in range(inceput, final):
            if reverse:
                if cmp(key(lista[i]), key(lista[i + 1])):
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    ok = True
            else:
                if cmpd(key(lista[i]), key(lista[i + 1])):
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    ok = True
        ok = False
        final = final - 1
        for i in range(final - 1, inceput, -1):
            if reverse:
                if cmp(key(lista[i]), key(lista[i + 1])):
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    ok = True
            else:
                if cmpd(key(lista[i]), key(lista[i + 1])):
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    ok = True
        inceput = inceput + 1
    return lista
