import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4))

# print(df)

pieces = [df[:3], df[3:7], df[7:]]

# print(pieces)

result = pd.concat(pieces)
print(result)