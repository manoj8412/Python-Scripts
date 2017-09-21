# https://math.stackexchange.com/questions/2438869/does-this-sequence-have-a-limit

import matplotlib.pyplot as plt
import string

def convert(x, b):
    r = ''
    while x > 0:
        r = string.printable[x % b] + r
        x //= b
    return r

def digit_adder(num, base=10):
	num = convert(num, base)
	return sum([int(x) for x in str(num)])

x = []
for n in range(3, 11):
	for i in range(1000):
		x.append((digit_adder(3**i, base=n)/digit_adder(3**(i+1), base=n)))

	plt.plot(x)
	plt.savefig("plot_" + str(n) + ".png")
	plt.clf()
	plt.cla()
	plt.close()
	print(x)
	x=[]
