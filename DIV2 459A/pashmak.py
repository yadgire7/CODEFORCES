import math
listin=input().split()
listUse=[int(i) for i in listin]
x1=listUse[0]
y1=listUse[1]
x2=listUse[2]
y2=listUse[3]
#slope=int((y2-y1)/(x2-x1))
dist=int(math.sqrt(pow((x2-x1),2)+pow((y2-y1),2)))
if y2-y1==0:
	x3=x2
	y3=y2+dist
	x4=x1
	y4=y1+dist
	print(x3,y3,x4,y4)
elif x2-x1==0:
	x3=x2+dist
	y3=y2
	x4=x1+dist
	y4=y1
	print(x3,y3,x4,y4)
elif (y2-y1!=0 and y2-y1==x2-x1) or (y2-y1!=0 and y2-y1==(x2-x1)*(-1)):
	x3=x2
	y3=y1
	x4=x1
	y4=y2
	print(x3,y3,x4,y4)

else:
	print(-1)
#print(dist)
