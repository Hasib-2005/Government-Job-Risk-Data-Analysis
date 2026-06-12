import pandas as pd
import numpy as np

random_strings_array = np.random.choice(["a", "b", "c"], 10**6)
df = pd.DataFrame(
    {
        "column_1": np.random.choice(["a", "b", "c"], 10**6),
        "column_2": np.random.choice(["a", "b", "c"], 10**6),
        "column_3": np.random.choice(["a", "b", "c"], 10**6),
    }
)

print(df.duplicated().sum())