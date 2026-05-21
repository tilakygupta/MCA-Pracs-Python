import matplotlib.pyplot as plt

students = ["Rahul", "Anita", "Vikas", "Sneha", "Amit"]
marks = [85, 72, 90, 67, 78]

plt.figure(figsize=(6,4))

plt.plot(students, marks, marker='o')

plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# ==================================================
# BAR CHART FOR SUBJECT-WISE PERFORMANCE
# ==================================================

subjects = ["Math", "Science", "English", "Computer", "History"]
scores = [88, 92, 76, 95, 80]

plt.figure(figsize=(6, 4))

plt.bar(subjects, scores)

plt.title("Subject-wise Performance")
plt.xlabel("Subjects")
plt.ylabel("Scores")

plt.show()


# ==================================================
# HISTOGRAM FOR AGE DISTRIBUTION
# ==================================================

ages = [18, 19, 20, 18, 21, 22, 20, 19, 18, 21,
        22, 23, 20, 19, 18, 21, 20, 22]

plt.figure(figsize=(6, 4))

plt.hist(ages, bins=5)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()