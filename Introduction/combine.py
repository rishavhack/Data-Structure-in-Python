print "Combine List of list"
breakfast=['Spam n Egg','Spam n Jam','Spam n Ham']
lunch=['SLT','PB&S']
dinner=['Spalad','Spamghetti','Spam noodle soup']
print "breakfast->",breakfast
print "lunch->",lunch
print "dinner->",dinner
menu = [breakfast,lunch,dinner]
print "menu->",menu
print "breakfast\t",menu[0]
print "lunch\t",menu[1]
print "dinner\t",menu[2]
print "menu[0][1]\t",menu[0][1]
print "menu[1][1]\t",menu[1][1]
print "Dictionary of Lists"
menus={'breakfast':['Spam n Egg','Spam n Jam','Spam n Ham'],
'lunch':['SLT','PB&S'],
'dinner':['Spalad','Spamghetti','Spam noodle soup']}
print "menus:\t",menus
print "You can access by menus['breakfast']"
print 'BreakFast Menu:\t',menus['breakfast']
print 'Lunch :\t',menus['lunch']
