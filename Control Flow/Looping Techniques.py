for key,value in enumerate(['Rishav','Srivastva','Big']):
	print key,value

# python code to demonstrate working of zip()
 
# initializing list
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

for question,answer in zip(questions,answers):
	print "what is ur {{0}}? I am {{1}}".format(question,answer)

