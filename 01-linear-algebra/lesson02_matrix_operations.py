import numpy as np

vector = np.array([3,4])

A = np.array([[2,0],[0,1]])
B = np.array([[1,0],[0,3]])
print(vector)
print(A)
print(B)

D = [
    [1, 2, 3],
    [4, 5, 6]
]
F = [
    [7, 8],
    [9, 10],
    [11, 12]
]
# function for matrix and vector multiplication
def matrix_vector_multiply(A,vector):
    """

    :param A: matrix which will be multiplied by the vector     \
    :param vector: which will be multiplied by the matrix
    :return: result of matrix and vector multiplication
    """
    transformed_vector = []
    for i in range(len(A)):
        result = 0
        for j in range(len(vector)):
            result += A[i][j] * vector[j]
        transformed_vector.append(result)
    return  transformed_vector


print(matrix_vector_multiply(A,vector))

if len(A[0]) != len(B):
    raise ValueError("Matrix dimensions do not match.")




# function for multiplying 2 matrices
def matrix_matrix_multiply(A,B):
    """
    :param B: matrix which will be multiplied by the matrix A
    :param A: matrix which will be multiplied by the matrix B
    :return: dot product of matrix A and matrix B
    """
    # initializing the empty matrix
    c = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                c[i][j] += A[i][k] * B[k][j]

    return c

print(matrix_matrix_multiply(D,F))