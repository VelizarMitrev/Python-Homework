nand = input("Choose a number ")
sum = 0

for x in range(1, int(nand) + 1):
    if x % 3 == 0 or x % 5 == 0:
        sum = sum + x


print("The sum number is " + str(sum))