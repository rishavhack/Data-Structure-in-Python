s = "My name is Rishav"
subs = "is"
flag = False
pos = -1
n = len(s)
count = 0
while True:
    pos = s.find(subs,pos+1,n)
    print pos
    if pos == -1:
        break
    print "found at index",pos
    flag = True
    count = count+1

if flag==False:
    print "Not found"