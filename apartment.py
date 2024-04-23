from paket.room import Room

class Apartment(Room):
    def __init__(self, length, width, height, num_rooms):
        super().__init__(length, width, height)
        self.num_rooms = num_rooms

    def calculate_total_area(self):
        return self.calculate_area() * self.num_rooms

    def calculate_heat_power(self):
        return self.calculate_total_area() * 120  # Пример расчета тепловой мощности для квартиры
