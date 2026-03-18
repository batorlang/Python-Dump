#Task four
name = input("Give the name of the CSV file:\n")
file = open(name, "r")
lines = file.readlines()
file.close()

data = []
for line in lines:
    row = line.strip().split(",")
    data.append(row)
     
for i in range(len(data)):
    print(data[i][1].strip())
