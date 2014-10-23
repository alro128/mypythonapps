class cuentat:
	def __init__(self, tipo, nombre):
		self.nombre = nombre.lower()
		self.tipo = tipo.lower()
		self.debe = 0
		self.haber = 0
	def asiento(self,nlado,nval):
		if (nlado == 'debe'):
			self.debe += int(nval)
		else:
			self.haber += int(nval)
	def cierre(self):
		if (self.tipo == 'af' or self.tipo == 'ac' or self.tipo == 'ga'):
			return self.debe-self.haber
		else:
			return self.haber-self.debe
