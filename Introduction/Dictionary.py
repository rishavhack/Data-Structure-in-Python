slang={'cheerio':'goodbye','Rishav':'Srivastava','Priy':'kamal'}
print "1.slang->",slang
print "2.slang['Rishav']->",slang['Rishav']
print "3.To add key value in dictionary"
print "dictionaryName['key']=['Value']"
slang['Seema']='Srivastava'
slang['Saumya']=8
print "4.slang->",slang
print "5.To update the value"
print "6.dictionary['key']='value'"
slang['Rishav']='Kumar'
print "7.slang->",slang
print "8.To delete"
print "9.DictionaryNAme['key']"
del slang['cheerio']
print "10.slang->",slang
print "Trying to access a key that does't exist will cause an error like slang['bloody']"
print "it return keyeroor:'bloody'"
print "If u want to check if a word is in dictionary,use get()."
result = slang.get('bloody')
print "result = slang.get('bloody')"
print "result->",result
if result:
	print result
else:
	print "Key does't exist"
