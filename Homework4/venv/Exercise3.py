from exercise_utils import find_longest_word
sentence = "A palindrome is a word which reads the same backward as forward e.g racecar"
word_list = sentence.split(" ")

print(str(find_longest_word(word_list)))