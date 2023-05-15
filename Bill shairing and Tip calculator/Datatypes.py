#Data types

# 1) Strings
                    #subscripting
print("Hello"[4])       

# 2)  Integers ---> Comprises of whole numbers

print(123 + 123)
#123_456 is the same as 123456 in python programming

# 3)   Float  ---> Comprises of decimal numbers
print(1.2 + 1.2)

# 4) Bolean
#True/False
print(3>4)

#type function
num_char = len(input("what's your name"))
print(type(num_char))
# you can only concatnate values of the same data type
#data type conversion
new_num_char = str(num_char)
print(type(new_num_char))

value = input("Enter two values to add")
Sum = int(value[0]) + int(value[1])
print(Sum)

#mathematical operations BMI

weight = input("Enter your weight in kgs \n")
height = input("Enter yor height in meters \n")
BMI = float(weight)/float(height)**2 #** raises power to exponetial
print(int(BMI))

print(round(8/3,2)) #this gives 2.66666... the 2 gives no. of decimal places, that is 2.67
result = 5
result +=1 #this adds 1 to initial value of result. same can be done to other operations
print(result)

#f-string  -  helps to convent variables/values automatically to strings when adding to a sentence
#f-string is added just before the beginning of the double quaotes
result = 0     #note yhis is an integer, therefore cannot be concatinated with strings before conversion
print(f"your score is {result}") #result is converted to string by f-string

age = input("what is your current age in years \n")
years_remaining = 90 - int(age)
months_remaining = 12 * years_remaining
weeks_remaining = 52 * years_remaining
print(f"you have {years_remaining} years, {months_remaining} months, and {weeks_remaining} weeks left")

print("Hello! Welcome to Tip Calculator")
total = input("what is the total bill?\n")
tip  = input("what is the percentage tip you would like to give?\n")
splits = input("how mamy people are sharing the bill?\n")
bill_per_person = (((int(total) * int(tip)/int(100)) + int(total))/int(splits))
each_bill  = "{:.2f}".format(bill_per_person) #forces to have 2 decimal places when the last value is zero
print(f"each person should pay ${each_bill}")