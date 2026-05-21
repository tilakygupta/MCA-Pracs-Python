import pandas as pd


# ==================================================
# CREATE DATAFRAME
# ==================================================

data = {
    "Name": ["Rahul", "Anita", "Vikas", "Sneha", "Amit"],
    "Roll No": [101, 102, 103, 104, 105],
    "Marks": [85, 72, 90, 67, 78]
}

df = pd.DataFrame(data)

print("----- Student DataFrame -----")
print(df)

print("--------------------------------")
filtered_students = df[df["Marks"]>75]
print(filtered_students)

sorted_df = df.sort_values(by="Marks", ascending=False)

print("\n----- Sorted DataFrame (Descending Marks) -----")
print(sorted_df)

mean_marks = df["Marks"].mean()
max_marks = df["Marks"].max()
min_marks = df["Marks"].min()

print("\n----- Statistical Analysis -----")
print("Average Marks :", mean_marks)
print("Maximum Marks :", max_marks)
print("Minimum Marks :", min_marks)

df.to_csv("students.csv", index=False)

print("\nDataFrame exported to students.csv successfully.")