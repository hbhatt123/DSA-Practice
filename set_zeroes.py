

def set_zeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    flag = False
    row = False
    column = False
    if matrix[0][0] == 0:
        flag = True
    for i in range(1,n):
        if matrix[i][0] == 0:
            column = True
            break
    for i in range(1,m):
        if matrix[0][i] == 0:
            row = True
            break
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j] == 0:
               matrix[0][j] = 0
               matrix[i][0]=0
    for i in range(1,n):
        for j in range(1,m):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0
    if flag:
        for i in range(n):
            matrix[i][0] = 0
        for i in range(m):
            matrix[0][i]=0
    else:
        if column:
            for i in range(n):
               matrix[i][0]=0
        if row:
            for i in range(m):
                matrix[0][i]=0
    return matrix
  
# Driver Code
if __name__ == '__main__':
    m = [[1,0,3,4],[5,1,7,8],[1,10,11,12],[13,14,15,1]]
    n = [[0,0,0,0],[5,0,7,8],[1,0,11,12],[13,0,15,1]]

    print(m[2][0])
    T = set_zeros(m)
    print(T)
