from turtle import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager
Window.size = (350, 600)

class ChangingText(MDApp):
    id = 1

    def on_start(self):
        self.start()

    def start(self, *args):
        anim = Animation(opacity = 1, duration = 1)
        anim += Animation(opacity = 1, duration = 3)
        anim += Animation(opacity = 0, duration = 1)
        anim.bind(on_complete=self.start)
        anim.start(self.root.ids[f"text{self.id}"])
        if self.id < 4:
            self.id += 1
        else:
            self.id -= 3

    def build(self):
        return Builder.load_file('hello.kv')

ChangingText().run()