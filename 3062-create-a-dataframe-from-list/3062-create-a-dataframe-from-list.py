import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Create DataFrame
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# Input data
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

# Call the function and print the DataFrame
df = createDataframe(student_data)
print(df)
