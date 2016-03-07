import math

value = float(raw_input())
notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print "NOTAS:"
for i in range(len(notes)):
	print "%d nota(s) de R$ %.2f" % (value / notes[i], notes[i])
	value -= notes[i] * (int(value) / notes[i])

print "MOEDAS:"
for i in range(len(coins)):
	print "%d moeda(s) de R$ %.2f" % (math.floor(value / coins[i]), coins[i])
	value -= coins[i] * (math.floor(value / coins[i]))