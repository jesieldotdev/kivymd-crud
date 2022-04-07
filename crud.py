from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineListItem
from kivymd.toast import toast
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

store = JsonStore('banco.json')

# store.put('tito', nome = 'Mathieu', idade=32)


Window.size = 300, 600
kv = Builder.load_file('crud.kv')



class VendasWindow(MDBoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		

	def Adicionar(self):
		nome = self.ids.nome.text
		idade = self.ids.idade.text
		colecao = self.ids.colecao.text
		

		if store.exists(colecao):
			print(f'{colecao} já existe')
			toast(f'{colecao} já existe')
		else:
			store.put(colecao, nome = nome, idade=idade)
			toast(f'{colecao} foi adicionado')
			

	def Remover(self):
		key = self.ids.colecao.text
		if store.exists(key):
			store.delete(key)
		else:
			print(f'{key} não existe')
			toast(f'{key} não existe')

	def Filtrar(self):
		print('Filtrar')
		toast('Test Kivy Toast')

	def Mostrar_db(self, **kwargs):
		lb_nome = self.ids.lbl1
		lb_idade = self.ids.lbl2
		
		res = store.find()
		for key in store:
			print(key)
			lb_nome.text = str(store.get(key.nome))
			lb_idade.text = str(item[1]["idade"])

	def listar(self):
		res = store.find()
		for key in store:
			nome = store.get(key)['nome']
			idade = store.get(key)['idade']

			self.ids.container.add_widget(TwoLineListItem(text = nome , secondary_text = idade))

		for key in store:
			print(store.get(key)['nome'])
			print(store.get(key)['idade'])


			


class MyCrud(MDApp):
	def build(self):
		self.theme_cls.material_style = "M3"
		return VendasWindow()

	


if __name__ == '__main__':
	MyCrud().run()
