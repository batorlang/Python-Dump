#Task one
def input_integers():
    input_string = input("Give integers separated by comma:\n")
    list_of_chars = input_string.split(",")
    list_of_ints = []
    for char in list_of_chars:
        list_of_ints.append(int(char))
    return list_of_ints
intlist = input_integers()
print(f"Reverted list:{intlist[::-1]}")


#Task two
def input_integers():
    input_string = input("Give integers separated by comma:\n")
    list_of_chars = input_string.split(",")
    list_of_ints = []
    list_removed = []
    lastchar = ""
    for char in list_of_chars:
        list_of_ints.append(int(char))
    for char2 in list_of_chars:
        if char2 != lastchar:
            list_removed.append(int(char2))
            lastchar = char2
    print(f"Original list: {list_of_ints}")
    print(f"List with removed duplicates: {list_removed}")

input_integers()
