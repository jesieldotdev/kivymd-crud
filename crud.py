from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import TwoLineListItem, TwoLineAvatarListItem
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty
from kivymd.toast import toast
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel
import re
from kivy.uix.recycleview import RecycleView



# Configurações de Tela
from kivy.utils import platform
if platform != 'android':
    Window.size = 300, 600

from kivy.storage.jsonstore import JsonStore
# Banco de Dados
store = JsonStore('database/banco.json')
# store.put('tito', nome = 'Mathieu', idade=32)


kv = Builder.load_file('crud.kv')


		
	

class Item(OneLineAvatarIconListItem):
	left_icon = StringProperty()
	right_text = StringProperty()


class ListComAvatar(TwoLineAvatarListItem):
	source = StringProperty("img/user-64.png")


class VendasWindow(MDBoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def existe(self, text='', search=False):
		
		def add_nome(nome, idade):
			self.ids.rv.data.append(
				{
					'viewclass': 'ListComAvatar',
					'text': str(nome),
					'secondary_text': str(idade)
					

				}
			)


		self.ids.rv.data = []
		
		for key in store:
			
			nome = store.get(key)['nome']
			idade = store.get(key)['idade']
			if search:
				if text in nome:
					add_nome(nome, idade)
			else:
				add_nome(nome, idade)
		
		
				

	def Adicionar(self):
		
		idade = self.ids.idade.text
		colecao = self.ids.colecao.text
		

		if store.exists(colecao):
			print(f'{colecao} já existe')
			toast(f'{colecao} já existe')
		else:
			store.put(colecao, nome = colecao, idade=idade)
			toast(f'{colecao} foi adicionado')
			

	def Remover(self):
		key = self.ids.colecao.text
		if store.exists(key):
			store.delete(key)
			toast(f'{key} foi deletado')

		else:
			print(f'{key} não existe')
			toast(f'{key} não existe')


	def Filtrar(self):
		print('Filtrar')
		toast('Test Kivy Toast')


class MyCrud(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.screen = VendasWindow()
	data = {
		'Mostrar todos': 'text-box-search',
		'Adicionar': 'notebook-plus-outline', 
		'Remover': 'delete', 'Filtrar': 'magnify'
		}
		

	def on_start(self):
		self.screen.existe()
		
		
	def abrir(self, instance):
		toast(instance.text)

	

	def callback(self, instance):
		Snackbar(text = instance.icon).open()
		# if instance.icon == 'text-box-search':
		# 	self.root.Listar()

		# elif instance.icon == 'notebook-plus-outline':
		# 	self.root.Adicionar()

		# if instance.icon == 'delete':
		# 	self.root.Remover()

		# if instance.icon == 'magnify':
		# 	self.root.Filtrar()
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Purple"
		
		lista = {'nome':'Adicionar', 'icon': 'plus'}, {'nome':'Remover', 'icon': 'delete'}
		menu_items = [{ "right_text": str(key.get('nome')) ,"left_icon": str(key.get('icon')),"viewclass": "Item" , "on_release": lambda x=(str(key.get('nome'))): self.menu_chamada(x),} for key in lista]
		self.menu = MDDropdownMenu(
			items=menu_items, 
			width_mult=4)
	
		return self.screen

	def chamada(self, button):
		self.menu.caller = button
		self.menu.open()

	def menu_chamada(self, text_item):
		self.menu.dismiss()
		Snackbar(text=text_item).open()
		

if __name__ == '__main__':
	MyCrud().run()
