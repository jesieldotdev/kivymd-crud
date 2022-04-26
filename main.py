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
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel
import re
from kivy.uix.recycleview import RecycleView
from conf import Conf
from create import TelaCadastro
import requests

response = requests.get('https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/users').json()

print(response)



# Configurações de Tela
from kivy.utils import platform
if platform != 'android':
    Window.size = 300, 600

from kivy.storage.jsonstore import JsonStore
# Banco de Dados
store = JsonStore('database/banco.json')
# store.put('tito', nome = 'Mathieu', idade=32)


kv = Builder.load_file('main.kv')



class Item(OneLineAvatarIconListItem):
	left_icon = StringProperty()
	right_text = StringProperty()


class ListComAvatar(TwoLineAvatarListItem):
	source = StringProperty()


class SM(ScreenManager):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.add_widget(InicioWindow(name='inicio'))
		self.add_widget(TelaCadastro(name='cadastro'))
		self.add_widget(Conf(name='conf'))

class InicioWindow(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def existe(self, text='', search=False):
		
		def add_nome(nome, idade, avatar):
			self.ids.rv.data.append(
				{
					'viewclass': 'ListComAvatar',
					'text': str(nome),
					'secondary_text': str(idade),
					'source': str(avatar)

				}
			)


		self.ids.rv.data = []
		
		for key in response:
			
			nome = key['name']
			idade = key['idade']
			avatar = key['avatar']
			if search:
				if text in nome:
					add_nome(nome, idade, avatar)
			else:
				add_nome(nome, idade, avatar)
		
		
				

	def add(self):
		
		idade = self.ids.idade.text
		colecao = self.ids.colecao.text
		

		if store.exists(colecao):
			print(f'{colecao} já existe')
			toast(f'{colecao} já existe')
		else:
			store.put(colecao, nome = colecao, idade=idade)
			toast(f'{colecao} foi adicionado')
			

	def delete(self):
		key = self.ids.colecao.text
		if store.exists(key):
			store.delete(key)
			toast(f'{key} foi deletado')

		else:
			print(f'{key} não existe')
			toast(f'{key} não existe')

	


class MyCrud(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.screen = SM()
		self.inicio = InicioWindow()
	data =(
			{
				'Create': 'file-document-edit',
				'Read': 'book-open-variant', 
				'Update': 'update',
				'Delete': 'delete',
			}
		)

	def on_start(self):
		self.inicio.existe()	
		
	def abrir(self, instance):
		toast(instance.text)

	def voltar(self):
		self.root.current = self.previous_screen

	

	def callback(self, instance):
		# Snackbar(text = instance.icon).open()
		if instance.icon:
			self.screen.current = 'cadastro'

	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Purple"
		
		lista = (
					{'nome':'Ajuda', 'icon': 'help-box'},
					{'nome':'Configurações', 'icon': 'cog'},
				)
		
		menu_items = (
						{
							"right_text": str(key.get('nome')) ,
							"left_icon": str(key.get('icon')),
							"viewclass": "Item" ,
							"on_release": lambda x=(str(key.get('nome'))): self.menu_chamada(x),
						} for key in lista
					)
		
		self.menu = MDDropdownMenu(
			items=menu_items, 
			width_mult=4)
	
		return self.inicio

	def chamada(self, button):
		self.menu.caller = button
		self.menu.open()

	def menu_chamada(self, text_item):
		self.menu.dismiss()
		if text_item == 'Configurações':
			self.screen.current = 'conf'
			print(text_item)
		

if __name__ == '__main__':
	MyCrud().run()
