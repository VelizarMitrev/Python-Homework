print("Calculator")
first_number = input("Enter the first number - ")
operator = input("Enter the operator - ")
second_number = input("Enter the second number - ")

total = 0

if operator == "+":
    total = int(first_number) + int(second_number)
elif operator == "-":
    total = int(first_number) - int(second_number)
elif operator == "/":
    total = int(first_number) / int(second_number)
elif operator == "*":
    total = int(first_number) * int(second_number)

print("The total is " + str(total))