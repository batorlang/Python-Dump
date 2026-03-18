#L02-First Task
name1 = str(input("Enter your name:\n"))
number1 = int(input("Enter an integer:\n"))
number2 = float(input("Enter a float:\n"))
number3 = round(number2 ** number1, 2)
print("Decimal", number2 ,"to power", number1 ,"is", number3)
print("Thank you for using the program,", name1,"!")
#L02-Second Task
lastname = str(input("Please enter your lastname:\n"))
firstname = str(input("Please enter your firstname:\n"))
print("Hi",firstname, lastname,", your email adress is: "+firstname+"."+lastname+"@lut.fi")
#L02-Third Task
longword = str(input("Enter a long word:"))
longword_lenght = len(longword)
print("The first five letters are:", longword[0:5])
print("The last five letters are:", longword[longword_lenght - 5:])
print("Letters 2, 3, 4 and 5 are:", longword[1:5])
print("Every second letter of the word:", longword[1::2])
print("The word backwards: `"+longword[::-1]+"`")
start_index = int(input("Enter start index:"))
end_index = int(input("Enter end index:"))
step = int(input("Enter step:"))
print("With these values `",longword,"` produces this:",longword [start_index: end_index: step])
print("Your word is", longword_lenght, "characters long")
###L02-Fourth Task
number4 = int(input("Enter a positive integer: "))
print("Number", number4,"multiplied by itself is", number4 * number4)
PII = 3.14
radius = int(input("Give the radius of a circle as an integer: "))
print("The radius of the circle is", radius,", the circumferrence is", 2*radius*PII," and the area is", (radius**2)*PII)
side1 = int(input("Enter the lenght of one side of the rectangle as an integer: "))
side2 = int(input("Enter the length of another side of the rectangle as an integer: "))
print("The sides of the rectangle are", side1," and", side2,"; perimeter is", (side1+side2)*2,"; and the area is", side1*si
