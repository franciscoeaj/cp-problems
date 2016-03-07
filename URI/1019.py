n = int(raw_input())

hours = n / 3600
n -= 3600 * hours
minutes = n / 60
n -= 60 * minutes
seconds = n

print "%d:%d:%d" % (hours, minutes, seconds)