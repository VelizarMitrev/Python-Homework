def find_armstrong_number(lower, upper):
    for num in range(int(lower), int(upper) + 1):

        size = len(str(num)) # the number of digits in the number
        sum = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)

input_lower_bound = input("Input lower bound. ")
input_higher_bound = input("Input higher bound. ")

print(find_armstrong_number(str(input_lower_bound), str(input_higher_bound)))

