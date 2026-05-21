import pandas as pd

data = {
    "name" : ["Tilak", "Yogesh", "Yash", "Shikha"],
    "roll_no" : [101, 102, 103 ,104],
    "marks" : [98, 40, 50, 60]
}

df = pd.DataFrame(data)
print(df)

print("------------------------")
filtered_students = df[df["marks"]>75]
print(filtered_students)

print("------------------------")
sorted_students = df.sort_values(by="marks", ascending=False)
print(sorted_students)


