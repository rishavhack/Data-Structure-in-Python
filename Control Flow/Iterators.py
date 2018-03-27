#Construtor
class Test(object):
	"""docstring for Test"""
	def __init__(self, limit):
		self.limit = limit
	def __iter__(self):
		self.x =10
		return self
	def next(self):
		x = self.x
		if x > self.limit:
			raise StopIteration

		self.x = x+1;
		return x

for i in Test(15):
	print i

for i in Test(5):
	print i
