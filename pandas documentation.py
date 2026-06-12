import pandas as pd
import numpy as np
from Demos.FileSecurityTest import permissions_dir_inherit

dates = pd.date_range("20130101", periods=6)
# # print(dates)
#
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(5)), dtype="float32"),
        "D": np.array([3] * 5, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train", "test"]),
        "F": "foo",
    }
)
# print(df2)
df2.index = dates[:5]

df1 = df2.reindex(index=dates[0:4], columns=list(df2.columns) + ["G"])

df1.loc[dates[0] : dates[1], "G"] = 1

df1.dropna(how="all", inplace=True)
print(df1)

# Calculate the mean value for each column:
#
# df.mean()

# Calculate the mean value for each row:
#
# df.mean(axis=1)


# 1. 10 Minutes to Pandas
# 2. Indexing (loc, iloc)
# 3. Missing Data
# 4. GroupBy
# 5. Merge / Join
# 6. Pivot Table
# 7. Matplotlib
# 8. Seaborn
# 9. Correlation
# 10. EDA Project