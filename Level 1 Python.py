#Level 1: Simple loops (counting, totals)

#Sum from 1 to n

#Input: n

#Output: 1 + 2 + ... + n
def SumFrom1ToN(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total    
print(SumFrom1ToN(10))
print(SumFrom1ToN(31))


#Count vowels

#Input: string s

#Output: number of vowels in s
def CountVowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count
print(CountVowels("Hello World"))
print(CountVowels("Python Programming"))
print(CountVowels("Factorial"))
#Factorial

#Input: n

#Output: n! (e.g. 5 → 120)
def Factorial(n):
    result = 1
    p = range(2, n + 1)
    print('series p = ' + str(list(p)))
    for i in range(2, n + 1):
        result *= i
    return result


print('Factorial of 5 = ' + str(Factorial(5)))
print('Factorial of -10 = ' + str(Factorial(-10)))

def FactorialByRecursion(n):
    if n < 0:
        return "Undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * FactorialByRecursion(n - 1)
p = range(1, 11)
print('series p = ' + str(list(p)))

for i in range(1, 11):
    print('Factorial of ' + str(i) + ' by recursion = ' + str(FactorialByRecursion(i)))
print('Factorial of 5 by recursion = ' + str(FactorialByRecursion(5)))
#Multiplication table

#Input: n

#Output: print n * 1 through n * 10
def MultiplicationTable(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

print('Multiplication Table of 66')
MultiplicationTable(66)  