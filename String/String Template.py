from string import Template
#Create template that has placeholder for value of x
t = Template('x is $x')
print t.substitute({'x':1})

student=[('Rishav',88),('Ankit',78),('Bob',92)]
t = Template('Hi $name,you got $marks marks')
for i in student:
	print t.substitute(name = i[0],marks=i[1])