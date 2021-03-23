##################################################################################################################
# FINAL TEST - COMPLETE PIVOT LU DECOMPOSITION

# DESCRIPTION: This source code generates Complete Pivot LU Decomposition on 10 randomly generated matrices of 
# size n x n. The formula used to perform the decomposition is PAQ = LU, where P and Q are permutation matrices,
# A is the randomly generated square matrix of size n x n, L is the Lower Triangular matrix and U is the Upper
# Triangular matrix. The output is a text file, with P, A, Q, L, U, Product 1 (P * A * Q) and Product 2 (L * U).
# It is noted that Product 1 and Product 2 are same for all the 10 iterations. Benchmarks such as time taken to 
# execute the code and maximum memory used are also outputted.

##################################################################################################################

import random
import numpy as np
import fractions
import time
import sys 

A = []
L = []
U = []
P = []
Q = []
P_list = []
Q_list = []
A_list = []
U_list = []

n = []
duration = [] # Holds the time taken for each iteration
memory = []

#Empty the file, each time you start execution
def clear_data_file(fileName):
    file = open(fileName, 'w')
    file.close()

def generate(mat_size):
    global A, L, U, P, Q
    A = []
    L = []
    U = []
    rows = mat_size
    cols = mat_size
    A = np.matrix(np.random.randint(1,pow(mat_size,2), size=(rows, cols)))
    # A = np.matrix([[2,3,4,10], [4,7,5,15], [4,9,5,17], [6,2,8,12]])
    # A = np.matrix([[2,3,4], [4,7,5], [4,9,5]])
    L = np.asmatrix(np.identity(mat_size))
    U = np.asmatrix(np.zeros(shape=(rows,cols)))
    P = np.asmatrix(np.identity(mat_size))
    Q = np.asmatrix(np.identity(mat_size))

def find_max_value(A):
    i,j = np.where(A == (sorted(A.flatten().tolist()[0])[-1]))
    return [i[0], j[0]]

def swap_rows(r1, r2):
    global P
    P = np.asmatrix(np.identity(mat_size))
    P_temp = P
    P_temp[[r1, r2]] = P_temp[[r2, r1]]
    return P_temp

def swap_cols(c1, c2):
    global Q
    Q = np.asmatrix(np.identity(mat_size))
    Q_temp = Q
    Q_temp[:,[c1,c2]] = Q_temp[:,[c2,c1]]
    return Q_temp

def rowEchelon(A, col):
    global L, U
    # print("In function")
    for i in range(col, len(A[:,1])-1):
        # print("coeff: -1 *", A[1+i,col], "/", A[col,col])
        coeff = (-1 * A[1+i,col]) / A[col,col]
        # print(coeff)
        L[i+1, col] = -1 * coeff
        for j in range(col, len(A[:,1])):
            U[i+1,j] = (A[col,j] * (coeff)) + A[i+1,j]
    return U

def getCurrentMemUsage():
    memory_sum = 0
    for object in globals():
        # if object != "n" or object != "duration" or object != "memory":
        memory_sum += sys.getsizeof(object)
    for object in locals():
        # if object != "n" or object != "duration" or object != "memory":
        memory_sum += sys.getsizeof(object)
    return memory_sum

for mat_size in range(2, 101):
    A = []
    L = []
    U = []
    P = []
    Q = []
    P_list = []
    Q_list = []
    A_list = []
    U_list = []
    start_time = time.time()
    # mat_size = n
    np.set_printoptions(formatter={'all':lambda L: str(fractions.Fraction(L).limit_denominator())})
    generate(mat_size)

    print("A:\n", A)
    print("L:\n", L)
    print("U:\n", U)
    print()


    for i in range(0, mat_size-1):

        if len(A_list) == 0:
            A_subset = A[i:mat_size, i:mat_size]
        else:
            A_subset = U[i:mat_size, i:mat_size]

        max_r, max_c = find_max_value(A_subset)
        
        # Manipulate P and Q matrix
        P_list.append(swap_rows(i, max_r+i))
        Q_list.append(swap_cols(i, max_c+i))

        # Swap L matrix to keep track of row manipulations
        if i > 0:
            r1 = i
            c1 = i-1
            r2 = max_r+i
            c2 = i-1
            if i == 1: 
                L[r1, c1], L[r2, c2] = L[r2, c2], L[r1, c1]
            elif i >1:
                for c in range(c1+1):
                    L[r1, c], L[r2, c] = L[r2, c], L[r1, c]

        # Compute PAQ
        if i == 0:
            A_list.append(np.matmul(P_list[-1], A))
            A_list[-1] = np.matmul(A_list[-1], Q_list[-1])
        else:
            A_list.append(np.matmul(P_list[-1], U))
            A_list[-1] = np.matmul(A_list[-1], Q_list[-1])

        # Compute new U
        U = rowEchelon(A_list[-1], col=i)
        U[:i+1] = A_list[-1][:i+1]




    for i, p in reversed(list(enumerate(P_list))):
        if i == len(P_list)-1:
            temp = p
        else:
            temp = temp.dot(p)

    P_final = temp
    print("P_final:\n", P_final)

    for i, q in enumerate(Q_list):
        if i == 0:
            temp = q
        else:
            temp = temp.dot(q)

    Q_final = temp
    print("Q_final:\n", Q_final)
    print()

    PAQ = P_final.dot(A).dot(Q_final)
    LU = L.dot(U)

    print("PAQ:\n", PAQ)
    print()
    print("LU:\n", LU)

    stop_time = time.time()
    n.append(mat_size)
    duration.append(stop_time - start_time)
    memory.append(getCurrentMemUsage())

    isResultValid = True
    for i in range(mat_size):
        for j in range(mat_size):
            if round(PAQ[i,j],6) != round(LU[i,j], 6):
                isResultValid = False

    print("\nValid Result for " + str(mat_size) + "x" + str(mat_size) + " matrix?", isResultValid)
    print("\n\n")
