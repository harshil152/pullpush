class sum():

	@classmethod
	def add(cls,a,b):
		return (a+b);
	@staticmethod
	def grt(a,b):
		if(a>b):
			return a
		else:
			return b

class subsum(sum):
	def divide(a,b):
		return (a/b);

sum1=subsum.add(3,4)
sum2=subsum.add(3,4)

print sum1
