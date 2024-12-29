#  Write and test a Python function that returns the sum of the elements on the main diagonal (upper left to lower right) of a square matrix (represented as a list of lists eg. [[9, 8, 7], [6, 5, 4], [3, 2, 1]]). In linear algebra, this value is called the trace of the matrix. Note: your solution should work for any sized square matrix passed to it

def sum_diagonal_matrix(z):
    i = 0
    diagonal_sum = 0 
    j = 0
    while i < x and j < y:
        diagonal_sum += z[i][j] 
        i+=1
        j+=1
    
    return diagonal_sum
    


if __name__ == "__main__":
    x,y = map(int, input("enter the number of rows and cloumn for matrix z (seperated by space): ").split())
    if x != y:
        raise ValueError ("x and y should have equal number of element")
    Matrix = [[int(input(f"Enter  value for matrix [{i}][{j}]"))for j in range(y)] for i in range(x)]
    
    result = sum_diagonal_matrix(Matrix)
    print(result)
    