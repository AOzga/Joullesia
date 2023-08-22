from enum import Enum

class Item:
    def generate_amount_rarity(self):
        ...

class WearableAdditionalInfo:
    def __init__(self):
        self.hp = int
        self.speed = int
        self.damage = int
        self.attack = int
        self.strength = int
        self.agility = int
        self.intelligence = int
        self.wisdom = int
        self.condition = int


class Wearable(Item):
    def __init__(self):
        self.slot = None
        self.info = WearableAdditionalInfo()

class Weapon(Wearable):
    def __init__(self):
        super(Weapon, self).__init__()
        self.slot = "weapon"
        self.damage = int



class Equipment():
    def __init__(self):
        self.head = None
        self.body = None
        self.body_outer = None
        self.legs = None
        self.feet = None
        self.hands = None
        self.main_weapon = None
        self.offhand = None
        self.rings = [None for i in range(10)]
        self.neck = None

    @property
    def eq_dmg(self):
        if not type(self.main_weapon) == Weapon:
            return 0

        return self.main_weapon.damage
