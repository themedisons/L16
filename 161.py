v0 = float(input("v0 = "))
g = float(input("g  = "))
for i in range(10 + 1):
	t = float(i) / 10
	y = v0 * t - 0.5 * g * t ** 2
	print("v0 = %.2f; t = %.1f; y = %.3f" % (v0, t, y))
