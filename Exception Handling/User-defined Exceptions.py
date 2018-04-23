class MyError(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

print MyError(3*2)
# try:
# 	raise (MyError(3*2))
# except MyError as error:
# 	print 'A new Exception occured',error.value
