print("This is a temperature converter")
print("It converts Celsius to Fahrenheit and the opposite")

temp_unit = input("What temperature unit do you want to convert? \nType 1 for Celsius, 2 for Fahrenheit, or 3 for Kelvin: ")
temp_unit = float(temp_unit)

temp_convert = input("What should it be converted to? \nType 1 for Celsius, 2 for Fahrenheit, or 3 for Kelvin: ")
temp_convert = float(temp_convert)

degree = input("And how many degrees do you want to convert? ")
degree = float(degree)

if temp_unit == 1:
    if temp_convert == 2:
        degree_outcome = (degree * 9/5 + 32)
        print(f"The result is {degree_outcome} Fahrenheit")
    elif temp_convert == 3:
        degree_outcome = (degree + 273.15)
        print(f"The result is {degree_outcome} Kelvin")
    else:
        print("The convert unit is not correct or does not exist")

elif temp_unit == 2:
    if temp_convert == 1:
        degree_outcome = ((degree - 32) * 5/9)
        print(f"The result is {degree_outcome} Celsius")
    elif temp_convert == 3:
        degree_outcome = ((degree - 32) * 5/9 + 273.15)
        print(f"The result is {degree_outcome} Kelvin")
    else:
        print("The convert unit is not correct or does not exist")

elif temp_unit == 3:
    if temp_convert == 1:
        degree_outcome = (degree - 273.15)
        print(f"The result is {degree_outcome} Celsius")
    elif temp_convert == 2:
        degree_outcome = ((degree - 273.15) * 9/5 + 32)
        print(f"The result is {degree_outcome} Fahrenheit")
    else:
        print("The convert unit is not correct or does not exist")

else:
    print("This unit is not supported")

