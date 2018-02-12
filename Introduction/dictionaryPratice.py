menuPrice={'Cheeze':0.50,'Burger':1.50,'Pizza':2.50}
print menuPrice
for name,price in menuPrice.items():
	print name,':$',format(price,'.2f')