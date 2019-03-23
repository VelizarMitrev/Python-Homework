number_list = [3, 6, 13, 2, 3, 3, 13, 5, 5]

occurences_dictionary = {}

for number in number_list:
    if number not in occurences_dictionary:
        occurences_dictionary[number] = 1
    else:
        occurences_dictionary[number] = occurences_dictionary[number] + 1

for number in occurences_dictionary:
    print("The number " + str(number) + " is found " + str(occurences_dictionary[number]) + " in the list!")
