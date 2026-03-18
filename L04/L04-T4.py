#L04-T4
lowrange = int(input("Enter the lower limit of the range:\n"))
uprangeinput = int(input("Enter the upper limit of the range:\n"))
uprange = uprangeinput + 1
tf = False
for i in range(lowrange, uprange):
    if i % 5 != 0:
        print(f"{i} is NOT divisible by 5, rejecting.")
        continue
    elif i % 7 != 0:
        print(f"{i} is NOT divisible by 7, rejecting.")
        continue
    elif i % 5 == 0 and i % 7 == 0:
        print(f"The number {i} is divisible by 5 and 7.\nStopping the search.")
        tf = True
        break
if tf == False:
    print("No suitable value was found in the range.")
