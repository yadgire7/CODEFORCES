from collections import Counter
letters=input()
count=0
trim=letters[1:len(letters)-1]

trim=trim.replace(',','')
trim=trim.split()

print (len(Counter(trim).keys()))
