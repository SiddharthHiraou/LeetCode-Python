import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df=employees
    return df.head(3)