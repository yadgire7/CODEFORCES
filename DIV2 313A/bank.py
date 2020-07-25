ac=input()
if ac[0]!='-':
	print(ac)
else:
	one=ac[0:len(ac)-1]
	two=list(ac[0:len(ac)-2])
	last=ac[-1]
	two.append(last)
	two=''.join(two)
	one=int(one)
	two=int(two)
	print (max(one,two))
