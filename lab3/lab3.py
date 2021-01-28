import random
import pylab
import time

def get_best_arr(n):
    x = random.randint(-1000, 1000)
    arr = list(x + i for i in range(n))
    return arr

def get_worst_arr(n):
    x = random.randint(-1000, 1000)
    arr = list(x - i for i in range(n))
    return arr

def get_random_arr(n):
    arr = list(random.randint(-1000, 1000) for i in range(n))
    return arr

def bubble_sort(arr):
    start_time = time.process_time()
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    t = time.process_time() - start_time
    return t
def insertion_sort(arr):
    start_time = time.process_time()
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    t = time.process_time() - start_time
    return t
def selection_sort(arr):
    start_time = time.process_time()
    for i in range(0, len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    t = time.process_time() - start_time
    return t

c1 = input("Ваш выбор: \n1.Сортировка пузырьком, выбором, вставками (лучший случай)\n2.Сортировка пузырьком, выбором, вставками (средний случай) \n3.Сортировка пузырьком, выбором, вставками (худший случай)")
xlist = []
ylist1 = []
ylist2 = []
ylist3 = []
if (c1 == '1'):
    i = 150
    delta = 200
    dt = 0
    while(i < 3300):         
          arr = get_best_arr(i)
          arr_copy = arr.copy()

          ylist1.append(bubble_sort(arr_copy))
          arr_copy = arr.copy()
 
          ylist2.append(insertion_sort(arr_copy))
          arr_copy = arr.copy()

          ylist3.append(selection_sort(arr_copy))
          xlist.append(i)
          i += delta
          delta += dt
    pylab.xlabel('Размер массива')
    pylab.ylabel('Время, секунды')
    pylab.plot(xlist, ylist1, 'r--', label = 'Сортировка пузырьком')
    pylab.plot(xlist, ylist2, color = 'yellow', label = 'Сортировка вставками')    
    pylab.plot(xlist, ylist3, 'b-.', label = 'Сортировка выбором')
    pylab.legend(loc='upper left')
    pylab.show()
elif (c1 == '2'):
    i = 10
    delta = 100
    dt = 200
    while(i < 8000):
        arr = get_random_arr(i)
        arr_copy = arr.copy()
        ylist1.append(bubble_sort(arr_copy))
        arr_copy = arr.copy()
        ylist2.append(insertion_sort(arr_copy))
        arr_copy = arr.copy()  
        ylist3.append(selection_sort(arr_copy))
        xlist.append(i)
        i += delta
        delta += dt

    pylab.xlabel('Размер массива')
    pylab.ylabel('Время, секунды')
    pylab.plot(xlist, ylist1, 'r--', label = 'Сортировка пузырьком')
    pylab.plot(xlist, ylist2, color = 'yellow', label = 'Сортировка вставками')
                
    pylab.plot(xlist, ylist3, 'b-.', label = 'Сортировка выбором')
    pylab.legend(loc='upper left')
    pylab.show()
elif (c1 == '3'):
    i = 10
    delta = 100
    dt = 350
    while(i < 8000):
        arr = get_worst_arr(i)
        arr_copy = arr.copy()
        ylist1.append(bubble_sort(arr_copy))
        arr_copy = arr.copy()

        ylist2.append(insertion_sort(arr_copy))
        arr_copy = arr.copy()

        ylist3.append(selection_sort(arr_copy))
        xlist.append(i)
        i += delta
        delta += dt
    pylab.xlabel('Размер массива')
    pylab.ylabel('Время, секунды')
    pylab.plot(xlist, ylist1, 'r--', label = 'Сортировка пузырьком')
    pylab.plot(xlist, ylist2, color = 'yellow', label = 'Сортировка вставками')
    pylab.plot(xlist, ylist3, 'b-.', label = 'Сортировка выбором')
    pylab.legend(loc='upper left')
    pylab.show()
else:
    print("Некорректный ввод!\n")


print("Введите массив:")
arr = list(int(i) for i in input().split())
arr_copy = arr.copy()

print("\nРезультат сортировки пузырьком c флагом: ")
bubble_sort(arr_copy)
print(arr_copy)

arr_copy = arr.copy()

print("\nРезультат сортировки вставками: ")
insertion_sort(arr_copy)
print(arr_copy)

arr_copy = arr.copy()

print("\nРезультат сортировки выбором: ")
selection_sort(arr_copy)
print(arr_copy)
            
