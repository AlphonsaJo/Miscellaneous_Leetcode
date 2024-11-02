import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # Pivot the DataFrame
    pivoted_df = weather.pivot_table(index='month', columns='city', values='temperature', aggfunc = 'max')
    
    # Resetting the index to have 'month' as a column again
  
    
    return pivoted_df
