import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    answer= animals[animals['weight']>100].sort_values(['weight'],ascending=False)[['name']]
    return answer