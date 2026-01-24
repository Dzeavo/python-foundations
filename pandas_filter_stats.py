from typing import Tuple
import pandas as pd

def table_stats_filtered(path: str) -> Tuple[float, float, float]:
    df = pd.read_csv(path)

    
    filtered_df = df[df["age"] > 30]

    mean_salary = filtered_df["salary"].mean()
    min_salary = filtered_df["salary"].min()
    max_salary = filtered_df["salary"].max()

    return mean_salary, min_salary, max_salary


print(table_stats_filtered("data.csv"))

