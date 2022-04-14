from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import os

class Conf(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		return Builder.load_file("conf.kv")