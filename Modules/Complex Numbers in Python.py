import cmath
x = 5
y = 3
z = complex(x,y);
print "X and Y",x,y
print "The real part of complex number is",z.real
print "The imaginary part of complex number is",z.imag
x = -1.0
y= 0.0
z = complex(x,y);
print "The phase of complex number is :",cmath.phase(z)

