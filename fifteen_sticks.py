import string

print("Добро пожаловать в программу Hello, World!\n")
name = string.capwords(input("Введите своё имя:\n"))
print("\nПривет," + name + "! Сегодня мы будем играть в игру 15 палочек")
print('''\nВ этой игре как следует из названия есть 15 палочек.
Ты можешь зачеркнуть от 1 до 3.
Компьютер зачеркивает тоже от 1 до 3 палочек.
Кому останется последняя палочка - тот проиграл\n''')
line = []
for i in range(15):
    line.append('l')
print(" ".join(line))
print("")
print(name + ", введи сколько палочек тебе хотелось бы зачеркнуть:")
turn1 = input()
turn1 = int(turn1)
i = 0
while i < turn1:
    # прорисовка первого хода игрока
    line.insert(i, 'x')
    line.remove('l')
    # прорисовка первого хода компьютера
    line.append('x')
    line.remove('l')
    i += 1
# выводим текущее положение игрового поля после первого хода:
print("компьютер тоже сделал свой ход:")
print("")
print(" ".join(line))
print("")
sum_l = line.count('l')
while sum_l > 1:
    sum_l = line.count('l')
    # print("Осталось палочек:" + str(sum_l))
    if sum_l == 1:
        print("Ты проиграл," + name + "! Повторить?")
        p = input("(Y/n)")
        if p == 'Y' or p == 'y' or p == 'Yes' or p == 'yes' or p == 'Д' or p == 'д' or p == 'Да' or p == 'да':
            print(name + ", повторяю: ты проиграл!")
            input()
            print("Конец.")
            exit()
        else:
            print("Нет так нет. Приятного дня и до скорой встречи!")
            exit()
    print("Твой следующий ход, введи сколько палочек зачеркнуть:")
    turn2 = input()
    turn2 = int(turn2)

    while i < (turn1+turn2):
        line.insert(i, 'x')
        line.remove('l')
        i += 1

    turn1 = turn1 + turn2
    sum_l = line.count('l')

    if sum_l > 1:
        turn_c = 4-turn2
        j = 0
        while j < turn_c:
            line.append('x')
            line.remove('l')
            j += 1
        print("компьютер тоже сделал свой ход:")
    else:
        print("Это победа! Ты молодец," + name)
        input()
        print("Конец.")
        exit()
    print("")
    print(" ".join(line))
    print("")
print("Конец.")
