def meassage(str):
	def add():
		return "Welcome to "

	return add() + str

def site(site_name):
	return site_name

print meassage(site("Rishav"))

print "\n"

def decorate(fun):
	def addWelcome(site):
		return "Welcome to "+ fun(site)
	return addWelcome;

@decorate
def site(site):
	return site;

print site("Rishav")
print "\n"

def attach(func):
	func.data = 3
	return func
@attach
def add(x,y):
	return x+y
print add(2,3)
print add.data
