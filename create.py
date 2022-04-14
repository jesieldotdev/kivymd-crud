from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import os


class TelaCadastro(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		return Builder.load_file("create.kv")