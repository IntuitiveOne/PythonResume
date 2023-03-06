height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

floatweight = float(weight)                                                             #float conversion of string input for calculation         
floatheight = float(height)
bmi = (floatweight/(floatheight * floatheight))
bmirounded = "{:.0f}".format(bmi)                                                       #rounding fuction for better user experience

if bmi < 18.5:                                                                          #basic if else statement to define where bmi variable sits for appropiate output
    result = f"Your BMI is {bmirounded}, you are underweight."
elif bmi > 18.5 and bmi < 25:
        result = f"Your BMI is {bmirounded}, you have a normal weight."
elif bmi > 25 and bmi < 30:
            result = f"Your BMI is {bmirounded}, you are slightly overweight."
elif bmi > 30 and bmi < 35:
                result = f"Your BMI is {bmirounded}, you are obese."
else:
                    result = f"Your BMI is {bmirounded}, you are clinically obese."

print(result)
