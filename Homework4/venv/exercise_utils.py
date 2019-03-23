def find_words(list, n):
     approved_words_list = []
     for word in list:
         if len(word) > n:
             approved_words_list.append(word)
     if len(approved_words_list) == 0:
         return "No words longer than " + str(n) + " characters!"

     return approved_words_list

def find_longest_word(list):
    longest_word = ""
    for word in list:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

def bubble_sort(list): # although bubble sort is not the fastest sorting algorithm it is still good enought for demonstation
    for x in range(len(list) - 1):
        for y in range(len(list) - 1):
            if list[y] > list[y + 1]:
                list[y] = list[y] + list[y + 1]
                list[y + 1] = list[y] - list[y + 1]
                list[y] = list[y] - list[y + 1] # with the 3 preceeding lines I'm swapping the two variables around, y and y + 1

    return list