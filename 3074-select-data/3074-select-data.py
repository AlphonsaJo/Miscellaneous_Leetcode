import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame where student_id is 101
    result = students[students['student_id'] == 101][['name', 'age']]
    return result