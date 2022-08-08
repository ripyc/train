import math
from math import radians, sin, cos, acos

print("\n# Первое задание:")


class Contact:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.birthday = birthday
        print(f"Создаём новый контакт {name}")

    def show_contact(self):
        print(f"{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}")


mike = Contact("Михаил Булгаков", "2-03-27", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6", "15.05.1891")
vlad = Contact("Владимир Маяковский", "73-88", "Россия, Москва, Лубянский проезд, д. 3, кв. 12", "19.07.1893")


def print_contact():
    print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")


mike.show_contact()
vlad.show_contact()

print("\n# Второе задание:")
# импортируйте библиотеку math


class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = 4 * math.pi * radius**2   # здесь вычислите площадь поверхности шара
        self.average_temp_celcius = temp_celsius
        self.average_temp_fahrenheit = (temp_celsius * 9/5) + 32  # здесь переведите температуру в градусы Фаренгейта

    def show_info(self):
        print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
        print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit}° по Фаренгейту.")


jupiter = Planet('Юпитер', 69911, -108)
jupiter.show_info()  # вызовите метод show_info для Юпитера

print("\n# Третье задание:")


class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name} ({self.phone})')


class Friend(User):
    def show(self):
        print(f'Имя: {self.name} || Телефон: {self.phone}')


user = User("Виктор Гюго", "+33 1 42 72 10 16")
# у класса friend нет конструктора, но он есть
# у родительского класса User, поэтому код сработает
friend = Friend("Виктор Гюго", "+33 1 42 72 10 16")
user.show()
friend.show()

print("\n# Четвёртое задание:")
# импортируем функции из библиотеки math для рассчёта расстояния


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)
    # считаем расстояние между двумя точками в км

    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude)\
                + cos(self.latitude) * cos(other.latitude) * cos(self.longitude - other.longitude)
        return 6371 * acos(cos_d)


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        # допишите код: сохраните свойства родителя
        # и добавьте свойства name и population

        self.name = name
        self.population = population
        super().__init__(latitude, longitude)

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")


class Mountain(Point):
    # допишите код: напишите конструктор, в нём сохраните свойства родителя
    # и добавьте свойства name и height
    # Переопределите метод show(self):
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height

    def show(self):
        print(f"Высота горы {self.name} - {self.height} м")


Moscow = City(55.755787, 37.617634, "Москва", "11,92 млн")
Moscow.show()
Everest = Mountain(28, 87, "Эверест", 8848)
Everest.show()
rast = float("{0:.3f}".format(Moscow.distance(Everest)))
print("Высота от Москвы до Эвереста - " + str(rast) + " километров")

print("\n# Пятое задание:")


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу
    def answer_question(self, question):
        return "- Очень интересный вопрос! Не знаю."


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        self.someone = someone
        self.question = question
        print(f"{self.someone}, {self.question}")
        print(f"{someone.answer_question(question)}")
        # запросите ответ на вопрос у someone
        print(' ')  # этот print выводит разделительную пустую строку


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            ans = "- Лучший отдых это смена деятельности"
        else:
            ans = super().answer_question(question)
        return ans
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса


# объявите и реализуйте классы CodeReviewer и Mentor
class CodeReviewer(Human):
    def answer_question(self, question):
        self.question = question
        if question == "что не так с моим проектом?":
            ans = ("- Для того, чтобы ты научился просить о помощи"
                   + "\nпостарайся оформить вопрос по правилам, пройдясь по всем пунктам")

        else:
            ans = super().answer_question(question)
        return ans


class Mentor(Human):
    def answer_question(self, question):
        if question == "как устроиться работать питонистом?":
            ans = ("- Нужно откликнутся на одноимённую вакансию, пройти собеседование,"
                   + "\nв случае успеха согласится и подписать договор")
        else:
            ans = super().answer_question(question)
        return ans


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
