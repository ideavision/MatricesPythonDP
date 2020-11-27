

def mtrx_order(p):
    n = len(p) - 1

    m = [[0 for x in range(0, n)] for y in range(0, n)]
    s = [[0 for x in range(0, n)] for y in range(0, n)]

    for i in range(0,n):
        m[i][i] = 0

    # compute smallest matrix costs first
    # for chains of length 2 to n
    for l in range(2, n+1):
        for i in range(0, n - l + 1):
            j = i + l - 1 # j is the endpoint of the chain
            if i < j: # skip the i > j cases since we must multiply in order
                # cost values
                c = [m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1] for k in range(i, j)]

                # get minimum index and value from costs
                (s[i][j], m[i][j]) = min(enumerate(c), key=lambda x: x[1])
                print( i, j, [x for x in enumerate(c)])
                s[i][j] = s[i][j] + i + 1 # correct our s value (count from 1, offset by i because of enumerate)

    return m,s

def pnt_optimize_par_solution(s, i, j):
# Sample matrices that read from files xmat, ymat, zmat
    # x = [[11,3],[7,11]]
    # y = [[8,0,1],[0,3,5]]
    # z = [[1],[3],[2]]
    
    if i == j:
        print('M' + str(i+1),end = " ") 
    else:
        print('(',end = ' ')
        pnt_optimize_par_solution(s, i, s[i][j]-1)
        pnt_optimize_par_solution(s, s[i][j], j)
        print(')',end = ' ')

# Read Matrices from txt file
with open('xmat.txt', 'r') as fx:
    x = [[int(num) for num in line.split(',')] for line in fx]
with open('ymat.txt', 'r') as fy:
    y = [[int(num) for num in line.split(',')] for line in fy]
with open('zmat.txt', 'r') as fz:
    z = [[int(num) for num in line.split(',')] for line in fz]

# Generate array from matrices 
arr = [len(x),len(x[0]),len(y[0]),len(z[0])]

# Array that chain multiplication from M(2x2) M(2x3) M(3x1) 
print('Array that chain multiplication from matrices : M(2x2) M(2x3) M(3x1) --> ',arr)
m, s = mtrx_order(arr)

#Matrices Product Results
def calc():
    R = [[sum(a*b for a,b in zip(Y_row,Z_col)) for Z_col in zip(*z)] for Y_row in y]
    Rf = [[sum(a*b for a,b in zip(X_row,R_col)) for R_col in zip(*R)] for X_row in x]
    print(' <-- Optimized Matrices Product Result\n')
    print('M1 : ',x)
    print('M2 : ',y)
    print('M3 : ',z)
    print('\nM2.M3 --> ',R)
    print('Final Result --> M1.(M2.M3) -->',Rf)

# Print Optimized parentes solution 
pnt_optimize_par_solution(s, 0, 2)
calc()