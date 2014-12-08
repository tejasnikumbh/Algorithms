if __name__ == "__main__":
	f = open('exp.txt')
	f2 = open('my.txt')
	a = []
	b = []
	for i in range(1000):
		a.append([int(x) for x in f.readline().rstrip().split()])
		b.append([int(x) for x in f2.readline().rstrip().split()])
	for i in range(1000):
		if(a[i][0] != b[i][0]):
			print "Index : " + str(i) + " Expected : " + str(a[i][0]) + "Your : " + str(b[i][0])