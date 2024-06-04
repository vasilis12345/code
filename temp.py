print("This is a temprature convertor")
print("It converts celcius to fahrenite and the opposite")

temp_unit = input("what temprature unit do you want to convert? \n type 1 for celsius or 2 for fahrenite")
temp_unit = float(float(temp_unit))

degree = input("and how many degrees do you want to convert?")
degree =float(float(degree))

if temp_unit == 1:
  degree_c_outcome = (degree * 9/5 + 32)
  print(f"The result is {degree_c_outcome}")

elif temp_unit == 2:
  degree_f_outcome = ((degree - 32) * 5/9)
  
else :
  print("This unit is not supported")