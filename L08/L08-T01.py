#Task one
import math
import random
random.seed(1)

print("This program uses libraries to solve tasks.")
def menu():
    print('''What do you want to do:
1) Calculate the area of the circle
2) Guess the number
0) Stop''')
    choice = int(input("Your choice:\n"))
    return choice

def area(radius):
    pi = math.pi
    area = radius**2*pi
    return area

def guess():
    randomnumber = random.randint(0,1000)
    return randomnumber

def main():
    while True:
        choicevalue = menu()
        if choicevalue == 1:
            radius = int(input("Enter the radius of the circle as an integer:\n"))
            areaofcircle = area(radius)
            print(f"With a radius of {radius}, the area of the circle is {round(areaofcircle, 2)}.\n")
        elif choicevalue == 2:
            randomnum = guess()
            tries = 0
            print("Guess the integer drawn by the program.")
            while True: 
                guessnum = int(input("Enter an integer between 0 and 1000:\n"))
                tries += 1
                if guessnum == randomnum:
                    print(f"Correct! You used {tries} tries to guess the correct integer.\n")
                    break
                elif guessnum > randomnum:
                    print("The requested number is lower.")
                elif guessnum < randomnum:
                    print("The requested number is higher.")
        elif choicevalue == 0:
            print("See you again!")
            break
        else:
            print("Unknown choice, please try again.\n")
main()
