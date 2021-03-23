import timeit
import random

def main():

    NumberOfInputs = int(input("Enter the number of inputs you want to test: "))
    bits = int(input("Enter the number of bits the input should have: "))

    # To ensure that there is no overflow of elements
    MAX_INT = int(pow(2, bits*2)/2)-1
    MIN_INT = int(pow(2, bits*2)/2)
    MASK = pow(2, bits*2) # cut off elements after this value to avoid overflow. 
    print(MAX_INT, MIN_INT, MASK)
    
    def generateNumbers(bits, NumberOfInputs):
        numList = []
        for i in range(NumberOfInputs):
            #generate random number based on user input
            numList.append(random.randrange(pow(-2, bits-1), pow(2, bits-1))) #generate signed integer
        return numList

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

    def multiply(x,y):
        res = 0;
        while (y != 0):
            if (y & 1):
                res = add(res, x) # if y is odd, add x to result
            x = (x << 1) % MASK
            y = (y >> 1) % MASK
        return res;

    numList = generateNumbers(bits, NumberOfInputs)
    for index, num in enumerate(numList):
        if index % 2 == 0 and index < len(numList):
            x, y = numList[index], numList[index + 1]
            answer = multiply(x,y)
            print("The multiplication of " + str(x) + " and " + str(y) + " is : " + str(answer))
        #Answer check:
            if answer != (x*y):
                print("FALSE!!!")

main()