import time

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
bmi_rounded = round(bmi, 2)
print(f"Your BMI is: {bmi_rounded}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.") 
time.sleep(1)
print("Thank you for using the BMI Calculator! Have a great day!")
print("Welcome to Day 4 -- Simple BMI Calculator")