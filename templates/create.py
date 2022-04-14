from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import os

kv = Builder.load_file('templates/create.kv')

class TelaCadastro(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		pass


kv = Builder.load_file(os.path.join(os.path.dirname(__file__), "create.kv"))