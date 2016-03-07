x, y = map(float, raw_input().split())

if (x == 0 and y == 0):
	result = "Origem"
elif (x == 0 and y != 0):
	result = "Eixo Y"
elif (x != 0 and y == 0):
	result = "Eixo X"
else:
	if (x > 0 and y > 0):
		result = "Q1"
	elif (x < 0 and y > 0):
		result = "Q2"
	elif (x < 0 and y < 0):
		result = "Q3"
	elif (x > 0 and y < 0):
		result = "Q4"

print result