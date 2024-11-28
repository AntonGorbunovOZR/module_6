class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'yelow']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, n_color):
        if n_color.casefold() in (color.casefold() for color in self.__COLOR_VARIANTS):
            self.__color = n_color
        else:
            print(f'Нельзя сменить цвет на {n_color}')


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'

# Проверяем что поменялось

vehicle1.print_info()
