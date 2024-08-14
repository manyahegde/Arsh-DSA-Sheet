# set matrix zeroes
def setMatrixZeroes(matrix):
    m=len(matrix)
    n=len(matrix[0])
    rows=set()
    cols=set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)
    for row in rows:
        for j in range(n):
            matrix[row][j]=0
    for col in cols:
        for j in range(m):
            matrix[j][col]=0
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setMatrixZeroes(matrix)
print(matrix)