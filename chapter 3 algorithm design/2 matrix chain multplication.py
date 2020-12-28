'#Dynamic programming excercise'

# For example, let's look at three matrices—P, Q, and R. To compute the multiplication of
# these three matrices, we have many possible choices
# (because the matrix multiplication is
# associative), such as (PQ)R = P(QR). So,
# if the sizes of these matrices are:
#P is a 20 × 30,
#Q is 30 × 45,
#R is 45 x 50,
#then, the number of multiplications for (PQ)R and P(QR) will be:
#
# (PQ)R = 20 x 30 x 45 + 20 x 45 x 50 = 72,000
# P(QR) = 20 x 30 x 50 + 30 x 45 x 50 = 97,500
import sys
def MatrixChain(mat, i, j):
    if i == j:
        return 0
    minimum_computations = sys.maxsize
    for k in range(i, j):
        count = (MatrixChain(mat, i, k) + MatrixChain(mat, k+1, j)+mat[i-1] * mat[k] * mat[j])
        if count < minimum_computations:
            minimum_computations= count;
    return minimum_computations;

matrix_sizes = [20, 30, 45, 50];
print("Minimum multiplications are", MatrixChain(matrix_sizes , 1,
len(matrix_sizes)-1))
