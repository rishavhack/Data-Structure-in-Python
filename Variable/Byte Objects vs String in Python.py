# Python code to demonstate String encoding
 
# initialising a String 
a = 'GeeksforGeeks'
 
# initialising a byte object
c = b'GeeksforGeeks'

d = a.encode('ASCII')
print d
if (d==c):
    print ("Encoding successful")
else : print ("Encoding Unsuccessful")

#Decoding
d = c.decode('ASCII')
if (d==a):
    print ("Decoding successful")
else : print ("Decoding Unsuccessful")