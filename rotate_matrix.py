

def rotate_in_place(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        t = transpose(matrix)
        r = reflect(t)
        return r 
    
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix        

def reflect(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
    return matrix        

def rotate_anticlock_matrix(m):
    print(m)
    a = []
    for i in range(len(m)-1,-1,-1):
        print(m[i])
        d = []
        for j in range(len(m[i])):
            d.append(m[j][i])
        a.append(d)    
    return a 
        
def transpose_matrix(m):
    b = []
    for i in range(len(m)):
        c = []
        for j in range(len(m[i])):
            c.append(m[j][i])
        b.append(c)
    return b   
            

    
# Driver Code
if __name__ == '__main__':
    m = [[1,2,3], [4,5,6], [7,8,9]]
    T = transpose_matrix(m)
    R = rotate_in_place(m)
    print(R)
