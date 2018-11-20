# Excersise 1
# GCD


print('Getting greatest common denominator of two integers')

a = int(input('type one integer : '))
b = int(input('type the other integer : '))


while (a != b):
    if a >b:
        a = a - b
    else:
        b = b - a

print(a)

