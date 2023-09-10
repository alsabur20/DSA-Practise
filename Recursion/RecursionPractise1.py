#Recursion Practise

#Print the numbers from 1 to 10 using recursion
def printNumbers(n):
    if n > 10:
        return  #Base Case
    print(n)    #Print the number
    printNumbers(n+1)   #Recursive call

#printNumbers(1)

#Print the numbers from 10 to 1 using recursion
def printNumbersReverse(n):
    if n < 1:
        return  #Base Case
    print(n)    #Print the number
    printNumbersReverse(n-1)   #Recursive call

#printNumbersReverse(10)

#calculate the sum of numbers from 1 to n using recursion

def sumNumbers(n):
    if n == 1:
        return 1    #Base Case
    return n + sumNumbers(n-1)  #Recursive call

#print(sumNumbers(10))  

#calculate factorial of a number using recursion
def factorial(n):
    if n==1:
        return 1    #Base Case
    return n * factorial(n-1)   #Recursive call

#print(factorial(5))

#print the fibonacci series using recursion
def fibonacci(a, b, n):
    if n==0:
        return
    c=a+b
    print(c)
    fibonacci(b,c,n-1)
    
# a=0
# b=1
# print(a)
# print(b)
# n=7
# fibonacci(a,b,n-2)

#print x^n (stack height is n)
def power(x,n):
    if n==0:
        return 1  #Base Case #1
    if x==0:
        return 0  #Base Case #2
    return x*power(x,n-1)  #Recursive call

# print(power(2,3))

#print x^n (stack height is logn)
def cPower(x,n):
    if n==0:
        return 1  #Base Case #1
    if x==0:
        return 0  #Base Case #2
    if n%2==0:
        return cPower(x,n//2)*cPower(x,n//2)
    else:
        return cPower(x,n//2)*cPower(x,n//2)*x
    
#print(cPower(2,4))