#Here I imported the possible modules I might use.
from datetime import datetime
import math
#Here I have the function of the menu which will ask the user for the choice and will return it to the main program. It even contains a error exceptions.
def menu():
    print('''You may select on of the following:
1) List available cars
2) Rent a car
3) Return a car
4) Count the money
0) Exit''')
    try:
        choice = int(input("What is your selection?\n"))
        return choice
    except ValueError:
        return None
#This function basically creates a matrix of the whole content of the file 'rentedVehicles.txt' for later use.
def need_for_return_car():
    matrix_of_rented = []
    rented_file = open("rentedVehicles.txt", "r")
    for line in rented_file:
        row = line.strip().split(",")
        matrix_of_rented.append(row)
    rented_file.close()
    return matrix_of_rented
#This function creates a list of the register numbers from the 'rentedVehicles.txt' file for later use.
def rented_cars_regnr():
    list_of_regnr = []
    rented_file = open("rentedVehicles.txt", "r")
    line1 = rented_file.readline()
    while line1 != "":
        list_of_regnr.append(line1[:7].strip())
        line1 = rented_file.readline()
    rented_file.close()
    return list_of_regnr
#This function creates a matrix of the whole content of the file 'vehicles.txt' for later use.
def matrix_of_all_cars_and_details():
    matrix_of_everything = []
    vehicles_file = open("vehicles.txt", "r")
    for line in vehicles_file:
        row = line.strip().split(",")
        matrix_of_everything.append(row)
    vehicles_file.close()
    return matrix_of_everything
#This function creates a list of all cars register numbers that are in the possession of the company for later use.
def all_cars_regnr():
    list_of_all_regnr = []
    vehicles_file = open("vehicles.txt", "r")
    for line in vehicles_file:
            regnr = line.split(",")[0].strip()
            list_of_all_regnr.append(regnr)
    return list_of_all_regnr
#This function creates a list of the available cars register number for later use.
def available_regnr_list():
    list_of_regnr2 = rented_cars_regnr()
    regnr_available = []
    vehicles_file = open("vehicles.txt", "r")
    for line in vehicles_file:
        regnr = line.split(",")[0].strip()
        if regnr not in list_of_regnr2:
            regnr_available.append(regnr) 
    return regnr_available

#This is the first function that contains prints for the user. This function creates a list of the available cars register number and than it will use the matrix where all details are found. Here I have created a small library for the details.
#In that way I can refer for the deatils more easily when I structure the string that will be printed. The given starting symbol for me is the '>'.
def list_available_cars():
    list_of_regnr2 = rented_cars_regnr()
    list_of_available = []
    vehicles_file = open("vehicles.txt", "r")
    line2 = vehicles_file.readline()
    while line2 != "":
        rented = False
        for i in list_of_regnr2:
            if line2 in i:
                rented = True
        if not rented:
            list_of_available.append(line2.strip())
        line2 = vehicles_file.readline() 
    vehicles_file.close()
    for vehicle in list_of_available:
        details_of_vehicles = vehicle.split(",")
        if len(details_of_vehicles) >= 0:
            reg_nr = details_of_vehicles[0]
            model = details_of_vehicles[1]
            price_per_day = details_of_vehicles[2]
            properties = details_of_vehicles[3:]
            properties_string = ""
            first_property = True
            for properties2 in properties:
                if first_property:
                    properties_string += properties2
                    first_property = False
                else:
                    properties_string += ", " + properties2
            print("The following cars are available:")
            print(f"""> Reg. nr: {reg_nr}, Model: {model}, Price per day: {price_per_day}""")
            print(f"Properties: {properties_string}")
    print("")
    return list_of_available

#This is the second function which contains prints for the user. The function first asks the user which car is the desired one. The it might hasppen that the reg. number does nopt exist or the car is rented already.
#Than the program asks for the users birthday. If the user is a returning customer, than the program will automatically rent the car and greet the user. If not, than comes the next phase.
#The program decides if the user is between 18 and 75. It the user fits into the age requirement, than proceeds.
#The next step is to ask the user to enter their name correctly. The function will ask for the name untill it is given accordingly.
#The next step is the correct email address from the user. The program can differ the wrong email patterns and ask for the email again if the user fails to give the correct one.
#Finally the program will apopend the user information to the customer file and append the rental details to the rented vehicles file as well. Than the user will get a response from the program that the rent was successful.
def rent_a_car():
    matrix_of_customers = []
    while True:
        regnrinput = input("Give the register number of the car you want to rent:\n")
        if regnrinput in rented_cars_regnr():
            print(f"{regnrinput} already rented\n")
        elif regnrinput not in rented_cars_regnr() and regnrinput not in all_cars_regnr():
            print("Car does not exist\n")
        elif regnrinput in available_regnr_list():
            break
    while True:
        try:
            birthdayinput = input("Please enter you birthday in the form DD/MM/YYYY:\n")
            birthday = datetime.strptime(birthdayinput, "%d/%m/%Y").date()
            birthday_formatted = birthday.strftime("%d/%m/%Y")
            today = datetime.today()
            age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
            customer_file = open("customers.txt", "r")
            line4 = customer_file.readline()
            while line4 != "":
                matrix_of_customers.append(line4.strip().split(","))
                line4 = customer_file.readline()
            customer_file.close()
            found = False
            for i in range(len(matrix_of_customers)):
                if birthday_formatted in matrix_of_customers[i]:
                    found = True
                    row_index = i
                    break
            if found == True:
                print(f"Hello {matrix_of_customers[i][1]}")
                today = datetime.today()
                today_formatted = today.strftime("%d/%m/%Y %H:%M")
                renting_string = f"{regnrinput},{birthday_formatted},{today_formatted}\n"
                customer_string = f"{birthday_formatted},{matrix_of_customers[i][1]},{matrix_of_customers[i][2]},{matrix_of_customers[i][3]}\n"
                rented_file2 = open("rentedVehicles.txt", "a")
                line3 = rented_file2.writelines(renting_string)
                rented_file2.close()
                print(f"You rented the car {regnrinput}\n")
                return
            elif found == False:
                if age < 18:
                    print("You are too young to rent a car.\n")
                    break
                elif age > 75:
                    print("You are too old to rent a car.\n")
                    break
                else:
                    print("Age OK")
        except ValueError:
            print("There is no such date. Try again!")
            continue
        print("Names contain only letters and start with capital letters.")
        while True:
            first_name = input("Enter the first name of the customer:\n")
            last_name = input("Enter the last name of the customer:\n")
            if first_name[0].isupper() and first_name.isalpha() and last_name[0].isupper() and last_name.isalpha():
                break
            else:
                print("Names containing only letters and start with capital letters.")
        while True:
            email = input("Give your email:\n")
            if "@" in email and "." in email:
                at_position = email.index("@")
                if "." in email[at_position:]:
                    valid_chars = True
                    for char in email:
                        if not (char.isalpha() or char.isdigit() or char in {"@", "."}):
                            valid_char = False
                            break
                    if valid_chars == True:
                        print(f"Hello {first_name}")
                        today = datetime.today()
                        today_formatted = today.strftime("%d/%m/%Y %H:%M")
                        birthday_formatted = birthday.strftime("%d/%m/%Y")
                        renting_string = f"{regnrinput},{birthday_formatted},{today_formatted}\n"
                        customer_string = f"{birthday_formatted},{first_name},{last_name},{email}\n"
                        rented_file2 = open("rentedVehicles.txt", "a")
                        line3 = rented_file2.writelines(renting_string)
                        rented_file2.close()
                        customer_file = open("customers.txt", "a")
                        line4 = customer_file.writelines(customer_string)
                        customer_file.close()
                        print(f"You rented the car {regnrinput}\n")
                        break
                    else:
                        print("Give a valid email address")
                else:
                    print("Give a valid email address")
            else:
                print("Give a valid email address")
        break

#This function also contains prints for the user. This function asks the user for the rented vehicles register number and according to that, it will delete the line containing it from the rented file and will append a line into the transactions file.
#Also will print the price that has to be paid and give feedback about the process of the system. I have put the print after the program finished the file writing, so the user can be sure that there will not be nay mistake.
def return_a_car():
    while True:
        regtnrtoreturn = input("Give the register number of the car you want to return:\n")
        if regtnrtoreturn not in all_cars_regnr():
            print("Car does not exist\n")
            break
        else:
            if regtnrtoreturn in available_regnr_list():
                print("Car is not rented\n")
                break
            else:
                if regtnrtoreturn in rented_cars_regnr():
                    for rented_car in need_for_return_car():
                        if rented_car[0] == regtnrtoreturn:
                            regnr_for_return = rented_car[0]
                            birthday = rented_car[1]
                            rental_date = rented_car[2]
                            rental_date_calc = datetime.strptime(rental_date, "%d/%m/%Y %H:%M")
                            return_date = datetime.today()
                            return_formatted = return_date.strftime("%d/%m/%Y %H:%M")
                            birthday_formatted = datetime.strptime(birthday, "%d/%m/%Y").strftime("%d/%m/%Y")
                            timedelta_days = (return_date - rental_date_calc).days
                            timedelta = max(int(timedelta_days), 1)
                            break
                    car_details = matrix_of_all_cars_and_details()
                    for car_details in matrix_of_all_cars_and_details():
                        if car_details[0] == regtnrtoreturn:
                            price_per_day = float(car_details[2])
                            break
                    cost1 = price_per_day * timedelta
                    cost2 = "{:.2f}".format(int(cost1))
                    transaction_string = f"\n{regnr_for_return},{birthday_formatted},{rental_date},{return_formatted},{timedelta_days},{cost2}\n"
                    transaction_file = open("transActions.txt", "a")
                    line5 = transaction_file.write(transaction_string)
                    transaction_file.close()
                    remove_index = rented_cars_regnr().index(regtnrtoreturn)
                    rented_file2 = open("rentedVehicles.txt", "r")
                    lines = rented_file2.readlines()
                    rented_file2.close()
                    rented_file2 = open("rentedVehicles.txt", "w")
                    current_index = 0
                    for line in lines:
                        if current_index != remove_index:
                            rented_file2.write(line)
                        current_index += 1
                    rented_file2.close()
                    print(f"The rent lasted {timedelta_days} and the cost is {cost2} euros\n")
                    break
#This function can calculate the total money or the total income of the company calculated from file.
#The function creates a matrix out of the file transActions.txt and that n it creates a list of the last coulum. Than it will sum up the list and return it to the string that will be printed.
def count_the_money():
    matrix_of_transaction = []
    list_of_prices = []
    transaction_file = open("transActions.txt", "r")
    for line in transaction_file:
        row = line.strip().split(",")
        matrix_of_transaction.append(row)
    transaction_file.close()
    for i in range(len(matrix_of_transaction)):
        list_of_prices.append(float(matrix_of_transaction[i][5]))
    summoney = sum(list_of_prices)
    sum_of_money = "{:.2f}".format(summoney)
    print(f"The total amount of money is {sum_of_money} euros\n")

#This is the main function. This function handles the manu, everything that is printed to the user. It has an endless loop thta can be stopped by inputting 0.
def main():
    while True:
        choicevalue = menu()
        if choicevalue == 1:
            list_available_cars()
        elif choicevalue == 2:
            rent_a_car()
        elif choicevalue == 3:
            return_a_car()
        elif choicevalue == 4:
            count_the_money()
        elif choicevalue == 0:
            print("Bye")
            break
        
        elif choicevalue == None:
            print("Incorrect input!")
main()
