value = int(raw_input())
values = [100, 50, 20, 10, 5, 2, 1]

print value

for i in range(len(values)):
	print "%d nota(s) de R$ %d,00" % (value / values[i], values[i])
	value -= values[i] * (value / values[i])