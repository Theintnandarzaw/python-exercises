i = 0
numbers = []

while i < 6:
    print("At the top is %r "%i)
    numbers.append(i)

    i=i+1
    print("Numbers now : ",numbers)
    print("At the bottom i is %r"%i)


print("The numbers:")

for num in numbers:
    print(num)
