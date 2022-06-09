# hashbang python (#!/usr/bin/env python3)?
#clases.py

''' En este archivo incluyo las clases con las que trabajar para este
proyecto, y sus instancias'''

class Insumo:
	''' Clase que engloba los insumos necesarios para la elaboracion de
	los productos a vender'''

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

	def comprar(self, cantidad):
		self.stock += cantidad
		print(f'Quedan {self.stock} {self.unidad} de {self.nombre}')

#Instancias de Insumo
cera = Insumo('Cera de soja', 5, 'KG')
pabilo = Insumo('Pabilo para cera de soja', 2, 'M')
chapita = Insumo('Chapita para velas', 100, 'Un.')
vaso = Insumo('Vaso para vela', 12, 'Un.')
esencia = Insumo('Esencia para vela', 200, 'CC')

lista_de_insumos_vela = ['cera', 'pabilo', 'chapita', 'vaso', 'esencia']
lista_de_insumos_difusor = ['alcohol', 'vial', 'tapa', 'esencia difusor']



class Producto:
	def __init__(self, nombre, stock, precio):
		self.nombre = nombre
		self.stock = stock
		self.precio = precio

	def __str__(self):
		return f''

	def __repr__(self):
		return f''


class Vela(Producto): #REvisar
	def __init__(self, nombre, stock, precio, tipo):
		super().__init__(nombre, stock, precio)
		self.tipo = tipo

class Difusor:
	pass