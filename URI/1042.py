values = map(int, raw_input().split())

asc_values = sorted(values)
for i in range(len(asc_values)):
	print asc_values[i]

print

for i in range(len(values)):
	print values[i]