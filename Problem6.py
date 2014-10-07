squareEach = 0
squareAll = 0

for x in xrange(1, 101):
	squareEach += x * x
	squareAll += x

print (squareAll * squareAll) - squareEach