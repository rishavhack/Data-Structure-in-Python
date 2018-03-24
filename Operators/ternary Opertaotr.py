#Simple Method

a,b =10,20
min = a if a<b else b
print min
print "\n"

#Direct Method 
print (b,a)[a<b]
print {True:a,False:b}[a<b]
# lamda is more efficient than above two methods
# because in lambda  we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())