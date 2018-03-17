x = input("Enter First number");
y = input("Enter Second number");
z = input("Enter Third number");

if x > y:
	if x > z:
		print "%d is max" %x
	else:
		print "%d is max" %z
elif y>z:
	print "%d is max" %y
else:
	print "%d is max" %z