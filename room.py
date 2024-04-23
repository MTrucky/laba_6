class Room:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.length * self.width

    def calculate_heat_power(self):
        return self.calculate_area() * 100   # Пример расчета тепловой мощности
