import pandas as pd
import pandas as pd
from pandas.core.groupby import DataFrameGroupBy

df = pd.DataFrame({
    "name": ["sawai", "singh", "charan", "ram", "shyam"],
    "class": ["10", "11", "10", "12", "11"],
    "age": [16, 17, 16, 18, 17],
    "marks": [90, 85, 78, 95, 88],
    "sports": ["y", "n", "y", "n", "y"]
})

# print first three rows only
print("print first 3 rows only: \n", df[0:3]) # this will fetch the rows 0, 1 and 2nd  index, last number is exclusive


print("---------------------------------------------------------")
# print first three rows only
print("print first 3 rows only: \n", df[0:3]) # this will fetch the rows 0, 1 and 2nd  index, last number is exclusive


print("---------------------------------------------------------")
# print name col only
print("# print name col only: \n", df["name"])

print("---------------------------------------------------------")
# print name and marks cols
print("# print name and marks cols: \n", df[["name", "marks"]])

print("---------------------------------------------------------")
# print number of rows and cols
print("# print number of rows and cols: \n", df.shape)


print("---------------------------------------------------------")
# print all column names
print("# print all column names: \n", df.columns)


print("\n\n\n---------------------------------------------------------")
# print datatype for each column
print("# print datatype for each column: \n", df.info())


print("\n\n---------------------------------------------------------")
# print rows where age is 17
print("# print rows where age is 17: \n", df[df["age"] > 17])

print("\n\n---------------------------------------------------------")
# print rows where age is 17
print("# print rows where age is 17: \n", df.where(df["age"] > 17))


print("\n\n---------------------------------------------------------")
# print rows where age is >= 17 and marks > 80
print("# print rows where age is > 17 and marks > 80: \n", df[(df["age"] >= 17) & (df["marks"] > 80)])

print("\n\n---------------------------------------------------------")
# print rows where marks > 80 and <=95
print("# print rows where marks > 80 and <=95: \n", df[(df["marks"] >= 80) & (df["marks"] < 95)])


print("\n\n---------------------------------------------------------")
# print records where name starts with 's'
print("# print records where name starts with 's': \n", df[df["name"].str.startswith("s")])


print("\n\n---------------------------------------------------------")
# print records where name contains 'a'
print("# print records where name contains 'a': \n", df[df["name"].str.contains("a")])


print("\n\n---------------------------------------------------------")
# sorting by marks asc
print("# sorting by marks asc: \n", df.sort_values(by="marks", ascending=True))


print("\n\n---------------------------------------------------------")
# sorting by marks desc
print("# sorting by marks desc: \n", df.sort_values(by="marks", ascending=False))


print("\n\n---------------------------------------------------------")
# sorting by age then marks asc
print("# sorting by age then marks asc: \n", df.sort_values(by=["age", "marks"], ascending=True))


def get_grades(marks):
    if marks > 90:
        return "A+"
    elif marks > 80:
        return "A"
    elif marks > 60:
        return "B"
    elif marks > 45:
        return "C"
    else:
        return "F"


print("\n\n---------------------------------------------------------")
# Create a new column of the grade
df["grade"] = df["marks"].apply(get_grades)
print("# Create a new column of the grade: \n", df)


def get_bonus_marks(dataframe):
    print("dataframe==============", dataframe)
    if dataframe["sports"] == 'y':
        return dataframe["marks"] + 5
    else:
        return dataframe["marks"]


print("\n\n---------------------------------------------------------")
# add one more column and add +5 marks if person is from sports category
df["final_marks"] = df.apply(get_bonus_marks, axis=1)
print("# Create a new column of the grade: \n", df)


print("\n\n---------------------------------------------------------")
# find the min marks
print("# find the min marks: \n", df["marks"].min())


print("\n\n---------------------------------------------------------")
# find the max marks
print("# find the max marks: \n", df["marks"].max())

print("\n\n---------------------------------------------------------")
# find the avg marks
print("# find the avg marks: \n", df["marks"].mean())


print("\n\n---------------------------------------------------------")
# find the number of students for each class, here value is again a DataFrame
data_frame_group_by: DataFrameGroupBy = df.groupby("class")
for key, value in data_frame_group_by:
    print("key:", key, ", value:", value.size)


