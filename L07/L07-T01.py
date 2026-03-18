#Task one
def main():
    filename = input("Enter the name of the file to be saved:\n")
    return filename
name = main()
def file_write(name):
    file = open(name, "w")
    ip = ""
    listofinputs = []
    while ip != "0":
        ip = input("Enter a name to save to the file (0 to stop):\n")
        if ip != "0":
            listofinputs.append(ip)
            listofinputs.append("\n")
        else:
            file.writelines(listofinputs)
            break
    file.close()

def file_read(name):
    print(f"The following names are stored in the file '{name}':")
    file = open(name, "r")
    line = file.readline()
    while line != "":
        if line != "":
            print(line.strip())
            line = file.readline()
        else:
            break
    file.close()


file_write(name)
file_read(name)
