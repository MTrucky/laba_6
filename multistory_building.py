from paket.apartment import Apartment

class MultistoryBuilding(Apartment):
    def __init__(self, length, width, height, num_floors, num_apartments_per_floor):
        super().__init__(length, width, height, num_floors * num_apartments_per_floor)
        self.num_floors = num_floors
        self.num_apartments_per_floor = num_apartments_per_floor

    def calculate_total_area(self):
        return super().calculate_total_area() * self.num_floors

    def calculate_heat_power(self):
        return super().calculate_heat_power() * 1.2  # Пример расчета тепловой мощности для многоэтажного дома
