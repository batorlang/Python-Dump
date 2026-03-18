#Task three
shoppinglist = []
def menu():
    print(f'''Your shopping list contains the following products:
{shoppinglist}
You can choose from the functions below:
1) Add
2) Remove
0) End''')
    choice = int(input("Your choice:\n"))
    return choice
def add(thing1):
    shoppinglist.append(thing1)
def remove(thing2):
    shoppinglist.pop(int(thing2) - 1)
def main():
    while True:
        choicevalue = menu()
        if choicevalue == 1:
            thing1 = input("Enter the product to be added:\n\n")
            add(thing1)
        elif choicevalue == 2:
            print(f"You have {len(shoppinglist)} items in your shopping list.")
            thing2 = int(input("Enter the location of the product to be removed:\n\n"))
            remove(thing2)
        elif choicevalue == 0:
            print(f'''You are going to buy the following products:
{shoppinglist}''')
            break
        else:
            print("Unknown selection.\n")
main()
