import random as rd
import enum as e
import kivy as kv
from kivy.uix.widget import Widget

from Joulle.joulle import Joulle




class Area:
    def __init__(self,*args, **kwargs):
        self.name = "BaseAreaTest"

    @classmethod
    def instantiate_area_r(cls):
        flist = [(area.value() ,area.value.weight) for area in list(Areas)]
        return rd.choices([z[0] for z in flist],weights=[z[1] for z in flist],k=1)[0]



class Junkyard(Area):
    weight = 150
    def __init__(self,*args,**kwargs):
        super(Junkyard, self).__init__(*args, **kwargs)
        self.name = "Junkyard"

class Suburbia(Area):
    weight = 30
    def __init__(self,*args,**kwargs):
        super(Suburbia, self).__init__(*args, **kwargs)
        self.name = "Suburbs"


class Highclass(Area):
    weight = 10
    def __init__(self,*args,**kwargs):
        super(Highclass, self).__init__(*args, **kwargs)
        self.name = "High Class City"


class Lowclass(Area):
    weight = 20
    def __init__(self,*args,**kwargs):
        super(Lowclass, self).__init__(*args, **kwargs)
        self.name = "Slums"


class Wasteland(Area):
    weight = 5
    def __init__(self,*args,**kwargs):
        super(Wasteland, self).__init__(*args, **kwargs)
        self.name = "Wasteland"

class CityCommon(Area):
    weight = 30
    def __init__(self,*args,**kwargs):
        super(CityCommon, self).__init__(*args, **kwargs)
        self.name = "City"

class Joullopolis(Area):
    weight = 3
    def __init__(self,*args,**kwargs):
        super(Joullopolis, self).__init__(*args, **kwargs)
        self.name = "Joullopolis"


class Location:
    def __init__(self):
        self.area:(AreaInstance, None) = None
        self.available_to_spawn_on:[Area]

    def action(self,joulle:Joulle):
        print(f'Joul visited {self.area.name if self.area else "what"}')

class Hospital(Location):
    def __init__(self):
        super(Hospital, self).__init__()

class Shop(Location):
    def __init__(self):
        super(Shop, self).__init__()

class AreaInstance:
    def __init__(self,posx:int, posy:int, area:Area,map):
        self.area = area
        self.objects = []
        self.map_pos = (posx, posy)
        self.map = map
        self.baton:(None, Widget)

    # def gen_objects(self):
    #     objects = Locations


    def adjecent(self):
        x = self.map_pos[0]
        y = self.map_pos[1]
        bottom = (x, y-1) if y-1 >= 0 else None
        top = (x, y+1) if y+1 < self.map.height else None
        left = (x-1, y) if x-1 >= 0 else None
        right = (x+1, y) if x+1 < self.map.width else None
        ret = [x for x in [bottom, top, left, right] if x]
        # {"left":left,"right":right,"top":top,"bottom":bottom}

        return [self.map.get_sqm(z[0], z[1]) for z in ret]

    @property
    def name(self):
        return f"[{self.map_pos[0]}][{self.map_pos[1]}] {self.area.name}"


class Areas(e.Enum):
    JUN = Junkyard
    HGH = Highclass
    LOW = Lowclass
    WST = Wasteland
    CTC = CityCommon
    JLP = Joullopolis
    SBR = Suburbia


class Map:
    def __init__(self,height=5,width=5,jcap=4):
        self.height = height
        self.width = width
        self.jcap = jcap
        self.grid:[[(AreaInstance,None)]] = [[AreaInstance(j, i, Area.instantiate_area_r(),map=self) for i in range(width)] for j in range(height)]


    def get_sqm(self, x:int, y:int) -> (AreaInstance, None):
        return self.grid[x][y]

    def get_random_position(self):
        return rd.choice(rd.choice(self.grid))





