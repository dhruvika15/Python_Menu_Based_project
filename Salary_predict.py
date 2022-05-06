import joblib
model= joblib.load('salary_model.pk1')
print('Enter your Years of Experience', ' ')
exp= float(input())
p= model.predict([[exp]])
print("Your Salary is: ",p)
