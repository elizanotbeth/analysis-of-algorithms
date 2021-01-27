import random
import pylab
import time

def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end = ' ')
        print()
def init_matr(m, n):
    matrix = [[0] * n for i in range(m)]
    for i in range(0, m):
        for j in range(0, n):
            matrix[i][j] = random.randint(-10, 10)
    return matrix
def init_matr_hand(m, n):
    matrix = [[0] * n for i in range(m)]
    print("Введите матрицу: ")
    for i in range(0, m):
        for j in range(0, n):
            matrix[i][j] = int(input())
    return matrix
def standart_multiplication_matrix(m1, m2):
    n = len(m1)  # строки первой
    q = len(m2[0])   # столбцы второй
    m = len(m1[0])   # столбцы первой
    m3 = [[0] * q for i in range(n)]
    start_time = time.process_time()
    for i in range(0, n):
        for j in range(0, q):
            for k in range(0, m):
                m3[i][j] = m3[i][j] + m1[i][k] * m2[k][j]
    t = time.process_time() - start_time
    return t, m3
def vinograd_multiplication_matrix(m1, m2):
    m = len(m1)   # строки первой
    n = len(m1[0])   # столбцы первой
    q = len(m2[0])   # столбцы второй
    m3 = [[0] * q for i in range(m)]

    row = [0] * m
    for i in range(0, m):
        for j in range(0, n // 2, 1):
            row[i] = row[i] + m1[i][2 * j] * m1[i][2 * j + 1]
 
    col = [0] * q
    for j in range(0, q):
        for i in range(0, n // 2, 1):
            col[j] = col[j] + m2[2 * i][j] * m2[2 * i + 1][j]

    start_time = time.process_time()
    for i in range(0, m):
        for j in range(0, q):
            m3[i][j] = -row[i] - col[j]
            for k in range(0, n // 2, 1):
                m3[i][j] = m3[i][j] + (m1[i][2 * k + 1] + m2[2 * k][j]) * (m1[i][2 * k] + m2[2 * k + 1][j])

    if n % 2 == 1:
        for i in range(0, m):
            for j in range(0, q):
                m3[i][j] = m3[i][j] + m1[i][n - 1] * m2[n - 1][j]       
    t = time.process_time() - start_time
    return t, m3

def vinograd_optimizate_multiplication_matrix(m1, m2):
    m = len(m1)
    n = len(m1[0])
    q = len(m2[0])
    m3 = [[0] * q for i in range(m)]
    row = [0] * m
    for i in range(0, m):
        for j in range(1, n, 2):
            row[i] -= m1[i][j] * m1[i][j - 1]

    col = [0] * q
    for j in range(0, q):
        for i in range(1, n, 2):
            col[j] -= m2[i][j] * m2[i - 1][j]

    flag = n % 2
    start_time = time.process_time()
    for i in range(0, m):
        for j in range(0, q):
            m3[i][j] = row[i] + col[j]
            for k in range(1, n, 2):
                m3[i][j] += (m1[i][k - 1] + m2[k][j]) * (m1[i][k] + m2[k - 1][j])
            if (flag):
                m3[i][j] += m1[i][n - 1] * m2[n - 1][j]
    t = time.process_time() - start_time
    return t, m3
xlist = []
ylist1 = []
ylist2 = []
ylist3 = []
for i in range (101, 501, 100):
    m1 = init_matr(i, i)
    m2 = init_matr(i, i)
    ylist1.append(standart_multiplication_matrix(m1, m2)[0])
    ylist2.append(vinograd_multiplication_matrix(m1, m2)[0])
    ylist3.append(vinograd_optimizate_multiplication_matrix(m1, m2)[0])
    xlist.append(i)

pylab.xlabel('Размер матрицы, символы')
pylab.ylabel('Время, секунды')
pylab.plot(xlist, ylist1, color = 'red', label = 'Стандартный алгоритм')
pylab.plot(xlist, ylist2, color = 'yellow', label = 'Алгоритм Винограда')
pylab.plot(xlist, ylist3, 'b-.', label = 'Оптимизированный алгоритм Винограда')
pylab.legend(loc='upper left')
pylab.show()


xlist = []
ylist1 = []
ylist2 = []
ylist3 = []

for i in range (100, 500, 100):
    m1 = init_matr(i, i)
    m2 = init_matr(i, i)
    ylist1.append(standart_multiplication_matrix(m1, m2)[0])
    ylist2.append(vinograd_multiplication_matrix(m1, m2)[0])
    ylist3.append(vinograd_optimizate_multiplication_matrix(m1, m2)[0])
    xlist.append(i)
                
pylab.xlabel('Размер матрицы, символы')
pylab.ylabel('Время, секунды')
pylab.plot(xlist, ylist1, color = 'red', label = 'Стандартный алгоритм')
pylab.plot(xlist, ylist2, color = 'yellow', label = 'Алгоритм Винограда')
pylab.plot(xlist, ylist3, 'b-.', label = 'Оптимизированный алгоритм Винограда')
pylab.legend(loc='upper left')
pylab.show()





print("Введите размерность матрицы 1 ")
m = int(input("m1 = "))
n = int(input("n1 = "))
print("Введите размерность матрицы 2 ")
k = int(input("m2 = "))
q = int(input("n2 = "))

m1 = init_matr(m, n)
m2 = init_matr(k, q)

if n != k:
    print("Матрицы не могут быть перемножены")
else:
    print("\nМатрица 1: ")
    print_matrix(m1)
    print()
    print("Матрица 2: ")
    print_matrix(m2)
    print("\nСтандартный алгоритм: ")
    t, new_m = standart_multiplication_matrix(m1, m2)
    print_matrix(new_m)
    print("\nАлгоритм Винограда: ")
    t, new_m = vinograd_multiplication_matrix(m1, m2)
    print_matrix(new_m)
    print("\nОптимизированный алгоритм Винограда: ")
    t, new_m = vinograd_optimizate_multiplication_matrix(m1, m2)
    print_matrix(new_m)







