# input() is used to input the values from the key board.
# int() converts the string into number or integer
# float() converts the string into number or float
# str() converts int or float into string

age=input("Enter your age here: ")
print(age)

if int(age)> 13:
    print(" you are Eligible for the programming!!")
else:
    print("Sorry You are not eligbile for programming!!!")

value=input("Enter the weight of person: ")
print(value)

float_weight_value= float(value)
print(float_weight_value)

float_to_string=str(float_weight_value)
int_to_string=str(age)

print(float_to_string)
print(int_to_string)