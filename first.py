def upper(func):
	# print "HELLO:"
	def convert():
		upr=func()
		if upr.isupper():
			return upr.lower();
		else:
			return upr.upper();
		return convert;
@upper
def printer():
	msg=raw_input("Enter string:")
	return msg
print printer()

