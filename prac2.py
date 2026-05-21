num = int(input("Enter a number: "))

if num > 1:
    is_prime = True

    for i in range(2, num):
        if num % i ==0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
else:
    print(f"{num} is not a prime number")


print("\n---- Prime numbers between 1 and 100 ----")
for n in range(2, 101):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False


    if prime:
        print(n, end=" ")



