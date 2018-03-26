cars = ["Rishav","AUDI","Mclaren"]
i=0;
while i< len(cars):
	print cars[i]
	i+=1

print "\n"

for i in range(len(cars)):
	print cars[i]

print "\n"

for x in enumerate(cars):
	print x[0],x[1]

print "\n"

print enumerate(cars)

for x in enumerate(cars,start=1):
	print x[0],x[1]

print "\n"

# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]
 
# Single dictionary holds prices of cars and 
# its accessories.
# First two items store prices of cars and
# next three items store prices of accessories.
prices = {1:"570000$", 2:"68000$", 3:"450000$",
          4:"890000$", 5:"4500$"}
 
for index,c in enumerate(cars,start=1):
 	print "car:%s prices:%c"%(c,prices[index])

for index,a in enumerate(accessories,start=1):
 	print "Accessory:%s Price:%s"%(a,prices[index+len(cars)])

for c,a in zip(cars,accessories):
	print "Car:%s, Accessory requires:%s"%(c,a)

 
# Unzip lists
l1,l2 = zip(*[('Aston', 'GPS'), 
              ('Audi', 'Car Repair'), 
              ('McLaren', 'Dolby sound kit') 
           ])
 
# Printing unzipped lists      
print(l1)
print(l2)
