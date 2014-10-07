maxNumber = 0

for x in reversed(xrange(100, 999)):
	for y in reversed(xrange(100, 999)):
		if str(x*y) == str(x*y)[::-1]:
			if x*y > maxNumber:
				maxNumber = x*y

print maxNumber