# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height ** 2)

if bmi < 18.5:
    final = round(bmi)
    print(f"Your BMI is {final}, you are underweight.")
elif bmi < 25:
    final = round(bmi)
    print(f"Your BMI is {final}, you have a normal weight.")
elif bmi < 30:
    final = round(bmi)
    print(f"Your BMI is {final}, you are slightly overweight.")
elif bmi < 35:
    final = round(bmi)
    print(f"Your BMI is {final}, you are obese.")
else:
    final = round(bmi)
    print(f"Your BMI is {final}, you are clinically obese.")