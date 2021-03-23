

def add(x, y):
 
    # Iterate till there is no carry 
    while (y != 0):
        # carry now contains common
        # set bits of x and y
        carry = x & y
 
        # Exclusive OR
        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y

        # Carry is shifted by one so that   
        # adding it to x gives the required sum
        y = carry << 1

    return x

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
        x = x ^ y
 
        # Borrow is shifted by one 
        # so that subtracting it from 
        # x gives the required sum
        y = borrow << 1
     
    if 'negate' in vars() and negate == True:
        negate = False
        return x * -1
    else:
        return x

def multiply1(x,y):
    res = 0;
    while (y != 0):
        print("x:", x, "y:", y, end=" ")
        if (y & 1):
            res = add(res, x); # if y is odd, add x to result
        print("res:", res)
        x <<= 1;
        y >>= 1;
    return res;

def multiply2(x, y):
    result = 0
    for i in range(y):
        result = add(x, result)
    return result

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
    return "NaN"

print(add(27, 89))
print(subtract(-100, 89))
print(subtract(27, 89))
print(multiply1(2,10))
print(multiply2(2,10))
print(divide(32, 4))
print(divide(4, 0))
print(divide(-32, 4))
print(divide(3, 20))