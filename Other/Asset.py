import numpy as np



class Asset:

	def __init__(self, name, data=None, amount=0):
		self.name = name
		self.data = data
		self.amount = amount



	def update_amount(self, new_amount):
		self.amount = new_amount


	def update_data(self, new_data):
		self.data = new_data