import math
import random
from Inventory.equipement import Equipment
from Joulle.joulleclass import JoulleClass


class Joulle:
    def __init__(self,position):
        self.isconcious = True
        self.position = position
        self.name=random.choice(["artur","dzosef","beatrice","ka","jogaikonie"])
        self.joulleclass = random.choice(["zul","menel","bej","bezdomny","dzul"])
        self.adjective = random.choice(["."])
        self._class:JoulleClass = JoulleClass.get_random_class()()
        self.equipement = Equipment()
        self.respect = 0
        self.experience = 0
        self.total_experience = 0
        self.level = 1
        self.boozelvl = 0
        self.current_health = self.health

        # self.damage = Statsheet.calc_damage(self.equipment.weapon,self.equipment.offhand)

    @property
    def full_name(self):
        return f"{self.name} {self.adjective} [{self._class.cname}]"

    def get_exp(self,amount:int):
        # print(f"{self.full_name} got {amount} of experience!")
        self.experience+=amount

        self.total_experience+=amount
        self.recalc_xp()

    def recalc_xp(self):
        while self.next_level_exp < self.experience:
            self.zul_level_up()
            self.current_health += self._class.health_b

    @property
    def next_level_exp(self):
        return sum([50*((x+1)**2 - 5*(x+1) + 8) for x in range(0,self.level)])

    @property
    def remaining_exp(self):
        return self.next_level_exp - self.experience

    def zul_attack(self,anodajoulle):
        # print(f"{self.full_name}---{self.damage}---->{anodajoulle.full_name}",end="")
        anodajoulle.zul_take_damage(self.damage)

    def zul_scavenge(self):
        pass

    def zul_sleep(self):
        for i in range(random.randint(1,8)):
            self.zul_regen()

    def zul_craft(self):
        pass

    def zul_take_damage(self,damage):
        inflicted = damage * 100/(100+self.defense)
        self.current_health -= inflicted
        if self.current_health <= 0:
            self.isconcious=False


    @property
    def damage(self):
        a = random.randint(0,100)

        dmg_premitigation = (self.base_damage + self.strength/4) * max(math.log((self.attack)**0.7)**2,1)
        if a < self.crit_chance:
            dmg_premitigation=dmg_premitigation*self.crit_dmg
        return dmg_premitigation*random.randint(85,125)/100

    @property
    def strength(self):
        return self.level*self._class.strength_b

    @property
    def attack(self):
        return self.level*self._class.attack_b

    @property
    def defense(self):
        return self.level*self._class.defense_b

    @property
    def base_damage(self):
        return self.level*self._class.base_damage

    @property
    def intelligence(self):
        return self.level*self._class.intelligence_b

    @property
    def agility(self):
        return self.level*self._class.agility_b

    @property
    def health(self):
        return self.level*self._class.health_b

    @property
    def wisdom(self):
        return self.level*self._class.wisdom_b

    @property
    def condition(self):
        return self.level*self._class.condition_b

    @property
    def crit_dmg(self):
        return self._class.critical_damage_modifier

    @property
    def crit_chance(self):
        return self._class.critical_chance_modifier * math.log(self.agility+10)**2

    def zul_level_up(self):
        self.level += 1

    def zul_regen(self):
        self.current_health = min(self.health,self.current_health+self.condition/2)

    def zul_move(self):
        r = random.choice(self.position.adjecent())
        self.position = r

    def zul_take_action(self,info):
        self.zul_regen()
        otherzule = [x for x in info if (x.joulref.position==self.position) and (x.joulref != self)]
        if self.isconcious:
            if otherzule:
                otherzul = random.choice(otherzule)
            else:
                otherzul=None
            a=random.randint(0,30)
            if a<10:

                self.zul_sleep()
            elif a<20:
                self.zul_move()
            elif a<30 and otherzul:
                self.zul_fight(otherzul)


    def zul_fight(self, otherzul):
        otherzul = otherzul.joulref
        while self.isconcious and otherzul.isconcious:
            a = random.choices([self, otherzul],weights=[int(self.intelligence+self.wisdom+self.agility) ,int(otherzul.intelligence+otherzul.wisdom+otherzul.agility) ],k=1)[0]
            if a==self:
                a.zul_attack(otherzul)
            else:
                otherzul.zul_attack(self)

