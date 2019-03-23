def factorial(number):
    sum = 1
    for x in range(1, int(number)):
        sum = sum * number
        number = number - 1
    return sum

input_number = input("Enter a number. ")

print(factorial(int(input_number)))