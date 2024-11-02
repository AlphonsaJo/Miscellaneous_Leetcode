import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:

    pivoted_df = weather.pivot_table(index='month', columns='city', values='temperature', aggfunc = 'max')
  
    
    return pivoted_df
