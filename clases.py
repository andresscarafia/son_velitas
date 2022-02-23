#clases.py

''' En este archivo incluyo las clases con las que trabajar para este proyecto'''

class Insumo:
	def __init__(self, nombre, stock, unidad):
	    self.nombre = nombre
	    self.stock = stock
	    self.unidad = unidad

	def __str__(self):
		return f'{self.nombre} - {self.stock} {self.unidad}'

	def __repr__(self):
		return f'Insumo({self.nombre}, {self.stock}, {self.unidad})'

	def usar(self, cantidad):
		self.stock -= cantidad
		print(f'Quedan {self.stock} {self.unidad} de {self.nombre}')

lista_de_insumos_vela = ['cera', 'pabilo', 'chapita', 'vaso', 'esencia']
lista_de_insumos_difusor = ['alcohol', 'vial', 'tapa', 'esencia difusor']

class Producto:
	pass


class Vela(Producto):
	pass

class Difusor(Producto):
	pass