
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    "Name": ["Raju", "RAmpal", "Candan", "Dhoni", "Karan"],
    "Study_Hours": [2, 3, 5, 1, 4],
    "Marks": [40, 50, 80, 20, 65]
}

df = pd.DataFrame(data)

X = df["Study_Hours"].values.reshape(-1, 1)  
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

def predict_hours(student_name, current_hours, goal):

    current_marks = model.predict(np.array([[current_hours]]))[0]
    if goal <= current_marks:
        return f"{student_name} has already achieved the goal! 🎉"

    required_hours = (goal - model.intercept_) / model.coef_[0]
    required_hours = max(0, required_hours) 
    additional_hours = required_hours - current_hours
    return (
        f"{student_name} needs to study approximately {additional_hours:.2f} more hours "
        f"to achieve the goal of {goal} marks."
    )

student_name = input("Enter the student's name: ")
current_hours = float(input("Enter current study hours per day: "))
goal = float(input("Enter the goal marks to achieve: "))

print(predict_hours(student_name, current_hours, goal))
