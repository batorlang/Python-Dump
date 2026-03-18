#Task four
from datetime import datetime, timedelta
print("This program uses the datetime library to deal with time.")
def menu():
    print('''What do you want to do:
1) Identify the components of a time object
2) Calculate age in days
3) Print the days of the week
4) Print the months
0) Stop''')
    choice = int(input("Your choice:\n"))
    return choice

def identify_components(date_input):
    date1 = datetime.strptime(date_input, "%d.%m.%Y %H:%M")
    print(f"You gave year {date1.year}")
    print(f"You gave month {date1.month}")
    print(f"You gave day {date1.day}")
    print(f"You gave hour {date1.hour}")
    print(f"You gave minute {date1.minute}\n")

def age_in_days(bd_input):
    bd = datetime.strptime(bd_input, "%d.%m.%Y")
    ref_date = datetime(2024, 1, 1)
    dif = ref_date - bd
    print(f"On January 1, 2024, you were {dif.days} days old.\n")

def print_days():
    mond = datetime(2024, 1, 1)
    for i in range(7):
        print(mond.strftime("%A"))
        mond += timedelta(days = 1)
    print("")
def print_month():
    start = datetime(2024, 1, 1)
    for i in range(12):
        print(start.strftime("%b"))
        next_month = start.month % 12 + 1
        next_year = start.year + (start.month // 12)
        start = datetime(next_year, next_month, 1)
    print("")
def main():
    while True:
        choicevalue = menu()
        if choicevalue == 1:
            date_input = str(input("Enter the date and time in the format 'dd.mm.yyyy hh:mm':\n"))
            identify_components(date_input)
        elif choicevalue == 2:
            bd_input = str(input("Enter your birthday as dd.mm.yyyy:\n"))
            age_in_days(bd_input)
        elif choicevalue == 3:
            print_days()
        elif choicevalue == 4:
            print_month()
        elif choicevalue == 0:
            print("See you again!")
            break
        else:
            print("Unknown choice, please try again.\n")
main()
