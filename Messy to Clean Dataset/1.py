import pandas as pd
from pandas.core.dtypes import dtypes

df = pd.read_csv("Garment_Job_Risk.csv")

###########   Dataset Overview   ###########
print(df.head()) # default 1st 5 rows, if we add value then 1st nth rows
print(df.tail()) # default last 5 rows, if we add value then last nth rows

print(df.sample(2)) # random rows

print(df.shape) # print (rows, column)

print(df.columns) # prints column names

print(df.dtypes) # prints datatypes of column headers

print(df.info()) # prints non null value count and datatypes of each column

print(df.to_string())
print(df.describe()) # prints count, mean, std, min, max, 25%, 50%, 75% of the numeric columns


############ Missing Value Analysis ##############
print(df.isnull()) # returns the whole dataframe with boolean values(if null value, prints true, else false)

print(df.isnull().sum()) # prints every columns total null value count

print(df.isna().sum()) # same as isnull.sum

print(df["Working_Hours_Per_Week"].mean()) # prints mean of that numeric column

print(df["Working_Hours_Per_Week"].median()) # prints median of that numeric column

print(df["Working_Hours_Per_Week"].mode()[0]) # prints mode of that numeric column ** [0] for multiple mods first value

df["Working_Hours_Per_Week"] = df["Working_Hours_Per_Week"].fillna(df["Working_Hours_Per_Week"].mean()) # fills all null values of "Working_Hours_Per_Week" column with mean value of the column

print(df["Working_Hours_Per_Week"])


############  Duplicate Handling  ############
# print(df.duplicated()) # checks duplicate rows, if multiple rows are same, only 1st row is considered as real(return false) and the others are duplicate(return true)
# print(df.duplicated().sum()) # total duplicate rows count

# df.drop_duplicates(inplace=True) # removes duplicate rows from dataframe


################# Date Cleaning ##############
# not for this dataset,,, should have date column
# df["Date"] = pd.to_datetime(df["Date"])
# df["Date"].dtype


########## Sorting ###############
# df = df.sort_values('Working_Hours_Per_Week') # sort ascending order whole dataframe based on that numeric column
# df = df.sort_values('Working_Hours_Per_Week', ascending=False) # sort descending order whole dataframe based on that numeric column

# df = df.sort_values(['Experience_Years', 'Working_Hours_Per_Week']) # # Sort by first column, if equal then by second column


################# Filtering #################
# Experience > 5 years
# print(df[df["Experience_Years"] > 5])

# Working hours > 50
# print(df[df["Working_Hours_Per_Week"] > 50])

# Task rotation frequency = 3
# print(df[df["Task_Rotation_Frequency"] == 3])

# Both conditions true
# print(df[(df["Experience_Years"] > 5) & (df["Working_Hours_Per_Week"] > 50)])

# At least one condition true
# print(df[(df["Experience_Years"] > 5) | (df["Working_Hours_Per_Week"] > 50)])

# High risk workers
# print(df[df["Job_Risk"] == "High"])


############## Statistics ###############
# print("Mean:", df["Working_Hours_Per_Week"].mean())
# print("Median:", df["Working_Hours_Per_Week"].median())
# print("Mode:", df["Working_Hours_Per_Week"].mode()[0])
# print("Max:", df["Working_Hours_Per_Week"].max())
# print("Min:", df["Working_Hours_Per_Week"].min())
# print("Std:", df["Working_Hours_Per_Week"].std())
# print("Count:", df["Working_Hours_Per_Week"].count())


#############  Grouping  ############
# Average working hours for each job role
# print(df.groupby("Job_Role")["Working_Hours_Per_Week"].mean())

# Maximum Pulse for each Job_Role group
# print(df.groupby("Job_Role")["Working_Hours_Per_Week"].max())

# Group by Job_Role and apply multiple aggregations
# print(df.groupby("Job_Role").agg({
#     "Working_Hours_Per_Week": "mean",
#     "Experience_Years": "max"
# }))


############ Create new columns ###############
# Hours worked per year of experience
# df["Hours_Per_Experience"] = df["Working_Hours_Per_Week"] / df["Experience_Years"]

# Experience × working hours
# df["Experience_Workload"] = df["Experience_Years"] * df["Working_Hours_Per_Week"]

# Injury history × working hours
# df["Injury_Risk_Score"] = df["Injury_History"] * df["Working_Hours_Per_Week"]

# print(df.to_string())

##############  Outlier Detection  ############
# Workers with more than 15 years experience
# print(df[df["Experience_Years"] > 15])

# Workers working more than 60 hours per week
# print(df[df["Working_Hours_Per_Week"] > 60])

# Workers with unusually high injury history
# print(df[df["Injury_History"] > 5])


########## Forward Fill (FFill) ############
# df["Working_Hours_Per_Week"] = df["Working_Hours_Per_Week"].ffill()

########## Backward Fill (BFill) ############
# df["Working_Hours_Per_Week"] = df["Working_Hours_Per_Week"].bfill()
print("********  Before cleaning Null counts  **********")
print(df.isnull().sum())
