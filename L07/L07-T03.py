#Task three
tobetested = input("Enter the name of the file to be read:\n")
file1 = open(tobetested, "r")
file2 = open("Palindromes.txt", "w")
listofwords = []
line = file1.readline()

while line != "":
    newline = line.strip()
    usableline = newline.lower()
    if usableline == usableline[::-1]:
        print(f"row '{newline}' is a palindrome.")
        listofwords.append(newline + "\n")
        
    else:
        print(f"row '{newline}' is not a palindrome.")

    line = file1.readline()

file2.writelines(listofwords)
file1.close()
file2.close()
