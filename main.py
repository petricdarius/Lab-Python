# def matrix(n):
#     matrice = [[0] * n for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             matrice[i][j] = int(input())
#     min = 100000000
#     max = -1
#     maxi = [0, 0]
#     mini = [0, 0]
#     for i in range(n):
#         for j in range(n):
#             if matrice[i][j] < min:
#                 min = matrice[i][j]
#                 mini = [i, j]
#             if matrice[i][j] > max:
#                 max = matrice[i][j]
#                 maxi = [i, j]
#     print("Valoarea minima este:", min, "pe pozitia: ", mini)
#     print("Valoarea maxima este:", max, "pe pozitia: ", maxi)
#
#
# def matrix2(matrice, n):
#     for i in range(n):
#         for j in range(n):
#             if (i+1) * (j+1) % 2 == 0:
#                 matrice[i][j] = 1
#             if (i+1) * (j+1) % 2 == 1:
#                 matrice[i][j] = 0
#             if i == j:
#                 matrice[i][j] = 2
#     for i in range(n):
#         for j in range(n):
#             print(matrice[i][j], end=" ")
#         print()
#
#
# def unire(stanga, dreapta):
#     i = 0
#     j = 0
#     lista_noua = []
#     while i< len(stanga) and j< len(dreapta):
#         if stanga[i] < dreapta[j]:
#             lista_noua.append(stanga[i])
#             i += 1
#         elif dreapta[j] < stanga[i]:
#             lista_noua.append(dreapta[j])
#             j += 1
#     while i < len(stanga):
#         lista_noua.append(stanga[i])
#         i += 1
#     while j < len(dreapta):
#         lista_noua.append(dreapta[j])
#         j += 1
#     return lista_noua
#
# def og(n):
#     nr = 0
#     while(n):
#         nr = nr* 10 + n%10
#         n/=10
#     print(nr)
#
# def msort(lista):
#     if len(lista) <= 1:
#         return lista
#     else:
#         mij = len(lista) // 2
#         stanga = msort(lista[:mij])
#         dreapta = msort(lista[mij:])
#     return unire(stanga, dreapta)
#
#
#
# if __name__ == '__main__':
#     # n = int(input())
#     # matrice = [[0] * n for i in range(n)]
#     # print(msort([1 , 3, 10, 20, 13, 18, 29, 4, 5]))
#     og(1)
#
def cautarebin(c):
    lista_monede_disponibile = [1, 5, 10, 20, 50, 100]
    lista_rezultat = [0] * len(lista_monede_disponibile)
    lista_monede_disponibile.reverse()
    for i in range(len(lista_monede_disponibile)):
        while lista_monede_disponibile[i] <= c:
            c -= lista_monede_disponibile[i]
            lista_rezultat[i] = lista_rezultat[i] + 1
    lista_rezultat.reverse()
    return lista_rezultat


def prb2(l):
    for i in range(len(l)):
        l[i] = 255 - l[i]
    return l


def fibo(n):
    if n <= 2:
        return [1]
    fib = [None] * n
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib


def my_function(l):
    return l[::-1]


def cautarebin(data, elem):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def cmaxrec(n):
    max = 1
    if n % 10 >= max:
        max = n % 10
    if n != 0:
        return cmaxrec(n//10)
    if n == 0:
        return max


def p_0218(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                matrix[i][j] = i + j + 2
            else:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1]
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


import math
def p_0922(*points):
    max_dist = 0
    count_max = 0
    for point in points:
        dist = math.sqrt(point[0] ** 2 + point[1] ** 2)  # calculăm distanța dintre punct și origine
        if dist > max_dist:
            max_dist = dist
            count_max = 1
        elif dist == max_dist:
            count_max += 1
    print(max_dist)
    print(count_max)


def my_function(a, b):
    l = [0] * (a+2)
    nr = ""
    a+=1
    for i in range(a):
        l[i] = input()
    for i in range(2, a):
        nr += l[i]
    nr2 = int(l[1]) + b
    nr += str(nr2)
    print(nr)


def func(l):
    l.sort()
    l2 = []
    l2.append(l[0])
    for i in range(1, len(l)):
        ok = 1
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                ok = 0
        if ok:
            l2.append(l[i])
    print(l2)


def func(n):
    cn = n
    ogl = 0
    while n:
        ogl = ogl * 10 + n % 10
        n //= 10
    print(ogl)
    if ogl == cn:
        print("DA")
    else:
        print("NU")


def vector(l1, l2):
    for i in range(len(l1)):
        ok = 0
        for j in range(len(l2)):
            if l1[j] == l2[i]:
                ok = 1
                print("DA")
        if ok == 0:
            print("NU")


def lista():
    a = int(input())
    b = int(input())
    l = []
    for i in range(a, b):
        l[i].append(i)
    print(l)


def minmax(l):
    min = 1000000000
    max = -1
    min1 = 100000000
    max1 = -1
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
        if l[i] > max:
            max = l[i]
    return min,max


def minmax2(l):
    l.sort()
    min1 = l[0]
    min2 = l[1]
    max2 = l[-1]
    max1 = l[-2]
    return min1, min2, max1, max2


def matrix(m):
    sir = "abcd"
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                print(sir[i], end=" ")
        print()


def rec(n):
    if n == 0:
        return 1
    elif n < 10:
        return 0
    else:
        if n % 10 == 0:
            return 1 + rec(n//10)
        else:
            return rec(n//10)


def my_function(s, c):
    cnt = 0
    for i in s:
        if i == c:
            cnt += 1
    cnt2 = 0
    for i in s:
        if i == c:
            cnt -= 1
        else:
            cnt2 +=1
        if cnt == 1:
            break
    print(s[:cnt2])


def cautare(lista, nr):
    ok = 0
    for i in range(len(lista)):
        if lista[i] == nr:
            print("DA")
            ok = 1
    if ok == 0:
        print("NU")


def bubble(l):
    switch = True
    while switch:
        switch = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                switch = True
    return l


def sir(s):
    s = s.replace("s", "*")
    s = s.replace("*", "s", 1)
    print(s)


def mergsort(l):
    n = len(l)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if l[j] < l[min]:
                min = j
        if min != i:
            aux = l[i]
            l[i] = l[min]
            l[min] = aux
    return l


employee1 = {
        'id': 14,
        'name': 'John Doe',
        'age': 36,
        'position': 'Business Manager.'
}
employee2 = {
        'id': 120,
        'name': 'Dari',
        'age': 18,
        'position': 'Software.'
}
employee3 = {
        'id': 36,
        'name': 'Alex',
        'age': 19,
        'position': 'Lucrator.'
}
employee4 = {
        'id': 2,
        'name': 'Andrei',
        'age': 20,
        'position': 'Developer.'
}


def cautareangajat(list1):
    for i in range(len(list1)):
        last = list(list1[i].values())[0]
        if last == 2:
            print(list1[i])

def numar_vocale_intre_consoane(sir):
    vocale = 'aeiou'
    consoane = 'bcdfghjklmnpqrstvwxyz'
    numar_vocale = 0
    start_consoana = -1
    for i in range(len(sir)):
        if sir[i] in consoane:
            if start_consoana != -1:
                for j in range(start_consoana + 1, i):
                    if sir[j] in vocale:
                        numar_vocale += 1
            start_consoana = i
    return numar_vocale


def cautare(l, nr):
    for i in range(len(l)):
        if l[i] == nr:
            return i
    return None


import random
def generareCNP(gen, an, luna, zi, judet, nnn):
    CNP = ""
    if gen == "M" or gen == "m" or gen == "masculin":
        if an>=2000:
            CNP += "5"
        else:
            CNP += "1"
    else:
        if an < 2000:
            CNP += "2"
        else:
            CNP += "6"
    if an >= 2000:
        an -= 2000
    else:
        an -= 1900
    if an < 10:
        CNP += "0"
    CNP += str(an)
    if luna < 10:
        CNP += "0"
    CNP += str(luna)
    if zi < 10:
        CNP += "0"
    CNP += str(zi)
    if judet < 10:
        CNP += "0"
    CNP += str(judet)
    if nnn < 10:
        CNP += "00"
    elif nnn < 100:
        CNP += "0"
    CNP += str(nnn)
    CNP += str(generareC(CNP))
    print(CNP)


def cifmax(nr):
    if len(str(nr)) == 1:
        return nr
    return max(nr % 10, cifmax(nr//10))


def fisier():
    file = open('da.txt', 'r+')


def generareC(CNP):
    cifre = "279146358279"
    cifracontrol = 0
    for i in range(len(CNP)):
        cifracontrol += int(CNP[i]) * int(cifre[i])
    cifracontrol %= 11
    if cifracontrol == 10:
        cifracontrol = 1
    return cifracontrol


def graf(l):
    max = 0
    for i in l:
        for e in i:
           if e > max:
               max = e
    mat = []
    n = max + 1
    mat = [[0] * n for i in range(n)]
    for element in l:
        x = element[0]
        y = element[1]
        mat[x][y] = 1
        mat[y][x] = 1
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()


def lista_adiacenta(mat):
    lista = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1 and j > i:
                lista[i].append([i, j])
    return lista


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 == dice2:
        return True
    else:
        return 1 + roll_dice()


def calculeaza_suma(n):
    suma = 0
    produs = 1
    for i in range(1, n + 1):
        produs *= i
        suma += produs
    return suma


parcurs = []
lp = []


def parcurgeregraph(graph, start):
    if start not in lp:
        parcurs.append(start)
        for element in graph:
            if element[0] == start and start not in lp:
                lp.append(start)
                parcurgeregraph(graph, element[1])


def parcurgereit(graph, start):
    cale = []
    currentnode = start
    cale.append(currentnode)
    for element in graph:
        if element[0] == currentnode:
            currentnode = element[1]
            cale.append(currentnode)
    return cale

def toatecaile(graph):
    cai = []
    n = len(graph)
    i = 0
    while i < n:
        primelement = graph[0][0]
        cai.append(parcurgereit(graph, primelement))
        graph.pop(0)
        i += 1
    print(cai)


if __name__ == '__main__':
    l = [100, 2, 4, 30, 230]
    # print(cautarebin(44))
    # print(prb2(l))
    # print(fibo(20))
    # print(my_function('abcd'))
    # print(cautarebin([1,10,23,40,500,1000], 23))
    # print(cmaxrec(293))
    # print(sum_of_two('12 443 55 4 3 2 2 1 4 5 6 6 7 76 54 33 3 3 33 3 334'))
    #
    # vector([0, 1, 2, 3, 4, 0, 33, 44, 55, 66, 777], [1, 2, 3, 555, 0, 33, 44, 55, 66, 777, 888])

    # def func(x):
    #
    #     res = 0
    #
    #     for i in range(x):
    #         res += i
    #
    #     return res
    #
    #
    # print(func(398))
    # l = [10, 2, 100, 39, 240, 1, 30, 20, 909, 0]
    # matrix([[1,1,1], [1, 1, 1], [1, 1, 1]])
    # sir("salut salt")
    # my_list = ['2', '1', '12']
    # print(max(my_list))
    # cautare([1, 3, 4, 30, 0, 25], 0)
    # print(mergsort([9, 3, 10, 1, 0, 2]))
    # employee1 = {
    #     'id': 14,
    #     'name': 'John Doe',
    #     'age': 36,
    #     'position': 'Business Manager.'
    # }
    # employee2 = {
    #     'id': 120,
    #     'name': 'Dari',
    #     'age': 18,
    #     'position': 'Software.'
    # }
    # employee3 = {
    #     'id': 36,
    #     'name': 'Alex',
    #     'age': 19,
    #     'position': 'Lucrator.'
    # }
    # employee4 = {
    #     'id': 2,
    #     'name': 'Andrei',
    #     'age': 20,
    #     'position': 'Developer.'
    # }
    # list1=[employee1, employee2, employee3, employee4]
    # print(employee1.keys())
    # print(employee1.values())
    # last=list(employee1.values())[0]
    # print(last)
    # list1 = [employee1, employee2, employee3, employee4]
    # cautareangajat(list1)
    # print(numar_vocale_intre_consoane("oasele sunt fragile"))
    # generareCNP("m",2004,6,18, 24, 506)
    # print(cifmax(9))
    # file = open('da.txt', 'r+')
    # txt = file.read()
    # v = txt.split('\n')
    # i = 0
    # while i < len(v):
    #     print(v[i])
    #     i += 1
    # f5 = 0
    # f6 = 0
    # print(i)
    # for i in range(len(v)):
    #     if v[i].startswith('5'):
    #         f5 = 1
    #     if v[i].startswith('6'):
    #         f6 = 1
    #     if v[i].startswith('7'):
    #         if f5 == 0:
    #             v.insert(i, '5555')
    #         if f6 == 0:
    #             v.insert(i+1, '6666')
    #         break
    # print(v)
    # file.close()
    # file = open('da.txt', 'w+')
    # for e in v:
    #     file.write(e)
    #     file.write('\n')
    # file.close()
    # file = open('da.txt', 'r+')
    # file.seek(0)
    # line = file.readline()
    # while line != '':
    #     if line.startswith('7'):
    #         file.seek(file.tell()-len(line)-1)
    #         file.write('5555\n')
    #         file.write(line)
    #     print(line)
    #     print(file.tell())
    #     line = file.readline()
    # file.close()
    # l = [[0, 1], [0, 2], [1, 2], [1, 3], [3, 4]]
    # graf(l)
    #print(roll_dice())
    # print(calculeaza_suma(4))
    graph = [[0, 1], [0, 2],
             [1, 2], [1, 3],
             [2, 4], [2, 6],
             [4, 5],
             [5, 7]]
    # parcurgereit(graph, 0)
    # print(parcurs)
    # print(lp)
    toatecaile(graph)