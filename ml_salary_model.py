import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv("data.csv")


X = df[["age"]]


y = df["salary"]


model = LinearRegression()


model.fit(X, y)


predicted_salary = model.predict([[30]])

print("Predicted salary for age 30:", predicted_salary[0])

