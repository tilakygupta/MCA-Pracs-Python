#recursive factorial
def fact_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * fact_recursive(n-1)

def fact_iterative(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

#recursive fibonacci
def fibo_recursive(n):
    if n<=1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)

def fibo_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

number = int(input("Enter a number: "))
print("Recursive factorial: ",fact_recursive(number))
print("Iterative factorial: ",fact_iterative(number))
print("\nFibonacci Series using Recursion:")
for i in range(number):
    print(fibo_recursive(i), end=" ")


print("\n\nFibonacci Series using Iteration:")
fibo_iterative(number)