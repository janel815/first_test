def fibonacci(n):
	count = []

	for i in range(n+1):
		if i == 0 :
			count.append(i)
		elif i == 1 :
			count.append(i)
		else:
			value = count[i-1]+count[i-2]
			count.append(value)
	return count
	
print fibonacci(10)					


# park's answer

pivo = []
pivo.append(0)
pivo.append(1)
num = input('number ?')
if num > 2:
	for i in range(1, num-1):
		pivo.append(pivo[i-1]+pivo[i])

for i in range(0, len(pivo)):
	if num >i:
		print pivo[i]		