# import pandas as pd

# # Example DataFrame
# data = {
#     'Name': ['Aadil', 'Joan', 'Karan'],
#     'Age': [21, 22, 20],
#     'Score': [85.5, 90.0, 88.5],
#     'Passed': [True, True, False]
# }

# df = pd.DataFrame(data)

# # Check data types of each column
# print(df.dtypes)

import pandas as pd
import numpy as np

# Example DataFrame with missing values
data = {
    'Age': [20, 25, np.nan, 30, np.nan, 22]
}
df = pd.DataFrame(data)

# Fill missing values with the mean of the column
df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)
