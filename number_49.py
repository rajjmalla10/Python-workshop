#  Let  x¯=(x1,x2...xn)  and  y¯=(y1,y2...yn)  be two n dimensional vectors. Their dot product, denoted  x¯.y¯  , is defined as  x¯.y¯=x1y1+x2y2+x3y3+...+xnyn  . Write and test a Python function that returns the dot product of two given vectors (represented as lists of the same length).

def dot_product(x,y):
    if len(x) != len(y):
        raise ValueError("Dimension of vector not equal")
    i = 0
    dot_product = 0 
    for x1, y1 in zip(x,y):
        dot_product += x1 * y1
    return dot_product
            
    

n = int(input("Enter number of dimension of vectors: "))
x = [float(input(f"enter value of x[{i+1}]: ")) for i in range(n)]
y = [float(input(f"enter value of y[{j+1}]: ")) for j in range(n)]
print(f"The dot product of {n} dimension x and y vector: {dot_product(x,y)}")

        
            