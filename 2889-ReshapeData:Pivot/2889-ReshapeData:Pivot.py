import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    answer= weather.pivot(index='month',columns='city',values='temperature')
    return answer