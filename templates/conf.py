from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import os

class Conf(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		return kv



kv = Builder.load_file(os.path.join(os.path.dirname(__file__), "conf.kv"))