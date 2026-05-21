file = open("employee.txt", "w")

file.write("101 Tilak Gupta 20000\n")
file.write("102 Yash Gupta 30000\n")
file.write("103 Shikha Gupta 40000\n")

file.close()
print("\n Employees added successfully")

file = open("employee.txt", "r")
data = file.read()

print("------Employee File Details------")
print(data)
file.close()

file = open("employee.txt", "r")
content = file.read()

characters = len(content)

words = len(content.split())

lines = content.splitlines()

print("----- File Statistics -----")
print("Number of Lines      :", lines)
print("Number of Words      :", words)
print("Number of Characters :", characters)

file.close()
