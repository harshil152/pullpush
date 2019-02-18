def gen(start,inc):
	list1=[]
	temp=start
	while True:
		list1.append(temp)
		temp+=inc
		yield list1
x=gen(1,2)
print x.next()
print x.next()
print x.next()
print x.next()
