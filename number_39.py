def sumVectors(x, y):
    vect = len(x)*[0]  # create a list of the same length as x, filled with 0s
    i = 0
    while i < len(x):
        vect[i] = x[i] + y[i]
        i += 1
    return vect

print(sumVectors([1,2,3],[6,5,4]))
