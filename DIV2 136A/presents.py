n=int(input())
arr=[int(x) for x in input().split()]
res=[None]*n
k=1
for i in range(n):
	k=arr[i]
	res[k-1]=i+1

print (*res,sep=" ")
	
	
		
	
		
		
		
	
