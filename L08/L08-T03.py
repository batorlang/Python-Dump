#Task three
from fractions import Fraction
print("Give the first fraction.")
num1 = int(input("Give numerator (top):\n"))
den1 = int(input("Give denominator (bottom):\n"))
print("Give the second fraction.")
num2 = int(input("Give numerator (top):\n"))
den2 = int(input("Give denominator (bottom):\n"))
exp = int(input("Give an exponent:\n"))
fraction1 = Fraction(num1, den1)
farction2 = Fraction(num2, den2)

addition = fraction1 + farction2
subtarction = fraction1 - farction2
multiplication = fraction1 * farction2
division = fraction1 / farction2
power = fraction1 ** exp

print(f'''Sum: {fraction1} + {farction2} = {addition}
Subtract: {fraction1} - {farction2} = {subtarction}
Multiply: ({fraction1}) * ({farction2}) = {multiplication}
Divide: ({fraction1}) / ({farction2}) = {division}
Power: ({fraction1})**{exp} = {power}''')
