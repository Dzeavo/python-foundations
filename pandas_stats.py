from typing import Tuple
import pandas as pd

def table_stats(df: pd.DataFrame) -> Tuple[float, float, float]:
    mean_salary = df["salary"].mean()
    min_salary = df["salary"].min()
    max_salary = df["salary"].max()

    return mean_salary, min_salary, max_salary


data = {
    "age": [25, 30, 40, 22],
    "salary": [50000, 70000, 90000, 45000]
}

df = pd.DataFrame(data)
print(table_stats(df))

