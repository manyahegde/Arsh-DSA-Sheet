# chocolate distribution problem
def findMinDif(A,N,M):
    A.sort()
    diff=float('inf')
    for i in range(N-M+1):
        minimum=A[i]
        maximum=A[i+M-1]
        diff=min(diff, maximum-minimum)
    return diff
N=7
M=3
A=[7, 3, 2, 4, 9, 12, 56]
print(findMinDif(A,N,M))