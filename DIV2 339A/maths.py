exp=input()
plus={"+"}
for i in plus:
	exp=exp.replace(i,"")
exp=list(exp)
exp.sort()
for j in range(2*len(exp)-1):
	if j%2==1:
		exp.insert(j,"+")
exp=''.join(exp)
print (exp)
