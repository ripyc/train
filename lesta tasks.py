# ЗАДАНИЕ 1. На языке Python реализовать алгоритм (функцию) определения четности целого числа,
# который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
# Объяснить плюсы и минусы обеих реализаций.

import time


def isEven(value):
    return value % 2 == 0


def parity_check(value):
    if str(bin(value))[-1] == '1':
        return False
    else:
        return True


number = 17777125465463653634634638269818
print("Время исполнения приведённого алгоритма:")
start_time = time.time()
isEven(number)
print("--- %s seconds ---\n" % (time.time() - start_time))

print("Время исполнения реализованного алгоритма:")
start_time = time.time()
parity_check(number)
print("--- %s seconds ---\n" % (time.time() - start_time))

# Преимущество приведенной в задании функции в том, что она интуитивно понятна, так как реализует свойство четности
# числа из его определения в Википедии. Так же она в 2 раза быстрее, чем реализованная мной.
# Из перимуществ функции parity_check можно отметить то, что она имеет название без заглавных букв (по PEP 8),
# использует работу со строкой, массивом, условным оператором. Ананлиз данного решения позволил найти вариант:
# def isEven2(value):return value&1==0, который в свою очередь в 2 раза быстрее первого алгоритма, а также познакомил
# меня с битовыми операциями в Python

print("* "*25)
# ЗАДАНИЕ 2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.

class RingBuffer:
    def __init__(self, max_size=10):