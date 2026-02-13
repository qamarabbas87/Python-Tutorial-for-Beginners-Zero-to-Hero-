###Level 0: Warm-up (no loops or very light loops)

#Sum of two numbers

#Input: a, b

#Output: a + b

def Sum(a, b):
    return a + b

print(Sum(291876576, 391621899))

#Even or odd

#Input: integer n

#Output: "even" or "odd"
def CheckEvenorOdd(input):
    if input % 2 == 0:
        return "even"
    else:
        return "odd"    

print(CheckEvenorOdd(2))
print(CheckEvenorOdd(3))
#Absolute value (without using abs)

#Input: integer n
print('ABSOLUTE VALUE FUNCTION')
#Output: absolute value
def AbsoluteValue(n):
    if n < 0:
        return -n
    else:
        return n    
print(AbsoluteValue(-5))
print(AbsoluteValue(5))
#Largest of three

#Input: a, b, c

#Output: largest number###

def LargestOfThree(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print(LargestOfThree(6545,453453,43543543544))
print(LargestOfThree(4545345, 435345, 43534435))
print(LargestOfThree(9999, 76987897, 0o7777))