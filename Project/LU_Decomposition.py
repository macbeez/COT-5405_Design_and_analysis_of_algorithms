"""import random
import numpy as np
#generating random 3 x 3 matrix elements

matrix = np.random.random_integers(0,999, (3,3)) 

print(matrix) """

import random
import numpy as np
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

matrix = scipy.array([ [47,60,33], [82,36,6], [15,40,26]])

# matrix = np.random.random_integers(0,999, (3,3)) 
P, L, U = scipy.linalg.lu(matrix)

print ("A:")
pprint.pprint(matrix)

print ("P:")
pprint.pprint(P)

print ("L:")
pprint.pprint(L)

print ("U:")
pprint.pprint(U)
	