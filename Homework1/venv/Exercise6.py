nand = input("Choose a number ")
operator = input("Input + OR * for either computing a number or multiplying it ")
sum = 0

if operator == "+":
    for x in range(1, int(nand) + 1):
            sum = sum + x

if operator == "*":
    sum = 1
    for x in range(1, int(nand) + 1):
        sum = sum * x


print("The final number is " + str(sum))