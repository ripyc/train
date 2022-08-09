# ЗАДАНИЕ 1. На языке Python реализовать алгоритм (функцию) определения четности целого числа,
# который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
# Объяснить плюсы и минусы обеих реализаций.

import time
import random


def isEven(value):
    return value % 2 == 0


def parity_check(value):
    if str(bin(value))[-1] == '1':
        return False
    else:
        return True


number = 1234567890987654321
print("Время исполнения приведённого алгоритма:")
start_time = time.time()
isEven(number)
print("--- %s seconds ---\n" % (time.time() - start_time))

print("Время исполнения реализованного алгоритма:")
start_time = time.time()
parity_check(number)
print("--- %s seconds ---\n" % (time.time() - start_time))

# Преимущество приведенной в задании функции в том, что она интуитивно понятна, так как реализует свойство четности
# числа из его определения. Также она в 2 раза быстрее, чем реализованная мной.
# Из перимуществ функции parity_check можно отметить то, что она имеет название без заглавных букв (по PEP 8),
# подчеркивает умение оперировать со строкой, массивом, условным оператором. К тому же ананлиз данного решения
# позволил найти вариант: def isEven2(value):return value&1==0, который в свою очередь в 2 раза быстрее
# первого алгоритма, а также познакомил меня с битовыми операциями в Python, за что я вам благодарен
print("* "*25)


# ЗАДАНИЕ 2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.

# Циклический буфер, реализованный с помощью массива:
class RingBuffer1:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def __str__(self):
        return str(self.items)

    def put(self, elem):
        if self.max_size < 2:
            return "Error. Max size of buffer ring not so big (max_size<2)"
        elif len(self.items) < self.max_size:
            self.items.append(elem)
        else:
            # если размер массива равен максимальному размеру, то убрать 0-ую (первую) позицию и добавить элемент
            self.items = self.items[1:] + [elem]

    def get(self):
        if not self.items:
            return "Error. Buffer is empty"
        else:
            self.items = self.items[1:]

    def size(self):
        return len(self.items)


# Циклический буфер, реализованный с помощью связного списка:
class Node4RingBuffer:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


class RingBuffer2:
    def __init__(self, max_size):
        self.max_size = max_size  # максимальный размер буфера
        self.size = 0  # текущий размер буфера
        self.head = None  # голова буфера
        self.tail = None  # хвост буфера

    def put(self, elem):
        print("Внесён элемент: " + str(elem))
        node = Node4RingBuffer(elem)
        if self.max_size < 2:
            return "Error. Max size of buffer ring not so big (max_size<2)"
        elif self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
        elif self.size < self.max_size:
            self.tail.next_item = node
            self.tail = node
            self.size += 1
        else:
            # если размер буфера равен максимальному размеру, то добавить элемент в хвост, а головой списка
            # сделать следующий за ней элемент, таким образом удалив голову буфера на момент добавления:
            self.tail.next_item = node
            self.tail = node
            self.head = self.head.next_item

    def get(self):
        if not self.head:
            print("Error. Buffer is empty")
        else:
            print("Уходит элемент: " + str(self.head.value))
            self.head = self.head.next_item
            self.size -= 1

    def show(self):
        if not self.head:
            print("Buffer is empty")
        else:
            node = self.head
            for i in range(self.size - 1):
                print(node.value, end=", ")
                node = node.next_item
            print(node.value)


# Преимущество в реализации циклического буфера FIFO с помощью массива в наглядности реолизации и возможности обратится
# к i-ому элементу буфера (без добавления доп. алгоритмов). Недостаток в используемой памяти, в том числе в процессе
# извлечения и добавления элемента в заполненый буфер.
# В свою очередь преимущества циклического буфера FIFO с помощью связного списка в отсутствии портебности хранить весь
# список элементов в памяти, однако, более сложный процесс обращения к i-му элементу и сортировки в случае необходимости
print("* "*25)


# ЗАДАНИЕ 3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей
# массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить
# почему вы считаете, что функция соответствует заданным критериям.

def mysorting(lst):
    lst.sort()
    return lst

# На мой взгляд, если данная сортировка находится в стандартной библиотеке, то она заслужила право быть лучшей. Возможно
# я что-то упускаю, и в более конктретном случае существует более удачная сортировка, но как минимум такой ответ на
# тестовое задание можно назвать изящным и в духе Python.

while True:
    try:
        n = int(input("Введите количество чисел в массиве:\n"))
    except ValueError:
        print("Ошибка. Нужно ввести целочисленное значение!")
    else:
        if 0 < n:
            break
        else:
            print("Ошибка. Значение должно положительным целым числом")
print("Массив, заполненный числами:")
massive = []
print("[", end="")
for indx in range(n):
    massive.append(random.randint(-100, 100))
    if indx < n-1:
        print(massive[indx], end=", ")
    else:
        print(massive[indx], end="]\n")

print("Отсортированный массив:")
start_time = time.time()
print(mysorting(massive))
print("--- %s seconds ---\n" % (time.time() - start_time))
print("* "*25)
