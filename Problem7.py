import math

def prime(num):
	denominator = 3
	if num % 2 == 0 and num != 2:
		return False
	if num == 2:
		return False

	while (denominator <= math.sqrt(num)):

		if(num%denominator == 0):
			return False
		denominator += 2

	return True

num = 3
n = 1

while (True):

	if prime(num):
		n+= 1
	if n > 10000:
		break
	num += 2

print num


