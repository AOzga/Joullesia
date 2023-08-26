# from kivy.app import App
import random

from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDIconButton
from Joulle.joulle import Joulle
from map import Map, Areas

class Joulicon(MDIconButton):
    joulz = []
    def __init__(self,joulref:Joulle):
        super(Joulicon, self).__init__()
        self.on_press = lambda:print(vars(joulref))
        self.joulref = joulref
        self.icon='account'
        self.icon_color = joulref._class.color
        self.size_hint = None,None
        self.size = 50,50
        self.parent = None
        self.pos_hint = {}
        self.joulz.append(self)
        # self.text=self.joulref.full_name
        self.text_color = joulref._class.color
        # print(Joulicon.joulz)


class AreaButton(Button):
    def __init__(self,name,clr,arearef):
        super(AreaButton, self).__init__()
        self.background_normal = ""
        self.background_color = clr
        self.arearef = arearef
        self.text = f""
        self.arearef.baton = self


class JoulVis(MDApp):
    def __init__(self,map:Map):
        super(JoulVis, self).__init__()
        self.holdwins = {}
        self.buttons = []
        self.winda = FloatLayout()
        self.windar = BoxLayout()
        self.windar.orientation = "vertical"
        self.map = map
        self.entities = [Joulle(position=self.map.get_random_position()) for _ in range(16)]
        self.infobar = BoxLayout()
        self.infobar.add_widget(Button(text="Spawn Joulle"))
        chkjl =Button(text="Check Joulle")
        chkjl.on_press = (lambda x=None: [print(vars(entity)) for entity in self.entities])
        self.infobar.add_widget(chkjl)
        opczan = Button(text="Options")
        opczan.on_press=lambda:Clock.schedule_interval(self.update_step,.3)
        self.infobar.add_widget(opczan)
        steppp=Button(text="Step")
        steppp.on_press = lambda:self.update_step(0.02)
        self.infobar.add_widget(steppp)
        self.infobar.size_hint_y = 0.125
        self.windar.add_widget(self.infobar)  # navbar
        self.grid_layout = GridLayout(size_hint=(1,1))
        self.grid_layout.rows = len(self.map.grid)
        self.grid_layout.cols = len(self.map.grid[0])
        self.windar.add_widget(self.grid_layout)
        self.go=True


        for i in self.map.grid:
            for j in i:
                if Areas(j.area.__class__) == Areas.JUN:
                    clr = "#afafaf"
                elif Areas(j.area.__class__) == Areas.HGH:
                    clr = "#1fc600"
                elif Areas(j.area.__class__) == Areas.LOW:
                    clr = "#063b00"
                elif Areas(j.area.__class__) == Areas.WST:
                    clr = "#451800"
                elif Areas(j.area.__class__) == Areas.CTC:
                    clr = "#aceace"
                elif Areas(j.area.__class__) == Areas.JLP:
                    clr = "#cfb53b"
                elif Areas(j.area.__class__) == Areas.SBR:
                    clr = "#cc6720"
                else:
                    clr = "FFFFFF"

                btn = AreaButton(name=j.name,clr=clr,arearef=j)
                self.buttons.append(btn)
                self.grid_layout.add_widget(btn)

        self.winda.add_widget(self.windar)
        for joul in self.entities:
            self.winda.add_widget(Joulicon(joulref=joul))
        Clock.schedule_interval(self.update_gui,1.0/60.0)
        self.eventz = Clock.create_trigger(self.update_step, timeout=0.01,interval=True)
        self.eventz()
        # Clock.schedule_interval(self.update_step,3)


    def update_gui(self, dt):
        ...

    def update_step(self,dt):
        jz = Joulicon.joulz
        for joul in jz:
            if not joul.joulref.isconcious:
                # print(f"pogrzebion {joul.joulref.full_name}")
                self.winda.remove_widget(joul)
                jz.remove(joul)
            joul.joulref.zul_take_action(jz)
            joul.joulref.get_exp(random.randint(2000, 2001))
            joul:Joulicon
            joul.pos=joul.joulref.position.baton.center_x , joul.joulref.position.baton.center_y
            # a = Animation(x=joul.joulref.position.baton.center_x+random.randint(int(-joul.joulref.position.baton.width*.95/3),
            #                                                                     int(joul.joulref.position.baton.width*.95/3)),
            #               y=joul.joulref.position.baton.center_y+random.randint(int(-joul.joulref.position.baton.height*.95/3),
            #                                                                     int(joul.joulref.position.baton.height*.95/3)),
            #               duration=0)
            # a.start(joul)
        suck='\n'
        if len([x for x in jz if x.joulref.isconcious]) == 1:
            self.eventz.cancel()

            if not self.holdwins.get([x for x in jz if x.joulref.isconcious][0].joulref._class.cname):
                self.holdwins[[x for x in jz if x.joulref.isconcious][0].joulref._class.cname] = 1
            else:
                self.holdwins[[x for x in jz if x.joulref.isconcious][0].joulref._class.cname]+=1
            print(
                f'[{[x for x in jz if x.joulref.isconcious][0].joulref} won]\n{f"{suck}".join([f"{k}:{v}" for k, v in self.holdwins.items()])}')



            for jl in Joulicon.joulz:
                self.winda.remove_widget(jl)
            while Joulicon.joulz:
                self.winda.remove_widget(Joulicon.joulz.pop())

            self.entities=[]
            for joul in [Joulle(position=self.map.get_random_position()) for _ in range(4)]:
                self.entities.append(joul)
                self.winda.add_widget(Joulicon(joulref=joul))
            self.eventz()



    def build(self):
        return self.winda