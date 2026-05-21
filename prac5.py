# ==================================================
# EMPLOYEE MANAGEMENT USING DICTIONARY
# ==================================================

# Employee Dictionary
employees = {
    101: {"name": "Rahul", "salary": 45000},
    102: {"name": "Anita", "salary": 60000},
    103: {"name": "Vikas", "salary": 75000}
}

# Display all employees
print("----- Employee Details -----")

for emp_id, details in employees.items():
    print(f"ID: {emp_id}")
    print(f"Name: {details['name']}")
    print(f"Salary: {details['salary']}")
    print()


# ==================================================
# ADD EMPLOYEE
# ==================================================

employees[104] = {
    "name": "Sneha",
    "salary": 55000
}

print("Employee Added Successfully\n")


# ==================================================
# UPDATE EMPLOYEE
# ==================================================

employees[101]["salary"] = 50000

print("Employee Salary Updated Successfully\n")


# ==================================================
# REMOVE EMPLOYEE
# ==================================================

del employees[103]

print("Employee Removed Successfully\n")


# ==================================================
# DISPLAY UPDATED EMPLOYEES
# ==================================================

print("----- Updated Employee Details -----")

for emp_id, details in employees.items():
    print(f"ID: {emp_id}")
    print(f"Name: {details['name']}")
    print(f"Salary: {details['salary']}")
    print()


# ==================================================
# EMPLOYEES WITH SALARY > 50000
# ==================================================

print("----- Employees with Salary Greater Than 50000 -----")

for emp_id, details in employees.items():

    if details["salary"] > 50000:
        print(f"{details['name']} --> {details['salary']}")



# ==================================================
# TUPLE PACKING AND UNPACKING
# ==================================================

print("\n----- Tuple Packing and Unpacking -----")

# Tuple Packing
employee_tuple = ("Amit", 105, 70000)

print("Packed Tuple:")
print(employee_tuple)

# Tuple Unpacking
name, emp_id, salary = employee_tuple

print("\nUnpacked Values:")
print("Name   :", name)
print("ID     :", emp_id)
print("Salary :", salary)



# ==================================================
# SET OPERATIONS
# ==================================================

print("\n----- Set Operations -----")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1 :", set1)
print("Set 2 :", set2)

# Union
print("\nUnion:")
print(set1.union(set2))

# Intersection
print("\nIntersection:")
print(set1.intersection(set2))

# Difference
print("\nDifference (Set1 - Set2):")
print(set1.difference(set2))

# Symmetric Difference
print("\nSymmetric Difference:")
print(set1.symmetric_difference(set2))