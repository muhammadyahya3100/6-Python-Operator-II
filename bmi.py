Weight = float(input("Enter your weuight in KG: "))
height = float(input("Enter your height in meters: "))
bmi = Weight / (height ** 2)
print ("Your BMI is : ", bmi)
if bmi < 18.5:
    print("YOU ARE UNDER WEIGHT")
elif 18.5 <= bmi < 24.9:
    print("YOU HAVE A NORMAL WEIGHT")
elif 25 <= bmi < 29.9:
    print ("YOUR ARE OVER WEIGHT")
elif bmi > 30.1:
    print("YOU ARE OBESE")