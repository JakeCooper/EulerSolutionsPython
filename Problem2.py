sumit = 0
backX = 1
frontX = 2
tempX = 0
while frontX < 4000000:
	if frontX % 2 == 0:
		sumit += frontX
	tempX = frontX + backX #newFront
	backX = frontX
	frontX = tempX
	
print sumit