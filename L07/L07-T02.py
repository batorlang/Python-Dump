#Task two
def file_copy(fileA, fileB):
    copycontent = []
    file = open(fileA, "r")
    line = file.readline()
    while line != "":
        if line != "":
            copycontent.append(line)
            line = file.readline()
        else:
            break
    file.close()
    file = open(fileB, "w")
    for i in copycontent:
        file.writelines(i)
    file.close()
    print("File copied successfully!")


fileA = input("Please give the name of the source file:\n")
fileB = input("Please give the name of the destination file:\n")
file_copy(fileA, fileB)
