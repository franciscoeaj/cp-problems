a, b = map(int, raw_input().split())

if max(a, b) % min(a, b) == 0:
	print "Sao Multiplos"
else:
	print "Nao sao Multiplos"