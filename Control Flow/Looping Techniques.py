for key,value in enumerate(['Rishav','Srivastva','Big']):
	print key,value

# python code to demonstrate working of zip()
 
# initializing list
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

for question,answer in zip(questions,answers):
	print "what is ur {{0}}? I am {{1}}".format(question,answer)

d = { "geeks" : "for", "only" : "geeks" }
 
# using iteritems to print the dictionary key-value pair
print ("The key value pair using iteritems is : ")
for i,j in d.iteritems():
    print i,j


 print "\n"

 basket = ['guave', 'orange', 'apple', 'pear', 
          'guava', 'banana', 'grape']
 
# using sorted() and set() to print the list
#  in sorted order
for fruit in sortedset(basket):
    print fruit


print "\n"