import random


class Inventory:
    def __init__(self, name):
        print(f'Инициализация инвентаря для {name}')
        self.inventory = []

    def inventory_add(self, item):
        self.inventory.append(item)

    def inventory_remove(self, item):
        self.inventory.remove(item)

class Container(Inventory):
    def __init__(self, name, form=None):
        super().__init__(name)
        print(f"Инициализация контейнера для {name}")
        self.name = name
        self.form = form

    def container_open(self):
        if self.inventory:
            print(f'Содержимое {self.name}:')
            for item in self.inventory:
                print(item)
        else:
            print(f"{self.name} пуст")


