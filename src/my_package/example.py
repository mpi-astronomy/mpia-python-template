def add_one(number):
	if isinstance(number, (float,int)):
		return number + 1
	elif isinstance(number, (str)):
		return number + '1'
	else:
		raise TypeError('Expecting an int, float or string.")
