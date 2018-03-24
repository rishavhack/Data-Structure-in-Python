def fun(a,b,c,d):
	print a,b,c,d

my_list = [2,5,7,8]

fun (*my_list)
print "\n"
#range example
args = [2,9]
print range(*args)
print "\n"

def mySum(*args):
	sum = 0
	for i in range(0,len(args)):
		sum = sum + args[i]
	return sum
print mySum(1,2,3,4,5)
print mySum(10,20)

print "\n"

def fun1(a,b,c):
	print a,b,c
def fun2(*args):
	args=list(args)
	args[0]="Rishav"
	args[1]="Srivastava"
	fun1(*args)
fun2('hello','beautui','awesome')


#using dictionay
# dictionary items using **
def fun(a,b,c):
	print a,b,c
d = {'a':2,'b':4,'c':10}
fun (**d)
print "\n"
#Another Example
def fun(**kwargs):
	print(type(kwargs))
	for key in kwargs:
		print "%s = %s" %(key,kwargs[key])
fun(name="geeks",id="101",langauge="Python")