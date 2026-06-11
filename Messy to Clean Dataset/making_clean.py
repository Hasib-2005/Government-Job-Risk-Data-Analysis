import pandas as pd

df = pd.read_csv("Garment_Job_Risk.csv")

df.fillna(df.mean(numeric_only=True), inplace=True)
# print(df.isnull().sum())

# String/Object columns
cat_cols = cat_cols = df.select_dtypes(include=["str", "object"]).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# print(df.isnull().sum())
# print("Duplicates:", df.duplicated().sum())
# print(df.describe())

# print(df[df["Working_Hours_Per_Week"] > 60])

# print(df[df["Experience_Years"] > 20])

# print(df["Job_Role"].unique())
# print(df["Shift_Type"].unique())
# print(df["Job_Risk"].unique())

# df.loc[df["Working_Hours_Per_Week"] > 60, "Working_Hours_Per_Week"] = 56
# print(df["Working_Hours_Per_Week"].describe())
# print(df["Experience_Years"].describe())
#
# print("********  After cleaning Null counts  **********")
# print(df.isnull().sum())

print(df.shape)