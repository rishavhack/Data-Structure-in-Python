def testify(arg,*argv):
	print "First argument :",arg
	for arg in argv:
		print "Next argument through *argv",arg

testify("Hello","Welcone","to","Python")

def hello(**kwargs):
	if kwargs is not None:
		for key,value in kwargs.iteritems():
			print "%s==%s"%(key,value)

hello(name="RishavIsName")