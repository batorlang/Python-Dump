#Task one
start = int(input("Enter the starting value:\n"))
endinp = int(input("Enter the ending value:\n"))
end = endinp+1
string = ''
print("Implementation wiht a for loop:")
for i in range(start, end):
    i = str(i)
    string = string + i + ' '
print(string)
print("Implementation with a while loop:")
n = start
string = ''
while(n <= endinp):
    k = str(n)
    string = string + k + ' '
    n += 1
print(string)
#Task two
text = str(input("Enter a string:\n"))
counter = 0
vowels = "aeiouAEIOU"
for i in text:
    if i in vowels:
        counter += 1
print(counter)
#Task three
a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))
while a < 1000 and b < 1000:
    print("a: ",a," b: ",b)
    a = a * 2
    b = b + 100
if a > 1000 and b > 1000:
    print("a exceeded 1000")
    print("b exceeded 1000")
elif b > 1000:
    print("b exceeded 1000")
elif a > 1000:
    print("a exceeded 1000")
