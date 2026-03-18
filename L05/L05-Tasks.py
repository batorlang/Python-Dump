###Task one
###A
##def print_lines(str1):
##    print(str1)
##print_lines("This is printed inside the function")
###B
##def process_number(nr):
##    print("The input number is", nr)
##    print("The number squared is", nr**2)
##nr = int(input("Enter a number\n"))
##process_number(nr)
###C
##def print_whole_name(firstname, lastname):
##    print("The whole name is", firstname, lastname)
##firstname = str(input("Enter your first name:\n"))
##lastname = str(input("Enter your last name:\n"))
##print_whole_name(firstname, lastname)
#Task two
##def integer_check(num1, num2, num3):
##    if num3 != 0:
##        if num1 > num2:
##            num1 = num1 - num3
##        elif num2 > num1:
##            num2 = num2 - num3
##        elif num1 == num2:
##            num1 = num1 - num3
##    if num1 > num2:
##        print(num1, "is greater than", num2)
##    elif num2 > num1:
##        print(num2, "is greater than", num1)
##    else:
##        print("The integers are the same.")
##num1 = int(input("Enter the first integer:\n"))
##num2 = int(input("Enter the second integer:\n"))
##num3 = int(0)
##integer_check(num1, num2, num3)
##num3 = int(input("Enter the integer that is subtracted from the larger:\n"))
##integer_check(num1, num2, num3)
###Task three
##def check(str2, str3):
##    for i in range(len(str3)-len(str2)+1):
##        boolean = True
##        for j in range(len(str2)):
##            if str3[i+j] != str2[j]:
##                boolean = False
##                break
##        if boolean == True:
##            return True
##    return False
##str2 = str(input("Enter the first string:\n"))
##str3 = str(input("Enter the second string:\n"))
##if check(str2, str3):
##    print("The first string can be found in the second string.")
##else:
##    print("The first string cannot be found in the second string.")
