class BaseDescriptor:

    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class NumberDescriptor(BaseDescriptor):

    @classmethod
    def verify(cls, field):
        if not isinstance(field, int):
            raise TypeError('номер игрока должен быть'
                            ' целым положительным числом')
        if not 0 <= field < 100:
            raise ValueError('номер игрока должен быть'
                             ' целым положительным числом меньше 100')

    def __set__(self, instance, value):
        self.verify(value)
        super().__set__(instance, value)


class PositionDescriptor(BaseDescriptor):
    positions = ('PG', 'SG', 'SF', 'PF', 'C')

    @classmethod
    def verify(cls, field):
        if not isinstance(field, str):
            raise TypeError('Позиция игрока должен быть '
                            'одно-/двух- буквенной строкой')
        if field not in cls.positions:
            raise ValueError(f'Позиция должна быть в {cls.positions}')

    def __set__(self, instance, value):
        self.verify(value)
        super().__set__(instance, value)


class HeightDescriptor(BaseDescriptor):

    @classmethod
    def verify(cls, field):
        if not isinstance(field, float):
            raise TypeError('Рост игрока должен быть'
                            ' числом с плавающей точкой в сантиметрах')
        if field < 0.0:
            raise ValueError('Рост игрока должен быть положительным числом')

    def __set__(self, instance, value):
        self.verify(value)
        super().__set__(instance, value)


class BasketballPlayer:
    number = NumberDescriptor()
    position = PositionDescriptor()
    height = HeightDescriptor()

    def __init__(self, number: int, position: str, height: float):
        self.number = number
        self.position = position
        self.height = height

    def __str__(self):
        return f'Игрок под номером {self.number} с ростом {self.height}' \
               f' играет на позиции {self.position}'
