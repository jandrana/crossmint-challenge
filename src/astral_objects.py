class AstralObject:
	def __init__(self, row, column):
		self.row = row
		self.column = column
	
	def create(self, api_client):
		raise NotImplementedError("Subclass must implement create method!")

class Polyanet(AstralObject):
	def create(self, api_client):
		api_client.create_polyanet(self.row, self.column)

class Soloon(AstralObject):
	def __init__(self, row, column, color):
		self.row = row
		self.column = column
		self.color = color

	def create(self, api_client):
		api_client.create_soloon(self.row, self.column, self.color)

class Cometh(AstralObject):
	def __init__(self, row, column, direction):
		self.row = row
		self.column = column
		self.direction = direction

	def create(self, api_client):
		api_client.create_cometh(self.row, self.column, self.direction)