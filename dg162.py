v0 = float(input("v0 = "))
g = float(input("g  = "))
for i in range(400 + 1):
	t = float(i) / 100
	y = v0 * t - 0.5 * g * t ** 2
	print("%.3f	%.3f" % (t, y))
