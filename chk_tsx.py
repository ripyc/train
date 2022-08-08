import random, time
from collections import Counter
import itertools

input("КОНЕЦ\n\n")



input("КОНЕЦ\n\n")

while True:
    try:
        n = int(input("Введите целое число:\n"))
    except ValueError:
        print("Вы должны ввести число!\n")
    else:
        if 1 <= n <= 998:
            break
        else:
            print("Число должно быть от 1 до 998\n")
start_time = time.time()
def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n-1)
print(str(n) + "! = " + str(faktorial(n)))
print("\n--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
fakt = 1
for k in range(n):
    fakt *= k + 1
print("\n" + str(n) + "! = " + str(fakt))
print("(получено с помощью цикла)")
print("\n--- %s seconds ---"

input("КОНЕЦ\n\n")

n = int(input("Введите номер числа Фибоначчи:\n"))
start_time = time.time()
#  Последние цифры числа Фиббоначи повторяются после номера 60, поэтому создадим массив:
fib60 = ['1', '1', '2', '3', '5', '8', '3', '1', '4', '5', '9', '4', '3', '7', '0', '7', '7', '4', '1', '5',
         '6', '1', '7', '8', '5', '3', '8', '1', '9', '0', '9', '9', '8', '7', '5', '2', '7', '9', '6', '5',
         '1', '6', '7', '3', '0', '3', '3', '6', '9', '5', '4', '9', '3', '2', '5', '7', '2', '9', '1', '0']
print("Последняя цифра числа Фибоначчи, под №%s:" % n)
print(fib60[n % 60])
print("\n--- %s seconds ---" % (time.time() - start_time))

input("КОНЕЦ\n\n")


while True:
    try:
        n = int(input("Введите номер числа Фибоначчи:\n"))
    except ValueError:
        print("Вы должны ввести число!\n")
    else:
        if 0 <= n <= 998:
            break
        else:
            print("Номер должен быть от 0 до 998\n")

start_time = time.time()
fib = [1, 1]
def fibonacci(number):
    if number < len(fib):
        return fib[number]
    else:
        fib.append(fibonacci(number-1) + fibonacci(number-2))
    return fib[number]


print("Число Фибоначии F №%s, равное сумме двух предыдущий членов ряда:" % n)
print(fibonacci(n))
print(fib)
print("\n--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
fib0 = fib1 = 1
while n > 0:
    fib0, fib1 = fib1, fib0 + fib1
    n -= 1
print("Число Фибоначчи, вычисленное без рекурсии за O(1):")
print(fib0)
print("\n--- %s seconds ---" % (time.time() - start_time))

input("КОНЕЦ\n\n")

start_time = time.time()
n = 10
print("Количество ступенек: %i" % n)
steps = []
for indx in range(n):
    steps.append(random.randint(0, 3))
print("На каждой ступеньке написано на какое максимальное количество с неё можно прыгнуть:")
print(steps)

def can_up(stairs):
    if len(stairs) == 1:  # если ступенька одна, то мы сразу на неё встанем и будем на верху лестницы
        return True
    else:
        for number in range(len(stairs)):  # если же ступенек две и более, то начинаем по ним подниматься
            if stairs[number] == 0:  # когда нам попадается нулевая ступенька - нужно проверить можно ли её перепрыгнуть
                step_down = 1  # шаг назад
                # Пока значение значение ступеньки, на которую мы опустились не превысит количесвто шагов назад
                # продолжаем спускаться вниз по лестнице, если достигли дна, возвращаем false
                while stairs[number - step_down] <= step_down:
                    step_down += 1
                    if step_down == number+1:
                        return False
    return True

print(can_up(steps))
if can_up(steps) == True:
    print("По этой лестнице МОЖНО подняться!")
else:
    print("По этой лестнице НЕЛЬЗЯ подняться!")

print("\n--- %s seconds ---" % (time.time() - start_time))

input("КОНЕЦ\n\n")

start_time = time.time()
n = random.randint(1, 1000)
print("Количесвто домов: " + str(n))
k = random.randint(1, 10000)
print("Общий бюджет: " + str(k))
homes = []
for indx in range(n):
    homes.append(random.randint(1, 10000))
print("\nСписок домов по стоимости:")
print(homes)
homes.sort()
max_homes = 0
for cost in homes:
    if cost > k:
        break
    else:
        max_homes += 1
        k -= cost
print("\nНаибольшее число домов, которое можно купить: " + str(max_homes))
print("\n--- %s seconds ---" % (time.time() - start_time))

input("КОНЕЦ\n\n")

start_time = time.time()
input_str = ""
for indx in range(10000):
    input_str += random.choice(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
print("Введённая строка:\n" + input_str)
print("Количество букв в последнем слове: "+ str(len(input_str.split()[-1])))
print("--- %s seconds ---" % (time.time() - start_time))

input("КОНЕЦ\n\n")

while True:
    try:
        n = int(input("\nВведите количество чисел в массиве:\n"))
    except ValueError:
        print("Ошибка. Нужно ввести целочисленное значение!")
    else:
        if 0 < n <= 10000:
            break
        else:
            print("Ошибка. Значение должно быть больше нуля, но не превышать десять тысяч!")
print("Массив, заполненный числами:")
massive = []
for indx in range(n):
    massive.append(random.randint(1, 9))
    print(massive[indx], end=" ")
print("\nСамая длинная возрастающая подпоследовательность в данном массиве имеет длину:")
massive_row = 1
massive_row_max = 1
for indx in range(n-1):
    if massive[indx] < massive[indx+1]:
        massive_row += 1
        if massive_row > massive_row_max:
            massive_row_max = massive_row
    else:
        massive_row = 1
print(massive_row_max)

input("КОНЕЦ\n\n")

n = int(input("Введите количество строк:\n"))
m = int(input("Введите количество столбцов:\n"))

print("Заполненная матрица:")
matrix = []
for row in range(n):
    matrix_row = []
    for column in range(m):
        elem = random.randint(-100, 100)
        print(elem, end="   \t")
        matrix_row.append(elem)
    print("\n")
    matrix.append(matrix_row)
print("Проход по матрице по спирали:")
spiral = []
while matrix:  # пока существует матрица
    for elem in matrix[0]:
        #print(elem)
        spiral.append(elem)  # добавляем по очереди каждый элемент из первой строки
    del matrix[0]  # удаляем первую строку
    for indx in range(len(matrix)):
        #print(matrix[indx][-1])
        spiral.append(matrix[indx][-1])  # добавляем последний элемент каждой строки
        del matrix[indx][-1]  # потом удаляем его
    for elem in reversed(matrix[-1]):
        #print(elem)
        spiral.append(elem)  # добавляем в обратном порядке каждый элемент из последней строки
    del matrix[-1]  # удаляем последнюю строку
    for indx in range(len(matrix)):
        #print(matrix[len(matrix)-1-indx][0])
        spiral.append(matrix[len(matrix)-1-indx][0])  # добавляем первый элемент каждой строки с конца (снизу)
        del matrix[len(matrix)-1-indx][0]  # потом удаляем его
print(spiral)

input("КОНЕЦ\n\n")

n = int(input("Введите количество строк:\n"))
m = int(input("Введите количествобукв в каждой строке:\n"))
matrix = []
for indx in range(n):
    a = ""
    for letter in range(m):
        a += random.choice("abcdefgh")  # буквы без ijklmnopqrstuvwxyz
    matrix.append(a)
    print(a)
del_column_qt = 0
for column_indx in range(m):
    for indx in range(n-1):
        if matrix[indx][column_indx] > matrix[indx+1][column_indx]:
            del_column_qt += 1
            break
print("Чтобы все столбцы были неубывающими последовательностями нужно удалить: " + str(del_column_qt) + " из них")


input("КОНЕЦ\n\n")

kids = int(input("Введите количество детей:\n"))
factor = []
print("Фактор жадности этих ребят:")
for indx in range(kids):
    factor.append(random.randint(1, 5))
    print(factor[indx], end=" ")
cookies_qt = int(input("\nВведите количество печенек:\n"))
cookies = []
print("Размеры каждой из них:")
for indx in range(cookies_qt):
    cookies.append(random.randint(1, 5))
    print(cookies[indx], end=" ")
print("\n\nЖадность к Печенькам:")
factor.sort()
cookies.sort()
print(factor)
print(cookies)
happy_kids = 0
cookindx = 0
for indx in range(kids):
    while factor[indx] > cookies[cookindx]:
        cookindx += 1
        if cookindx + 1 >= cookies_qt:
            break

    if cookindx + 1 >= cookies_qt:
        break
    else:
        cookindx += 1
        happy_kids += 1

print("\nЧисло довольных детей:" + str(happy_kids))

input("КОНЕЦ\n\n")

max_mass = float(input("Введите вместимость рюкзака:\n"))
things_qt = int(input("Введите количество вещей в магазине:\n"))
things = []
for indx in range(things_qt):
    things.append([round(random.uniform(10, 1000), 2), round(random.uniform(0.1, 5), 1), indx+1])
    print("Товар №" + str(things[indx][2]) + "\tЦена: " + str(things[indx][0]) + "  \t Вес: " + str(things[indx][1]))
things.sort(reverse=True)
things_in_bag = []
for indx in range(things_qt):
    if things[indx][1] <= max_mass:
        max_mass -= things[indx][1]
        things_in_bag.append(things[indx][2])
print("Товары, которые кладём в рюкзак методом наибольшей стоимости (в порядке увеличения ценности):")
print(things_in_bag)

input("КОНЕЦ\n\n")

str = ""
for indx in range(15000):
    str += random.choice("abcdefghijklmnopqrstuvwxyz")
print("Последовательность букв:")
print(str)
chn_str = input("Введите искомую подпоследовательность:\n")

index_chn_str = 0
for elem in str:
    if elem == chn_str[index_chn_str]:
        index_chn_str += 1
        if index_chn_str == len(chn_str):
            print("Введённая подпоследовательность содержится в последовательности")
            break

if index_chn_str < len(chn_str):
    print("Строка НЕ является подпоследовательностью")


input("КОНЕЦ\n\n")


while True:
    try:
        days = int(input("Введите количество дней с котировками:\n"))
    except ValueError:
        print("Нужно ввести целое число!")
    else:
        if 1 < days < 1001:
            break
        else:
            print("Нужно ввести число от 2 до 1000!")

quots = []
for indx in range(days):
    quots.append(random.randint(1, 20))
    print(quots[indx], end=" ")

profit = 0
buy = quots[0]
for indx in range(1, days-1):  # пробегаемся по списку начиная со второго элемента
    if indx == days-1 and quots[days] > buy:  # если котировка в последний день больше цены покупки
        profit += quots[days] - buy  # то продаем в последний день и фиксируем прибыль
    elif quots[indx] > buy:  # если цена акции больше чем котировка покупки
        if quots[indx] > quots[indx+1]:  # и если цена акции больше чем стоимость на следующий день
            profit += quots[indx] - buy  # то фиксируем прибыль
            buy = quots[indx+1]  # и покупаем на следующий день
    else:  # если цена акции меньше котировки покупки
        buy = quots[indx]  # то покупаем по этой цене, а в другой день как будто не покупали

print("\nМаксимальная прибыль: " + str(profit))

input("КОНЕЦ\n\n")

# Время начала и конца уроков
lessons = [[9, 10], [9.3, 10.3], [10, 11], [10.3, 11.3], [11, 12]]
lessons2 = [[9, 10], [11, 12.25], [12.15, 13.3]]
lessons3 = [[19, 19], [7, 14], [12, 14], [8, 22], [22, 23], [5, 21], [9, 23]]


def sorted_by_end_of_lesson(lsn_lst):
    # Переворачиваем время окончания и начала, затем сортируем лист уроков по времени окончания:
    for lsn_time in lsn_lst:
        lsn_time.reverse()
    lsn_lst.sort()
    # Пробегаемся по отсортированному списку уроков, и если время начала более поздно заканчивающегося урока
    # раньше чем время окончания предыдущего, то удаляем его (не забыв уменьшить индекс пробегания):
    indx = 1
    while indx < len(lsn_lst):
        if lsn_lst[indx][1] < lsn_lst[indx - 1][0]:
            del lsn_lst[indx]
            indx -= 1
        indx += 1
    # Переворачиваем начало и окончание уроков обратно и возвращаем этот список:
    for lsn_time in lsn_lst:
        lsn_time.reverse()
    return lsn_lst


print(lessons)
print(sorted_by_end_of_lesson(lessons))
print()
print(lessons2)
print(sorted_by_end_of_lesson(lessons2))
print()
print(lessons3)
print(sorted_by_end_of_lesson(lessons3))


input("КОНЕЦ\n\n")


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(node):
    has_cycle = False
    uninames = set()
    uninames_amt = 0
    while node is not None:
        uninames.add(node)
        uninames_amt += 1
        node = node.next

        if uninames_amt > len(uninames):
            has_cycle = True
            break
    return has_cycle


# Задаём связанный список с головой n1:
n7 = Node("воскресенье")
n6 = Node("суббота", n7)
n5 = Node("пятница", n6)
n4 = Node("четверг", n5)
n3 = Node("среда", n4)
n2 = Node("вторник", n3)
n1 = Node("понедельник", n2)
n6.next = n1  # понедельник начинается в субботу
print(hasCycle(n1))


input("КОНЕЦ\n\n")


while True:
    calc_str = input("Введите обратную польскую запись:\n")
    split_calc_str = calc_str.split()
    # Проверка, что строка содержит только цифры и операнды:
    if not set(calc_str) <= set(" *+-/0123456789"):
        print("Необходимо ввести числа, используя цифры 0-9 и знаки операций сложения '+', вычитания '-', "
              "умножения '*' или деления '/' (целочисленное), разделённые пробелами")
    # Проверка, что строка не начинается с операнда:
    elif calc_str[0] in "+-*/":
        print("Ошибка ввода, строка начинается со знака, не с числа")
    elif len(split_calc_str) < 3:
        print("Ошибка ввода")
    else:
        break


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(int(item))

    def pop(self):
        if not self.items:
            return "error"
        else:
            self.items.pop()

    def sum(self):
        if len(self.items) > 1:
            self.items[-2] += self.items[-1]
            self.items.pop()
        else:
            return "error"

    def plus(self):
        if len(self.items) > 1:
            self.items[-2] += self.items[-1]
            self.items.pop()
        else:
            return "error"

    def minus(self):
        if len(self.items) > 1:
            self.items[-2] -= self.items[-1]
            self.items.pop()
        else:
            return "error"

    def multi(self):
        if len(self.items) > 1:
            self.items[-2] *= self.items[-1]
            self.items.pop()
        else:
            return "error"

    def times(self):
        if len(self.items) > 1:
            self.items[-2] = self.items[-2] // self.items[-1]
            self.items.pop()
        else:
            return "error"


stack = Stack()
stack.pop()

for elem in split_calc_str:
    if set(elem) <= set("0123456789"):
        stack.push(elem)
    elif str(elem) == "+":
        if stack.plus() == "error":
            print("Неккоректная строка")
        else:
            stack.plus()

    elif str(elem) == "-":
        if stack.minus() == "error":
            print("Неккоректная строка")
        else:
            stack.minus()

    elif str(elem) == "*":
        if stack.multi() == "error":
            print("Неккоректная строка")
        else:
            stack.multi()

    elif str(elem) == "/":
        if stack.times() == "error":
            print("Неккоректная строка")
        else:
            stack.times()
    else:
        print("Неккоректная строка")

print(str(stack.items))


input("КОНЕЦ\n\n")


class Node4dek:
    def __init__(self, value=None, next_item=None, prev_item=None):
        self.value = value
        self.next_item = next_item
        self.prev_item = prev_item


class MyDekNode:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.head = None
        self.tail = None

    def put_front(self, elem):
        print(f"Вносится элемент {str(elem)} в начало Дека")
        node = Node4dek(elem)
        if self.size == self.max_size:
            print(f"Дек переполнен! Внесение не удалось")
        elif self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.head.next_item = node
            node.prev_item = self.head
            self.head = node
            self.size += 1

    def put_back(self, elem):
        print(f"Вносится элемент {str(elem)} в конец Дека")
        node = Node4dek(elem)
        if self.size == self.max_size:
            print(f"Дек переполнен! Внесение не удалось")
        elif self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.prev_item = node
            node.next_item = self.tail
            self.tail = node
            self.size += 1

    def get_front(self):
        if self.size == 0:
            print(f"Дек пуст! Удаление элемента в начале Дека не удалось")
        elif self.size == 1:
            print(f"Удаляется {self.head.value} - последний элемент из Дека")
            self.size = 0
            self.head = None
            self.tail = None
        else:
            print(f"Удаляется элемент {self.head.value} из начала Дека")
            self.head = self.head.prev_item
            self.head.next_item = None
            self.size -= 1

    def get_back(self):
        if self.size == 0:
            print(f"Дек пуст! Удаление элемента в конце Дека не удалось")
        elif self.size == 1:
            print(f"Удаляется {self.tail.value} - последний элемент из Дека")
            self.size = 0
            self.head = None
            self.tail = None
        else:
            print(f"Удаляется элемент {self.tail.value} из конца Дека")
            self.tail = self.tail.next_item
            self.tail.prev_item = None
            self.size -= 1


d = MyDekNode(6)
print(f"Создан Дек с максимальным размером {d.max_size} элементов")
d.put_front(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.put_front(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.put_front(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.put_back(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.put_back(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.put_front(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.put_front(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.put_back(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.get_back()
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.get_back()
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.get_front()
d.get_front()
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.get_front()
d.get_front()
d.get_front()
d.get_front()
d.put_back(random.randint(-100, 100))
d.put_back(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")
d.put_front(random.randint(-100, 100))
d.put_front(random.randint(-100, 100))
print(f"Дек имеет {d.size} элементов из {d.max_size}, в начале: {d.head.value}, в конце: {d.tail.value}")


input("КОНЕЦ\n\n")


class Node4queue:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


class MyQueueNode:
    def __init__(self):
        self.size = 0  # текущий размер очереди
        self.head = None  # голова очереди
        self.tail = None  # хвост очереди

    def push(self, elem):
        print("Внесён элемент: " + str(elem))
        node = Node4queue(elem)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next_item = node
            self.tail = node
        self.size += 1

    def pop(self):
        if not self.head:
            print("error, очередь пуста")
        else:
            print("Уходит элемент: " + str(self.head.value))
            self.head = self.head.next_item
            self.size -= 1


o = MyQueueNode()
print("Размер очереди: " + str(o.size))
o.push(5)
o.push(15)
print("Размер очереди: " + str(o.size))
print("Первый в очереди: " + str(o.head.value))
print("В хвосте очереди: " + str(o.tail.value))
o.pop()
print("Размер очереди: " + str(o.size))
print("Первый в очереди: " + str(o.head.value))
print("В хвосте очереди: " + str(o.tail.value))
o.pop()
o.pop()
print("Размер очереди: " + str(o.size))
o.push(5)
o.push(15)
print("Размер очереди: " + str(o.size))
print("Первый в очереди: " + str(o.head.value))
print("В хвосте очереди: " + str(o.tail.value))
o.push(25)
o.push(45)
o.push(15)
o.push(35)
print("Размер очереди: " + str(o.size))
print("Первый в очереди: " + str(o.head.value))
print("В хвосте очереди: " + str(o.tail.value))

input("КОНЕЦ\n\n")


rnd_str = ""
for i in range(10000):
    rnd_str += random.choice("abcdefgh")
print("Анализируемая строка:")
print(rnd_str)
while True:
    search_ag = str(input("Введите искомую анаграмму:\n"))
    if 0 < len(search_ag) < len(rnd_str):
        break
    elif search_ag == "":
        print("Строка не должна быть пустой!")
    else:
        print("Анаграмма должна быть короче аналзируемой строки!")

len_ag = len(search_ag)
list_ag = []
sort_ag = sorted(search_ag)

for i in range(len(rnd_str) - len_ag + 1):
    if sorted(rnd_str[i:(i+len_ag)]) == sort_ag:
        list_ag.append(rnd_str[i:(i+len_ag)])

print("В строке " + str(len(list_ag)) + " анаграмм:")
print(list_ag)

input("КОНЕЦ\n\n")


class MyQueueSize:
    def __init__(self, max_size):
        self.items = [None for _ in range(max_size)]
        self.max_size = max_size
        self.size = 0  # текущий размер очереди
        self.head = 0  # индекс места входа в очереди
        self.tail = 0  # индекс хвоста очереди

    def __str__(self):
        return "".join(self.items.__str__())

    def is_empty(self):
        return len(self.items) == []

    def push(self, item):
        if self.size != self.max_size:
            print("Добавляем " + str(item) + " в хвост очереди")
            self.items[self.tail] = item
            self.size += 1
            self.tail = (self.tail + 1) % self.max_size
        else:
            print("Очередь переполнена, не удаётся добавить " + str(item))

    def pop(self):
        if self.is_empty():
            print("Очередь итак пустая")
            return None
        print("Удаляется элемент: " + str(self.items[self.head]) + " (с позиции " + str(self.head + 1) + ")")
        self.items[self.head] = None
        self.size -= 1
        self.head = (self.head + 1) % self.max_size

    def peek(self):
        print("Первый элемент в очереди: " + str(self.items[self.head]) + " (на позиции " + str(self.head + 1) + ")")


o = MyQueueSize(5)
print(o)
o.push(5)
o.peek()
o.push(4)
o.peek()
o.push(1)
o.peek()
print(o)
o.push(2)
o.peek()
print(o)
o.push(3)
o.peek()
print(o)
o.push(2)
o.peek()
print(o)
o.pop()
print(o)
o.peek()
o.pop()
print(o)
o.peek()


input("КОНЕЦ\n\n")


class MyQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "".join(self.items.__str__())

    def push(self, item):
        print("Добавляемый элемент: " + str(item))
        self.items.append(item)

    def pop(self):
        if self.items:
            print("Удаляемый элемент: " + str(self.items[0]))
            self.items.pop(0)
        else:
            print("error, очередь пуста")

    def peek(self):
        if self.items:
            print("Первое число в очереди: " + str(self.items[0]))
        else:
            print("error, очередь пуста")

    def size(self):
        print("Размер очереди: " + str(len(self.items)))

    def is_empty(self):
        return len(self.items) == []


o = MyQueue()
print(o)
o.push(1)
print(o)
o.push(2)
print(o)
o.push(3)
print(o)
o.push(2)
print(o)
o.pop()
print(o)
o.size()
o.peek()


input("КОНЕЦ\n\n")


a = input("Введите скобочную последовательность для проверки:\n")
b = []
for i in range(len(a)):
    if a[i] == "(" or a[i] == "[" or a[i] == "{":
        b.append(a[i])
    elif a[i] == ")":
        if not b:
            b.append(" ")
            break
        if b[-1] == "(":
            b.pop()
        else:
            break
    elif a[i] == "}":
        if not b:
            b.append(" ")
            break
        if b[-1] == "{":
            b.pop()
        else:
            break
    elif a[i] == "]":
        if not b:
            b.append(" ")
            break
        if b[-1] == "[":
            b.pop()
        else:
            break

if not b:
    print(True)
else:
    print(False)

input("КОНЕЦ\n\n")


a = input("Введите скобочную последовательность для проверки:\n")
while "()" in a or "{}" in a or "[]" in a:
    a = a.replace("()", "")
    a = a.replace("[]", "")
    a = a.replace("{}", "")
if a == "":
    print(True)
else:
    print(False)

input("КОНЕЦ\n\n")


def is_correct_bracket_seq(hooks):
    itis = True
    while itis is True:
        if hooks == "":
            break
        if len(hooks) % 2 == 1:
            itis = False

        for i in range(len(hooks)-1):
            if hooks[i] == "(" and hooks[i+1] == ")":
                hooks = hooks[:i] + hooks[i+2:]
                break
            elif hooks[i] == "[" and hooks[i+1] == "]":
                hooks = hooks[:i] + hooks[i+2:]
                break
            elif hooks[i] == "{" and hooks[i+1] == "}":
                hooks = hooks[:i] + hooks[i+2:]
                break
            elif i == len(hooks)-2:
                itis = False
                break

    if len(hooks) > 0:
        itis = False
    return itis


a = "{[()]}"
print(a + " -> " + str(is_correct_bracket_seq(a)))
a = input("Введите скобочную последовательность для проверки:\n")
if is_correct_bracket_seq(a):
    print("Введена правильная скобочная последовательность")
else:
    print("Cкобочная последовательность НЕПРАВИЛЬНАЯ!")


input("КОНЕЦ\n\n")


class StackSet:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "".join(self.items.__str__())

    def push(self, item):
        if item not in self.items:
            self.items.append(item)
            print("Добавлен элемент: " + str(item))
        else:
            print("Элемент: " + str(item) + " уже в стеке и не может быть добавлен")

    def pop(self):
        if self.items:
            print("Удаление текущей вершины - " + str(self.items[-1]))
            self.items.pop()
        else:
            print("удаление error")

    def peek(self):
        if not self.items:
            print("вершина error")
        else:
            print("Вершина: " + str(self.items[-1]))

    def size(self):
        print("Количество элементов в стеке: " + str(len(self.items)))


stack = StackSet()

stack.push(1)
stack.push(2)
stack.size()
stack.pop()
stack.size()
stack.push(1)
stack.size()
stack.peek()
stack.pop()
stack.size()
stack.pop()
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(5)
stack.size()
stack.peek()
stack.push(2)
stack.push(3)
stack.push(4)
stack.size()
stack.peek()
stack.pop()
stack.peek()
stack.size()

print("Окончательный список: " + str(stack))

input("КОНЕЦ\n\n")


class StackMaxEffective:
    def __init__(self):
        self.items = []

    # Добавляем пару: элемент и текущий максимум списка
    def push(self, item):
        if not self.items:
            self.items.append([item, item])  # первый максимум равен самому элементу
        else:
            if item < self.items[-1][1]:  # если добавляемый элемент меньше текущего максимума
                self.items.append([item, self.items[-1][1]])  # то добавляем элемент и сохраняем максимум
            else:
                self.items.append([item, item])  # в противном случае добавляем элемент и обновляем текущий максимум

    def pop(self):
        return self.items.pop()

    def get_max(self):
        get_max = None
        if self.items:
            get_max = self.items[-1][1]
        return get_max


while True:
    try:
        comands_qt = int(input("Введите число операций:\n"))
    except ValueError:
        print("Введены запрещённые символы! Попробуйте снова...")
    else:
        if 0 < comands_qt <= 1000:
            break
        print("Операций должно быть больше одной, но не больше 1000!")

# Создаём экземпляр класса:
stack = StackMaxEffective()

# Добавляем, убираем, выводим максимум:
for i in range(comands_qt):
    command = random.choice(["Добавить в стек", "Удалить с вершины стека", "Вывести текущий максимум"])
    if command == "Добавить в стек":
        x = random.randint(-20, 20)
        print("\n(" + str(i+1) + ") " + command + " число: " + str(x))
        stack.push(x)
        print("Стек стал иметь вид:")
        stack_str = ""
        for i in range(len(stack.items)):
            stack_str += str(stack.items[i][0]) + " "
        print(stack_str)

    if command == "Удалить с вершины стека":
        print("\n(" + str(i+1) + ") " + command + " последнее число")
        if not stack.items:
            print("error")
        else:
            stack.pop()
            if not stack.items:
                print("Стэк стал пустым")
            else:
                print("Стек стал иметь вид:")
                stack_str = ""
                for i in range(len(stack.items)):
                    stack_str += str(stack.items[i][0]) + " "
                print(stack_str)

    if command == "Вывести текущий максимум":
        print("\n(" + str(i+1) + ") " + command + ":\n" + str(stack.get_max()))


input("КОНЕЦ\n\n")


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class StackMax(Stack):
    def get_max(self):
        maximum = None
        if not self.isEmpty():
            maximum = self.items[0]
            for elem in self.items:
                if elem > maximum:
                    maximum = elem
        return maximum


while True:
    try:
        comands_qt = int(input("Введите число операций:\n"))
    except ValueError:
        print("Введены запрещённые символы! Попробуйте снова...")
    else:
        if 0 < comands_qt <= 1000:
            break
        print("Операций должно быть больше одной, но не больше 1000!")

# Создаём экземпляр класса:
stack = StackMax()

# Добавляем, убираем, выводим максимум:
for i in range(comands_qt):
    command = random.choice(["Добавить в стек", "Удалить с вершины стека", "Вывести текущий максимум"])
    if command == "Добавить в стек":
        x = random.randint(-20, 20)
        print("\n(" + str(i+1) + ") " + command + " число: " + str(x))
        stack.push(x)
        print("Стек стал иметь вид:")
        print("".join(stack.items.__str__()))
    if command == "Удалить с вершины стека":
        print("\n(" + str(i+1) + ") " + command + " последнее число")
        if stack.isEmpty():
            print("error")
        else:
            stack.pop()
            if stack.isEmpty():
                print("Стэк стал пустым")
            else:
                print("Стек стал иметь вид:")
                print("".join(stack.items.__str__()))
    if command == "Вывести текущий максимум":
        print("\n(" + str(i+1) + ") " + command + ":\n" + str(stack.get_max()))


input("КОНЕЦ\n\n")


class DoubleConnectedNode:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value


def dblconlst_reverse_print(node):
    while node.next is not None:
        node = node.next
    while node is not None:
        print(node.value)
        node = node.prev
    pass


# Задаём связанный список с головой n1 и хвостом n10:
n1 = DoubleConnectedNode("первый")
n2 = DoubleConnectedNode("второй")
n3 = DoubleConnectedNode("третий")
n4 = DoubleConnectedNode("четвёртый")
n5 = DoubleConnectedNode("пятый")
n6 = DoubleConnectedNode("шестой")
n7 = DoubleConnectedNode("сельмой")
n8 = DoubleConnectedNode("восьмой")
n9 = DoubleConnectedNode("девятый")
n10 = DoubleConnectedNode("десятый")
n1.next, n2.next, n3.next, n4.next, n5.next, n6.next, n7.next, n8.next, n9.next, n10.next = \
    n2, n3, n4, n5, n6, n7, n8, n9, n10, None
n1.prev, n2.prev, n3.prev, n4.prev, n5.prev, n6.prev, n7.prev, n8.prev, n9.prev, n10.prev = \
    None, n1, n2, n3, n4, n5, n6, n7, n8, n9


print("Список (с хвоста):")
dblconlst_reverse_print(n1)

input("КОНЕЦ\n\n")


class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def list_print(node):
    while node is not None:
        print(node.value)
        node = node.next_item
    pass


def list_del_index(node, indx):
    current = node
    prev = None
    for i in range(indx):
        prev = current
        if current.next_item is not None:
            current = current.next_item
        else:
            print("Такой элемент не найден!")
            break
    prev.next_item = current.next_item
    pass


def list_found_elem(node, elem):
    indx = 1
    current = node
    while current.value != elem:
        current = current.next_item
        indx += 1
        if current.next_item is None:
            return None
    return indx


# Задаём связанный список с головой n1:
n10 = Node("десятый")
n9 = Node("девятый", n10)
n8 = Node("восьмой", n9)
n7 = Node("седьмой", n8)
n6 = Node("шестой", n7)
n5 = Node("пятый", n6)
n4 = Node("четвёртый", n5)
n3 = Node("третий", n4)
n2 = Node("второй", n3)
n1 = Node("первый", n2)

print("Список:")
list_print(n1)
del_index = int(input("\nВведите номер элемента, который нужно удалить:\n"))
list_del_index(n1, del_index-1)
print("Скорректированный список:")
list_print(n1)
found_elem = input("\nВведите элемент, который хотите найти:\n")
print("Искомый элемент имеет индекс: " + str(list_found_elem(n1, found_elem)))


input("КОНЕЦ\n\n")


while True:
    try:
        m = int(input("Введите количество строк:\n"))
        n = int(input("Введите количество столбцов:\n"))
    except ValueError:
        print("\nВведены запрещённые символы! Начнём сначала!\n")
    else:
        if 2 <= m <= 100 and 2 <= n <= 100:
            break
        print("Введённые числа должны быть в диапазоне от 2 до 100!")

print("\nСгенерирована матрица:")
matrix = []
for i in range(m):
    m_string = []
    for j in range(n):
        m_string.append(str(random.randint(0, 100)))
    matrix.append(m_string)
    print("\t".join(matrix[i]))

print("\nВведите координаты элемента, соседей которого хотите увидеть.")
while True:
    try:
        y = int(input("Введите номер строки:\n"))
        x = int(input("Введите номер столбца:\n"))
    except ValueError:
        print("\nВведены запрещённые символы!\n")
    else:
        if 1 <= y <= m and 1 <= x <= n:
            break
        elif y > m:
            print("Номер строки превышает размер матрицы!")
        elif x > n:
            print("Номер столбца превышает размер матрицы!")
        else:
            print("Такого элемента нет!")
    print("\nЕщё раз...\n")

print("В строке " + str(y) + ", столбце " + str(x) + " находится элемент: " + str(matrix[y-1][x-1]))


def near_elem(horizontal, vertical):
    near_elements = []
    # Добавляем в массив соседей верхний и левый элемент:
    if horizontal >= 1:
        near_elements.append(matrix[horizontal - 1][vertical])
    if vertical >= 1:
        near_elements.append(matrix[horizontal][vertical - 1])
    # Пробуем добавить нижний и правый элемент:
    try:
        near_elements.append(matrix[horizontal+1][vertical])
        near_elements.append(matrix[horizontal][vertical + 1])
    except IndexError:  # Если их не существует, то ничего не делаем
        pass
    return " ".join(near_elements)


print("Соседние элементы: " + str(near_elem(y-1, x-1)))

input("КОНЕЦ\n\n")


stroka = str(input("Введите строку:\n"))
max_string_various_symbols = []
curmax = []
for i in range(len(stroka)):
    if stroka[i] in curmax:
        index_repeat = curmax.index(stroka[i])+1
        # Обрезаем текущую максимальную подстроку с первого вхождения повторяющегося элемента:
        curmax = curmax[index_repeat:]
    curmax.append(stroka[i])
    if len(max_string_various_symbols) < len(curmax):
        max_string_various_symbols = curmax

print("Длина наибольшей подстроки, которая не содержит повторяющиеся символы: " + str(len(max_string_various_symbols)))
print("Найденная подстрока: " + "".join(max_string_various_symbols))

input("КОНЕЦ\n\n")


while True:
    try:
        m = int(input("Введите количество строк:\n"))
        n = int(input("Введите количество столбцов:\n"))
    except ValueError:
        print("\nВведены запрещённые символы! Начнём сначала!\n")
    else:
        if 2 <= m <= 100 and 2 <= n <= 100:
            break
        print("Введённые числа должны быть в диапазоне от 2 до 100!")

print("\nСгенерирована матрица:")
matrix = []
for i in range(m):
    m_string = []
    for j in range(n):
        m_string.append(str(random.randint(0, 100)))
    matrix.append(m_string)
    print("\t".join(matrix[i]))

print("\nТранспортированная матрица:")
matrix_inv = []
for i in range(n):
    m_string = []
    for j in range(m):
        m_string.append(matrix[j][i])
    matrix_inv.append(m_string)
    print("\t".join(matrix_inv[i]))


input("КОНЕЦ\n\n")


while True:
    try:
        section_amt = int(input("Введите количество секций:\n"))
    except ValueError:
        print("Введены запрещённые символы! Попробуйте снова...")
    else:
        if 2 <= section_amt <= 10000:
            break
        print("Введённое число должно быть в диапазоне от 2 до 10000!")

section_lst = ["вышивание крестиком",    "рисование мелками",    "нестольный теннис",
              "африканская кухня",      "тяжелая атлетика",     "изучение насекомых",
              "питоноведение",          "авиамоделирование",    "папье маше",
              "народные частушки",      "каякинг",              "кузнечное дело",
              "стрельба",               "туризм",               "культурные места Санкт-Петербурга", ]

print("Список кружков всех учеников:")
section_ppl = []
for i in range(section_amt):
    section_ppl.append(section_lst[random.randint(0, len(section_lst)-1)])
    print(section_ppl[i])

section_unique = set(section_ppl)
print("_"*25)
print("Количество уникальных секций - " + str(len(section_unique)) + str(":"))
for section in section_unique:
    print(section)

input("КОНЕЦ\n\n")

c = [1, 2, 3, 4, 5, 6]
print(c)

for i in range(len(c)//2):
    c[i*2], c[i*2+1] = c[i*2+1], c[i*2]

print(c)

input("КОНЕЦ\n\n")


def points_input():
    p = []
    while True:
        try:
            days = int(input("Введите количество дней:\n"))
        except ValueError:
                print("Введены запрещённые символы! Попробуйте снова...")
        else:
            if 3 <= days <= 2000:
                break
            print("Введённое число должно быть в диапазоне от 3 до 2000!")
    for i in range(days):
        p.append(random.randint(-100, 100))
    return p


points = points_input()
print("Сгенерируемый список очков:")
print(points)


combi3 = []
for i in itertools.combinations(points, 3):
    combi3.append(i)

multi3 = []
for i in combi3:
    points_sum = 0
    mult = 1
    for j in i:
        points_sum += j
        mult *= j
    if points_sum == 0:
        multi3.append(mult)


multi3.sort()
multi3.reverse()
print(multi3)
print("Максимальное произведение очков за 3 дня, сумма в которые равна 0 (-1 если нет подходящих):")
if len(multi3) == 0:
    print(-1)
elif multi3[0] <= 0:
    print(-1)
else:
    print(multi3[0])


input("КОНЕЦ\n\n")


btm = {2: 'abc', 3: 'def',
       4: 'ghi', 5: 'jkl', 6: 'mno',
       7: 'pqrs', 8: 'tuv', 9: 'wxyz'}


def input_sms():
    while True:
        try:
            sms = int(input("Введите строку из цифр 2-9 (до 10 символов):\n"))
        except ValueError:
            print("Введены запрещённые символы! Попробуйте снова...")
        else:
            if 0 < len(str(sms)) <= 10 and '1' not in str(sms):
                return sms
            print("Некорректный ввод! Попробуйте снова...")


sms_str = str(input_sms())
text_str = []

for i in range(len(sms_str)):
    text_str.append([])
    for j in btm[int(sms_str[i])]:
        text_str[i].append("".join(j))
print("Возможные нажатые буквы:")
print(text_str)

text_sms = text_str[0]
for i in range(1, len(text_str)):
    drop = len(text_sms)  # сохраняем длину списка до добавления новых сочетаний
    for j in (itertools.product(text_sms, text_str[i])):
        text_sms.append("".join(map(str, j)))
    del text_sms[:drop]  # удаляем список до добавления новых сочетаний

print("Возможные слова:")
print(" ".join(text_sms))

input("КОНЕЦ\n\n")


def input_k():
    while True:
        try:
            k = int(input("Введите количество пользователей за месяц:\n"))
        except ValueError:
            print("Вы ввели не число! Попробуйте снова...")
        else:
            if 0 <= k < 10000:
                return k
            print("Введённое число вне диапазона: от 0 до 10000! Попробуйте снова...")


print("Первый сервер.")
k = input_k()
serv1 = []
print("Второй сервер.")
m = input_k()
serv2 = []
for i in range(k):
    serv1.append(str(random.randint(0, 10000)))
for i in range(m):
    serv1.append('0')
    serv2.append(str(random.randint(0, 10000)))
print("Вводные данные по серверам:")
print(" ".join(serv1))
print(" ".join(serv2))

print("Отсортированный список по обоим серверам:")
for i in range(k, k+m):
    serv1[i] = int(serv2[i-k])
for i in range(k):
    serv1[i] = int(serv1[i])
serv1.sort()
for i in range(k+m):
    serv1[i] = str(serv1[i])
print(" ".join(serv1))

input("КОНЕЦ\n\n")


numeric = int(input("Введите число, которое нужно проверить на степень 4:\n"))


def power_of_4(n):
    while n >= 1:
        n /= 4
        if n == 1:
            return True
        elif n < 1:
            return False


print("Утверждение, что " + str(numeric) + " является степенью 4: " + str(power_of_4(numeric)))
input("КОНЕЦ\n\n")

str_d = input("Введите строку:\n")
period = Counter(str_d)
sort_d = []
for i in sorted(period.values()):
    print(i)
    for k, v in period.items():
        if i == v and k not in sort_d and k != "":
            for j in range(i):
                sort_d.append(k)
sort_d.reverse()
print("".join(sort_d))
input("КОНЕЦ\n\n")

str_a = input("Введите строку:\n")
new_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
str_b = list(str_a)
str_b.insert(random.randint(0, len(str_a)+1), new_letter)
str_b = "".join(str_b)
print("В строке: " + str_b)
i = 0
while i < (len(str_a)):
    if str_a[i] == str_b[i]:
        i += 1
        if i == len(str_a):
            print("лишняя буква \'" + str_b[i] + "\' была в конце")
    else:
        print("лишняя буква \'" + str_b[i] + "\'")
        break
input("КОНЕЦ\n\n")

dec_d = input("Введите десятичное число:\n")
bin_d = str(bin(int(dec_d))[2:])
print("(двоичное " + bin_d + ")")
ed = 0
for i in range(len(bin_d)):
    if bin_d[i] == '1':
        ed += 1
print("Число единиц у введенного числа в двоичной системе: " + str(ed))
input("КОНЕЦ\n\n")

lst = [42, 54, 5, 42, 64, 43, 5, 64, 99, 99, 54, 45, ]
print(lst)
lst = sorted(lst)
i = 0
while i < (len(lst)-2):
    if lst[i] == lst[i+1] and lst[i] != lst[i+2]:
        i += 2
    else:
        print("Сотрудник неверно записавшийся на обед: ")
        print(lst[i])
        break

input("КОНЕЦ\n\n")

bin_one = input("Введите первое двоичное число\n")
print("(десятичное " + str(int(bin_one, 2)) + ")")
bin_two = input("Введите второе двоичное число\n")
print("(десятичное " + str(int(bin_two, 2)) + ")")


def bin_to_dec(a):
    dec_a = 0
    step = 1
    for i in a[::-1]:
        if i == '1':
            dec_a += step
        step *= 2
    return dec_a


def bin_sum(a, b):
    dec_s = int(bin_to_dec(a) + bin_to_dec(b))
    bin_s = ""
    while dec_s > 0:
        bin_s = str(dec_s % 2) + bin_s
        dec_s = dec_s // 2
    return str(bin_s)


bin_one_plus_two = bin_sum(bin_one, bin_two)

print("Сумма двоичных чисел = " + bin_one_plus_two)
print("(десятичное " + str(int(bin_one_plus_two, 2)) + ")")

input("КОНЕЦ\n\n")


word_one = list(input("Введите первое слово:\n"))
word_two = list(input("Введите второе слово:\n"))
if word_one == word_two:
    print("введены одинаковые слова")
elif list(reversed(word_one)) == word_two:
    print("введеные слова - палиндромы")
elif sorted(word_one) == sorted(word_two):
    print("введённые слова - АНАГРАММЫ")
else:
    print("введённые слова не являются анаграммами")

input("КОНЕЦ\n\n")


lst = []
long_lst = int(input("Введите количество чисел в списке:\n"))
for i in range(long_lst):
    lst.append(random.randint(0, 10))
print(lst)

for i in range(len(lst)):
    dbl = lst[i]
    for j in lst[(i+1):]:
        if dbl == j:
            print(dbl)
input("КОНЕЦ\n\n")


d = int(input("Введите десятичное число:\n"))
print("В двоичной системе оно будет выглядеть так:")
print(bin(d)[2:])
input("КОНЕЦ\n\n")


digit_score = 1
score_member = []


def score_input():
    global digit_score, score_member
    digit_score = int(input("Введите количество дней:\n"))
    for i in range(digit_score):
        day_score = input("Введите очки за %d-й день:\n" % (i+1))
        score_member.append(day_score)
    pass


score_input()
print("Введенные данные:")
print(digit_score)
print(" ".join(score_member))
print(score_member)
i = 0
while i < len(score_member):
    if int(score_member[i]) == 0:
        score_member.pop(i)
    else:
        i += 1

print(" ".join(score_member))

input("КОНЕЦ\n\n")

digit_x = 1
x_list = []
k = 1


def number_input():
    global k, x_list, digit_x
    digit_x = int(input("Введите количество цифр у числа X:\n"))
    for i in range(digit_x):
        x_member = input("Введите %d-ю цифру Х:\n" % (i+1))
        x_list.append(x_member)
    k = int(input("Введите число К:\n"))
    pass


number_input()

print("Введенные данные:")
print(digit_x)
print(" ".join(x_list))
print(k)
x = int("".join(map(str, x_list)))
print(" ".join(str(x+k)))
input("КОНЕЦ\n\n")

stroka = []


def data_input():
    while True:
        napolnenie = input("Введите новую подстроку (чтобы завершить ввод оставьте её пустой):\n")
        if napolnenie == '':
            return False
        stroka.append(napolnenie)
    pass


data_input()
print("Введённая строка:")
print(stroka)
max_dlina = 0
index_max = 0

for podstroka in stroka:
    print("№" + str(stroka.index(podstroka)+1) + ' -> ' + str(podstroka))
    next_element = podstroka[0]
    dlina = 0
    for element in podstroka:
        if element == next_element:
            dlina += 1
            next_element = element
            if max_dlina < dlina:
                max_dlina = dlina
                index_max = stroka.index(podstroka)
        else:
            continue

print("Длина самой длинной подстроки, состоящей из одного элемента:")
print(max_dlina)


def formula_a(a, x, b, c):
    y = a*x*x+b*x+c
    return y


answer = formula_a(8, 2, 9, -10)


print("Ответ:")
print(answer)

conference = []


def vuz_input():
    vuz_id = 1
    while True:
        print("Введите количество участников от ВУЗа с id= %d (чтобы закончить ввод осавьте поле пустым):" % vuz_id)
        member = input()
        if member == '':
            return False
        conference.append(int(member))
        vuz_id += 1
        pass


vuz_input()
print("количество участников конференции от каждого ВУЗа:")
print(conference)
k = int(input("Введите число, сколько ВУЗов вывести с наибольшим числом участников:\n"))
if k >= len(conference):
    k = len(conference)

top = list(reversed(sorted(conference)))
topk = str()
for i in range(k):
    topk += str(top[i]) + " "
print("Максимальное число участников:")
print(topk)
input("КОНЕЦ\n\n")
