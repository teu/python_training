class TestableCalculator:
	outputer = ''
	"""Initializing the object with the outputter strategy
	@outputer Output
	"""
	def __init__(self, outputer):
		self.outputer = outputer
	
	def dodaj(self, a, b):
		# the strategy implementation is responsible for doing the correct
		# thing
		result = "a + b = " + str(a + b)
		return self.outputer.output(result)
	
	def odejmij(self, a, b):
		result = "a - b = " + str(a - b)
		return self.outputer.output(result)

