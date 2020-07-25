song=input()
p="WUB"
n=[]
s=song.split(p)
for i in range(len(s)):
	if s[i]!='':
		n.append(s[i])
n=' '.join(n)

print (n)
