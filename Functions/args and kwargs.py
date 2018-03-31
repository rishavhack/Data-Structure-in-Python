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

def test(arg1,arg2,arg3):
	print "arg1",arg1
	print "arg2",arg2
	print "arg3",arg3

args=("hey",17,"Rishav")
test(*args)
print "\n"
kwargs={"arg1":"hey","arg2":"14","arg3":"Rishav"}
test(**kwargs)