import time
import random
import string
import pylab
def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end = ' ')
        print()
    print()
    
# Расстояние Левенштейна   
def levinstein(a, b):
    m = [[i+j if i*j == 0 else 0 for j in range(len(b) + 1)] for i in range (len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range (1, len(b) + 1):
            if a[i-1] == b[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = 1 + min(m[i-1][j], m[i][j-1], m[i-1][j-1])
    #print_matrix(m, len(a) + 1 , len(b) + 1)
    return m[len(a)][len(b)]

# Расстояние Дамерау - Левенштейна
def damerau_levinstein(a, b):
    m = [[i+j if i*j == 0 else 0 for j in range(len(b) + 1)] for i in range (len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = 1 + min(m[i-1][j], m[i][j-1], m[i-1][j-1])
            if (i > 1 and j > 1) and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
                m[i][j] = min(m[i][j], m[i-2][j-2] + 1)
    #print_matrix(m, len(a) + 1 , len(b) + 1)
    return m[len(a)][len(b)]
#Рекурсивное расстояние Левенштейна
def levinstein_recursive(a, b):
    if a ==  "" or b == "": 
        return abs(len(a) - len(b))
    coef = 0 if (a[-1] == b[-1]) else 1
    return min(levinstein_recursive(a, b[:-1]) + 1,
               levinstein_recursive(a[:-1], b) + 1,
               levinstein_recursive(a[:-1], b[:-1]) + coef)

#Рекурсивное расстояние Дамерау-Левенштейна
def damerau_lev_recursion(a, b):
    if a ==  "" or b == "":
        return abs(len(a) - len(b))
    coef = 0 if (a[-1] == b[-1]) else 1
    res = min(damerau_lev_recursion(a, b[:-1]) + 1,
              damerau_lev_recursion(a[:-1], b) + 1,
              damerau_lev_recursion(a[:-1], b[:-1]) + coef)
    if (len(a) >= 2 and len(b) >= 2 and a[-1] == b[-2] and a[-2] == b[-1]):
        res = min(res, damerau_lev_recursion(a[:-2], b[:-2]) + 1)
    return res

def print_table(td):
    from prettytable import PrettyTable  # Импортируем установленный модуль.

    # Определяем твою шапку и данные.
    th = ["A", "B", "Лев", "Дамерау-Лев", "Лев(рек)", "Дамерау-Лев(рек)"]

    columns = len(th)  # Подсчитаем кол-во столбцов на будущее.

    table = PrettyTable(th)  # Определяем таблицу.

    # Cкопируем список td, на случай если он будет использоваться в коде дальше.
    td_data = td[:]
    # Входим в цикл который заполняет нашу таблицу.
    # Цикл будет выполняться до тех пор пока у нас не кончатся данные
    # для заполнения строк таблицы (список td_data).
    while td_data:
        # Используя срез добавляем первые пять элементов в строку.
        # (columns = 5).
        table.add_row(td_data[:columns])
        # Используя срез переопределяем td_data так, чтобы он
        # больше не содержал первых 5 элементов.
        td_data = td_data[columns:]

    print(table)  # Печатаем таблицу
    print()
    
list1 = ["кухня", "", "бабушка", "пила", "кинотеатр"]
list2 = ["снег", "", "бабушка","ипла", "кинооо"]
td = []
for s1, s2 in zip(list1, list2):
    td.append(s1)
    td.append(s2)
    td.append(levinstein(s1, s2))
    td.append(damerau_levinstein(s1, s2))
    td.append(levinstein_recursive(s1, s2))
    td.append(damerau_lev_recursion(s1, s2))
    print_table(td)

#Вывод графика для матричного Левенштейна и Дамерау-Левенштейна 
xlist = []
ylist1 = []
ylist2 = []
for i in range (0, 800, 50):
   s1 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for y in range(i))
   s2 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for y in range(i))
   xlist.append(i)

   start_time = time.process_time()
   levinstein(s1, s2)
   ylist1.append(time.process_time() - start_time)

   start_time = time.process_time()
   damerau_levinstein(s1, s2)
   ylist2.append(time.process_time() - start_time)

pylab.xlabel('Длина слов, символы')
pylab.ylabel('Время, секунды')
pylab.plot(xlist, ylist1, 'r--', label = 'Расстояние Левенштейна матричным способом')
pylab.plot(xlist, ylist2, color = 'yellow', label = 'Расстояние Дамерау-Левенштейна матричным способом')
pylab.legend(loc='upper left')
pylab.show()
#Вывод графика для рекурсивного Левенштейна и Дамерау-Левенштейна и Левештейна матричного
xlist = []
ylist3 = []
ylist4 = []
ylist2 = []
for i in range (0, 11, 2):
    s1 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for y in range(i))
    s2 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for y in range(i))
    xlist.append(i)
    
    start_time = time.process_time()
    levinstein(s1, s2)
    ylist2.append(time.process_time() - start_time)
    

    start_time = time.process_time()
    levinstein_recursive(s1, s2)
    ylist3.append(time.process_time() - start_time)

    start_time = time.process_time()
    damerau_lev_recursion(s1, s2)
    ylist4.append(time.process_time() - start_time)

pylab.xlabel('Длина слов, символы')
pylab.ylabel('Время, секунды')
pylab.plot(xlist, ylist3, color = 'blue', label = 'Расстояние Левенштейна рекурсивным способом')
pylab.plot(xlist, ylist4, color = 'red', label = 'Расстояние Дамерау-Левенштейна рекурсивным способом')
pylab.plot(xlist, ylist2, color = 'yellow', label = 'Расстояние Левенштейна матричным способом')
pylab.legend(loc='upper left')
pylab.show()
