def fibonacci(num): # this is a recursive solution, in this case it's slower but the code is cleaner
   if num <= 1:
       return num
   else:
       return(fibonacci(num-1) + fibonacci(num-2))

numbers_sequence = input("Enter how many numbers from the fibonacci sequence you want to print: ")

print("Fibonacci sequence:")
for i in range(int(numbers_sequence)):
    print(fibonacci(i))