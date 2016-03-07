prices = [4.0, 4.5, 5.0, 2.0, 1.5]

a, b = map(int, raw_input().split())

print "Total: R$ %.2f" % (prices[a - 1] * b)