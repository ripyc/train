# Hi, this is calculator of money and calories

import datetime as dt

class Record:
    def __init__(self, amount, comment, date = ''):
        self.amount = str(amount)
        self.comment = str(comment)
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, note):
        #self.note = note
        self.records.append(note)

    def get_today_stats(self):
        today_stats = 0
        for note in self.records:
            if note.date == dt.datetime.now().date():
                today_stats += int(note.amount)

        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for note in self.records:
            if (today - dt.timedelta(days=7)) <= note.date <= today:
                week_stats += note.amount

        return week_stats


class CashCalculator(Calculator):
    USD_RATE = 85
    EUR_RATE = 95

    def get_today_cash_remained(self, currency):
        currency = currency.lower()
        balance = (self.limit - self.get_today_stats())
        if currency == 'rub':
            if balance > 0:
                return f'На сегодня осталось {balance} руб.'
            elif balance == 0:
                return 'Денег нет, держись'
            elif balance < 0:
                return f'Сегодня потрачено больше лимита, долг {balance} руб.'

        elif currency == 'usd':
            balance = round(balance/self.USD_RATE, 2)
            if balance > 0:
                return f'На сегодня осталось {balance} $'
            elif balance == 0:
                return 'Денег нет, держись'
            elif balance < 0:
                return f'Сегодня потрачено больше лимита, долг {balance} $'


        elif currency == 'eur':
            balance = round(balance/self.EUR_RATE, 2)
            if balance > 0:
                return f'На сегодня осталось {balance} Euro'
            elif balance == 0:
                return 'Денег нет, держись'
            elif balance < 0:
                return f'Сегодня потрачено больше лимита, долг {balance} Euro'

        else:
            return 'Некорректно введена валюта, используйте rub, usd или eur'


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        balance = (self.limit - self.get_today_stats())
        if balance >= 0:
            return f'На сегодня осталось {balance} каллорий'
        else:
            return 'Хватит есть!'



# значения для проверки работы CashCalculator
r1 = Record(amount=145, comment="Безудержный шопинг", date="15.04.2022")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="7.4.2022")
r3 = Record(amount=691, comment="Катание на такси")

# значения для проверки работы CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="4.04.2022")
r5 = Record(amount=84, comment="Йогурт.", date="7.4.2022")
r6 = Record(amount=1140, comment="Баночка чипсов.")

cash_test = CashCalculator(1000)
cash_test.add_record(r1)
cash_test.add_record(r2)
cash_test.add_record(r3)

# Ввод валюты для проверки остатка кошелька
def currency_check():
    while True:
        valuta = input("Введите валюту в которой хотите посмотреть баланс (rub, usd или eur:\n")
        if valuta == "rub" or valuta == "usd" or valuta == "eur":
            return valuta
print(cash_test.get_today_cash_remained(currency_check()))

cal_test = CaloriesCalculator(2500)
cal_test.add_record(r4)
cal_test.add_record(r5)
cal_test.add_record(r6)
amount_test = int(input("Введите потраченные сегодня каллории:\n"))
comment_test = input("Оставьте по ним комментарии:\n")
r7 = Record(amount=amount_test, comment=comment_test)
cal_test.add_record(r7)

print(f"Статистика на счегодня {cal_test.get_today_stats()}")
print(cal_test.get_calories_remained())
