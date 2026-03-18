#L01-T5
print("This program calculates the average of the 3 numbers you enter.")
print("The numbers can be int's or float's.")
num1 = float(input("Enter the first number:\n"))
num2 = float(input("Enter the second number:\n"))
num3 = float(input("Enter the third number:\n"))
sum1 = num1+num2+num3
print("Sum of the numbers:", sum1)
ave1 = sum1/3
ave2 = int(ave1)
print("Average of the numbers (rounded to 3 decimal places):", round(ave1, 3))
print("Average of the numbers (rounded to the closest integer):", round(ave1))
print("Average of the numbers as an integer without the decimal part:",(ave2)) 

             
