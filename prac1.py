# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# percentage = float(input("Enter your percentage: "))
#
# print("\n ----- Student Details ----")
# print(f"Name:", name)
# print(f"Age:", age)
# print(f"Percentage: {percentage:.2f}%")

a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))

print("\n ----- Arithmetic Operations ----")
print(f"Sum: {a+b}")
print(f"Difference: {a-b}")
print(f"Product: {a*b}")

if b != 0:
    print(f"Division: {a/b:.3f}")
else:
    print(f"Division: Cannot be done by Zero")