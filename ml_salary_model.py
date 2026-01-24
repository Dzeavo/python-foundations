import pandas as pd
from sklearn.linear_model import LinearRegression

# загружаем данные
df = pd.read_csv("data.csv")

# X — признак (возраст)
X = df[["age"]]

# y — то, что предсказываем (зарплата)
y = df["salary"]

# создаём модель
model = LinearRegression()

# обучаем модель
model.fit(X, y)

# делаем предсказание
predicted_salary = model.predict([[30]])

print("Predicted salary for age 30:", predicted_salary[0])

