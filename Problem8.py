import sys

data = open("input.txt")
data = data.read()
i = 0
maxSum = 0
sumIt = 1
for x in range(0, len(data) - 12):
	for t in range(0, 13):
		sumIt = sumIt * int(data[x + t])
	if sumIt > maxSum:
		maxSum = sumIt
	sumIt = 1

print(maxSum)
