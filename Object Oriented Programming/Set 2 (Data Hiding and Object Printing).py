#In Python, we use double underscore (Or __) before the attributes name and those attributes will not be directly visible outside
class myClass:
	__hiddenVariable = 0
	def add(self,increment):
		self.__hiddenVariable += increment
		print self.__hiddenVariable

myObject = myClass()
myObject.add(2)
myObject.add(5)
#Here it show error
#print myObject.__hiddenVariable

print myObject._myClass__hiddenVariable

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
 
    def __str__(self):
        return "From str method of Test: a is %s," \
              "b is %s" % (self.a, self.b)
 
# Driver Code        
t = Test(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()



class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
 
# Driver Code        
t = Test(1234, 5678)
print(t) 