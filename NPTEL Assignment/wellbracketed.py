def wellbracketed(word):
	rightBracket = 0
	leftBracket  = 0
	for i in word:
		if i == "(":
			rightBracket = rightBracket+1
		elif i==")":
			leftBracket =leftBracket+1
	if rightBracket == leftBracket:
		return True
	else:
		return False


print wellbracketed("22)")
print wellbracketed("(a+b)(a-b)")
print wellbracketed("(a(b+c)-d)((e+f)")