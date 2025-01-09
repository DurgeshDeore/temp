# Future Marks Prediction Project
# Linear Regression without AI/ML Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as linear_regression
# Sample data: Study hours, past semester marks, and remarks (1 for good, 0 for bad)
study_hours = [1,2, 3, 4, 5, 6,7,8,9,10]
past_marks = [50, 60, 65, 70, 75]
past_semester_marks = [55, 62, 67, 72, 78]
remarks = [1, 1, 0, 1, 1]  # 1 for good, 0 for bad

# Function to calculate the slope (m) and intercept (c) of the regression line
def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x2 = sum([x[i] ** 2 for i in range(n)])

    # Calculate slope (m)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)

    # Calculate intercept (c)
    c = (sum_y - m * sum_x) / n

    return m, c

# Function to predict future marks based on study hours, past semester marks, and remarks
def predict(m1, c1, m2, c2, m3, c3, hours, semester_marks, remark):
    predicted_marks_hours = m1 * hours + c1
    predicted_marks_semester = m2 * semester_marks + c2
    predicted_marks_remark = m3 * remark + c3
    
    # Average the predictions from the three factors
    final_prediction = (predicted_marks_hours + predicted_marks_semester + predicted_marks_remark) / 3
    return final_prediction

# Calculate slope and intercept for each factor
m1, c1 = linear_regression(study_hours, past_marks)
m2, c2 = linear_regression(past_semester_marks, past_marks)
m3, c3 = linear_regression(remarks, past_marks)

# Take user inputs for study hours, past semester marks, and remark
name= input("Enter Your Name:")
hours = float(input("Enter the number of study Hours: "))
semester_marks = float(input("Enter the past semester marks: "))
remark = int(input("Enter the remark (1 for good, 0 for bad): "))

# Predict future marks
predicted_marks = predict(m1, c1, m2, c2, m3, c3, hours, semester_marks, remark)

print(f"Predicted marks: {predicted_marks:.2f}")