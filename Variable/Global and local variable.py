#This func used global
def f():
	print s

s="I hate"
f()
print "\n"
#This func  has a both variable

def fg():
	s= "Rishav"
	print s

s="I hate"
fg()
print s

#global keyword
def fr():
	global s
	print s
	s ="Looks handsome"
s ="Python mere jann"
fr()
print s