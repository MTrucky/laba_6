# laba_6
## Модули и пакеты
____
### Вариант (GUI фреймворк): Tkinter

`Помещения:`

>1) Комната

>2) Квартира

>3) Многоэтажный дом

( Расчёт общей площади помещения, тепловой мощности для обогрева помещения )
____

## ***Создание пакета, содержащего 3 модуля***

>![image](https://github.com/MTrucky/laba_6/assets/146337304/860147dc-fdab-4253-a56e-769b1d549534)

Необходимо создать файл __init.py__ для того, чтобы python понял, что это пакет модулей.

`Модули:`
* Комната
* Квартира
* Здание


`Комната`:
```
class Room:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.length * self.width

    def calculate_heat_power(self):
        return self.calculate_area() * 100   # Пример расчета тепловой мощности
```

`Квартира`:
```
from paket.room import Room

class Apartment(Room):
    def __init__(self, length, width, height, num_rooms):
        super().__init__(length, width, height)
        self.num_rooms = num_rooms

    def calculate_total_area(self):
        return self.calculate_area() * self.num_rooms

    def calculate_heat_power(self):
        return self.calculate_total_area() * 120  # Пример тепловой мощности квартиры
```

`Здание`:

```
from paket.apartment import Apartment

class MultistoryBuilding(Apartment):
    def __init__(self, length, width, height, num_floors, num_apartments_per_floor):
        super().__init__(length, width, height, num_floors * num_apartments_per_floor)
        self.num_floors = num_floors
        self.num_apartments_per_floor = num_apartments_per_floor

    def calculate_total_area(self):
        return super().calculate_total_area() * self.num_floors

    def calculate_heat_power(self):
        return super().calculate_heat_power() * 1.2  # Пример тепловой мощности для многоэтажного дома
```


## ***Создаём файл main.py:***

Правильно импортируем модули (main.py должен быть в той же директории что и paket, иначе будет по другому)
```
import tkinter as tk
from tkinter import messagebox
from paket.room import Room
from paket.apartment import Apartment
from paket.multistory_building import MultistoryBuilding
import docx
from openpyxl import Workbook
```
### [Как сохранять данные в документ?](https://tokmakov.msk.ru/blog/item/78?ysclid=lvc5t4z1ec374680482)

### [хорошее объяснение Tkinter](https://www.youtube.com/playlist?list=PLQAt0m1f9OHsd6U5okp1XLoYyQR0oBjMM)

### [ChatGPT](https://chat.openai.com/c/912661ed-8274-4ed0-a1bf-a1baa433930f)
