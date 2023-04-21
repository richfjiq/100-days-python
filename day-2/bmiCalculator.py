# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_as_int = float(weight)
height_as_int = float(height)

bmi = weight_as_int / (height_as_int * height_as_int)

bmi_as_int = int(bmi)

print(bmi_as_int)