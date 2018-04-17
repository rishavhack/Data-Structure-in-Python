class Test:
	def fun(self):
		print "Hello"

obj = Test()
obj.fun()

class Person:
	def __init__(self,name):
		self.name=name
	def say_hi(self):
		print "Hello,my name is",self.name
p = Person('Rishav')
p.say_hi()


class CSStudent:
	"""docstring for CSStudent"""
	stream = 'cse'
	def __init__(self, roll):
		self.roll = roll

a = CSStudent(101)
b = CSStudent(102)

print a.stream
print b.stream
print a.roll
print b.roll

print CSStudent.stream

class CSStudents:
	"""docstring for CSStudents"""
	stream = 'cse'
	def __init__(self,roll):
		self.roll = roll

	def setAddress(Self,address):
		self.address=address

	def getAddress(self):
		return self.address

a = CSStudents(101)
a.setAddress("Brahmpura,Muzaffarpur")
print a.getAddress()

		