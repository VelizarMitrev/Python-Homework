def factorial(num):
    if int(num) == 1:
        return 1
    return factorial(int(num)-1) * int(num)

inpur_number = input("Input a number: ")

print(factorial(inpur_number))