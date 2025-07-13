import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # допиши код здесь
    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if not (1 <= len(name) <= 40):
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self) -> float:
        total = 0
        for item in self.__name_items:
            total += self.__item_price[item]
        if self.__number_items > 10:
            total *= 0.9
        return total

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total_prices = []

        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                price = self.__item_price[item]
                total_prices.append(price)
                twenty_percent_tax.append(price * 0.2)

        total_vat = sum(twenty_percent_tax)
        if self.__number_items > 10:
            total_vat *= 0.9
        return total_vat

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total_prices = []

        for item in self.__name_items:
            if self.__tax_rate.get(item) == 10:
                price = self.__item_price[item]
                total_prices.append(price)
                ten_percent_tax.append(price * 0.1)

        total_vat = sum(ten_percent_tax)
        if self.__number_items > 10:
            total_vat *= 0.9
        return total_vat

    def total_tax(self) -> float:
        """Общая сумма НДС по чеку."""
        return (
                self.twenty_percent_tax_calculation()
                + self.ten_percent_tax_calculation()
        )

    @staticmethod
    def get_telephone_number(telephone_number):
        if telephone_number is float:
            raise ValueError('Необходимо ввести цифры')
        if len(telephone_number) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'

    get_date_and_time = (
        lambda now: [
            f"{name}: {func(now)}"
            for name, func in [
                ('часы', lambda x: x.hour),
                ('минуты', lambda x: x.minute),
                ('день', lambda x: x.day),
                ('месяц', lambda x: x.month),
                ('год', lambda x: x.year),
            ]
        ]
    )(datetime.datetime.now())