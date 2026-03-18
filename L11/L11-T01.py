def powers(x):
    x2 = x ** 2
    x3 = x ** 3
    x4 = x ** 4
    x5 = x ** 5
    return x2, x3, x4, x5

x = float(input("Enter a number:\n"))
result = powers(x)
print(f"""Powers of {x}:
x^2: {round(result[0], 4)}
x^3: {round(result[1], 4)}
x^4: {round(result[2], 4)}
x^5: {round(result[3], 4)}""")
