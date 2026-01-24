from typing import Tuple
import pandas as pd

def table_stats_from_csv(path: str) -> Tuple[float, float, float]:
    df = pd.read_csv(path)

    mean_salary = df["salary"].mean()
    min_salary = df["salary"].min()
    max_salary = df["salary"].max()

    return mean_salary, min_salary, max_salary


print(table_stats_from_csv("data.csv"))

