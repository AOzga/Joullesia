from equipement import Equipment


class Inventory:
    size = 50
    def __init__(self):
        self.equipment = Equipment()
        self.inventory = [None for _ in range(self.size)]
