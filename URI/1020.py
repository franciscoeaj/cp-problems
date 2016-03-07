n = int(raw_input())

print "%d ano(s)" % (n / 365)
n -= 365 * (n / 365)
print "%d mes(es)" % (n / 30)
n -= 30 * (n / 30)
print "%d dia(s)" % n