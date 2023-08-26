import math
import random
from equipement import Equipment


class JoulleClass:
    def __init__(self):
        self.cname = "JCLASS"
        self.color = "00ffff"
        self.base_damage = 4
        self.critical_chance_modifier:float = 1
        self.critical_damage_modifier:float = 1.5
        self.defense_b = 5
        self.health_b = 15
        self.attack_b = 1
        self.strength_b = 1
        self.agility_b = 1
        self.intelligence_b = 1
        self.wisdom_b = 1
        self.condition_b = 1

    @classmethod
    def get_random_class(cls):
        return random.choice([Piesciarz,Scavenger,Shuvax,Pacyfista])


class Piesciarz(JoulleClass):
    def __init__(self):
        super(Piesciarz, self).__init__()
        self.cname = "Piesciarz"
        self.color = (1,0,0,1)
        self.attack_b = 25
        self.strength_b = 25
        self.agility_b = 2
        self.intelligence_b = .3
        self.wisdom_b = .1
        self.condition_b = 1.5

class Scavenger(JoulleClass):
    def __init__(self):
        super(Scavenger, self).__init__()
        self.cname = "Scavenger"
        self.color = (0,0,0,1)
        self.base_damage = 3
        self.critical_chance_modifier: float = 1
        self.critical_damage_modifier: float = 1.75
        self.defense_b = 2
        self.health_b = 12
        self.attack_b = 1
        self.strength_b = .8
        self.agility_b = 3
        self.intelligence_b = 2
        self.wisdom_b = 2
        self.condition_b = 0.5

class Shuvax(JoulleClass):
    def __init__(self):
        super(Shuvax, self).__init__()
        self.cname = "Shuvax"
        self.color = (0,1,1,1)
        self.base_damage = 3
        self.critical_chance_modifier: float = 1.2
        self.critical_damage_modifier: float = 3
        self.defense_b = 1.6
        self.health_b = 13
        self.attack_b = .5
        self.strength_b = .5
        self.agility_b = 4
        self.intelligence_b = 3
        self.wisdom_b = 5
        self.condition_b = 4

class Pacyfista(JoulleClass):
    def __init__(self):
        super(Pacyfista, self).__init__()
        self.cname = "Pacyfista"
        self.base_damage = 1
        self.critical_chance_modifier: float = 5
        self.critical_damage_modifier: float = 150
        self.defense_b = 0
        self.health_b = 10
        self.attack_b = .4
        self.strength_b = .5
        self.agility_b = 3
        self.intelligence_b = 5
        self.wisdom_b = 5
        self.condition_b = .5

