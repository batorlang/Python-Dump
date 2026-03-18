numbers = []
while True:
    user_input = input("Enter an integer (or type 'done' to finish input):\n")
    if user_input == 'done':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer")

while True:
    target = input("Enter the target sum:\n")
    try:
        targetsum = int(target)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
pairs = []
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == targetsum:
            pairs.append((numbers[i], numbers[j]))
if pairs:
    print(f"Pairs with a sum of {targetsum}:")
    for pair in pairs:
        print(pair)
else:
    print(f"No pairs found with a sum of {targetsum}.")
