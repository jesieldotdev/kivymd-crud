from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineListItem, TwoLineAvatarListItem
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty
from kivymd.toast import toast
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

store = JsonStore('banco.json')

# store.put('tito', nome = 'Mathieu', idade=32)
#Window.size = 300, 600
kv = Builder.load_file('crud.kv')


class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    '''Implements a material design v3 card.'''

    text = StringProperty()




class ListComAvatar(TwoLineAvatarListItem):
	source = StringProperty("data/logo/kivy-icon-256.png")




class VendasWindow(MDBoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		

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


	def Listar(self):
		res = store.find()
		for key in store:
			nome = store.get(key)['nome']
			idade = store.get(key)['idade']

			self.ids.container.add_widget(ListComAvatar(text = f'[b]{nome}[/b]' , secondary_text = f'{idade} anos'))
	
		for key in store:
			print(store.get(key)['nome'])
			print(store.get(key)['idade'])

			


class MyCrud(MDApp):
	data = {
	'Mostrar todos': 'text-box-search',
	'Adicionar': 'notebook-plus-outline', 
	'Remover': 'delete', 'Filtrar': 'magnify'
	}
	def on_start(self):
		self.root.Listar()
		styles = {
            "elevated": "#f6eeee", "filled": "#f4dedc", "outlined": "#f8f5f4"
        }
        for style in styles.keys():
            self.root.ids.content.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style=style,
                    text=style.capitalize(),
                    md_bg_color=get_color_from_hex(styles[style]),
                )
            )
		
	def abrir(self, instance):
		print('Certo')

	def callback(self, instance):
		print(instance.icon)
		if instance.icon == 'text-box-search':
			self.root.Listar()

		elif instance.icon == 'notebook-plus-outline':
			self.root.Adicionar()

		if instance.icon == 'delete':
			self.root.Remover()

		if instance.icon == 'magnify':
			self.root.Filtrar()
	def build(self):
		
		return VendasWindow()

	



	


if __name__ == '__main__':
	MyCrud().run()
