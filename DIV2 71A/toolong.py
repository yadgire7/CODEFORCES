n=int(input())
for i in range(n):
	word=(input())
	p=len(word)
	if p<=10:
		print (word)
	else:
		l=len(word)-2
		l=str(l)
		start=word[0]
		end=word[-1]
		print (start+l+end)

