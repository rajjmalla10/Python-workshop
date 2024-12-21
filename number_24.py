nMax = int(input("enter number of interger u want to add: "))
n = 1
for j in range(nMax):
    while n <= j and j % 2 != 0:
        sum1n = 0
        i = 1
        while i <= n:
            sum1n += i
            i += 2
        print('{0:3d} {1:6d}'.format(n, sum1n))
        n += 2