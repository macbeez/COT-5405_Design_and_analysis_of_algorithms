import random

noOfBits = 8

# 4, 8, 16, 32, 64, 128, 256, 512

# MAX_INT = 0x7FFFFFFF
# MIN_INT = 0x80000000
# MASK = 0x100000000

def add(x, y):

    # Iterate till there is no carry 
    while (y != 0):
        # carry now contains common
        # set bits of x and y
        carry = x & y

        # Exclusive OR
        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = (x ^ y) % MASK

        # Carry is shifted by one so that   
        # adding it to x gives the required sum
        y = (carry << 1) % MASK

    return x if x <= MAX_INT else ~((x % MIN_INT) ^ MAX_INT)

def subtract(x, y):
    # If subtracting a larger number from
    # a smaller number, the output is 
    # negated
    if x < y:
        x, y = y, x
        negate = True

    # Iterate till there
    # is no carry
    while (y != 0):
     
        # borrow contains common 
        # set bits of y and unset
        # bits of x
        borrow = (~x) & y
         
        # Subtraction of bits of x
        # and y where at least one
        # of the bits is not set
        x = (x ^ y) % MASK
 
        # Borrow is shifted by one 
        # so that subtracting it from 
        # x gives the required sum
        y = (borrow << 1) % MASK
    
    if not x <= MAX_INT:
        x = ~((x % MIN_INT) ^ MAX_INT)

    return x * -1 if ('negate' in vars() and negate == True) else x

def multiply(x,y):
    res = 0;
    while (y != 0):
        #print("x:", x, "y:", y, end=" ")
        if (y & 1):
            res = add(res, x); # if y is odd, add x to result
        #print("res:", res)
        x = (x << 1) % MASK
        y = (y >> 1) % MASK
    return res;

def divide(dividend, divisor): 
    
    if divisor != 0:
        # Calculate sign of divisor i.e.,
        # sign will be negative only iff
        # either one of them is negative
        # otherwise it will be positive
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
         
        # Update both divisor and
        # dividend positive
        dividend, divisor = abs(dividend), abs(divisor)
         
        # Initialize the quotient
        quotient = 0
        while (dividend >= divisor): 
            dividend = subtract(dividend, divisor) 
            quotient = add(quotient, 1) 
         
        return sign * quotient
    else:
        return "NaN"

def getRandomArray(bits, noOfNums):
    numList = []
    for i in range(noOfNums):
        numList.append(random.randrange(pow(-2, bits-1), pow(2, bits-1)))
    return numList

# Generate number array
print("Number of bits:", noOfBits)
num_array = getRandomArray(bits=noOfBits, noOfNums=2000)

MAX_INT = int(pow(2, noOfBits*2)/2)-1
MIN_INT = int(pow(2, noOfBits*2)/2)
MASK = pow(2, noOfBits*2)

# Add
print("Adding...")
for index, num in enumerate(num_array):
    if index % 2 == 0 and index < len(num_array):
        result = add(num_array[index], num_array[index + 1])
        
        # For testing purpoes only, to compare to compare function with real operator
        real = num_array[index] + num_array[index + 1]
        if result != real:
            print("Add", index, num_array[index], num_array[index + 1], result, end =" ")
            print(result == real)

# Subtract
print("Subtracting...")
for index, num in enumerate(num_array):
    if index % 2 == 0 and index < len(num_array):
        result = subtract(num_array[index], num_array[index + 1])
        
        # For testing purpoes only, to compare to compare function with real operator
        real = num_array[index] - num_array[index + 1]
        if result != real:
            print("Subtract", index, num_array[index], num_array[index + 1], result, end =" ")
            print(result == real)

# Multiply
print("Multiplying...")
for index, num in enumerate(num_array):
    if index % 2 == 0 and index < len(num_array):
        result = multiply(num_array[index], num_array[index + 1])
        
        # For testing purpoes only, to compare to compare function with real operator
        real = num_array[index] * num_array[index + 1]
        if result != real:
            print("Multiply", index, num_array[index], num_array[index + 1], result, end =" ")
            print(result == real)

# Divide
print("Dividing...")
for index, num in enumerate(num_array):
    if index % 2 == 0 and index < len(num_array):
        result = divide(num_array[index], num_array[index + 1])
        
        # For testing purpoes only, to compare to compare function with real operator
        if num_array[index + 1] != 0:
            real = int(num_array[index] / num_array[index + 1])
        else:
            real = "NaN"
        if result != real:
            print("Divide", index, num_array[index], num_array[index + 1], result, end =" ")
            print(result == real)

