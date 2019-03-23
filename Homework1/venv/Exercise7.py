import sys
vowels = ['a','o','u','e','i','y'] # I'm including 'y' as a vowel despite that 'y' can be both a vowel and a consonant
vowels_count = 0

print("Type something and I will count the vowels!")

input_text = input()
input_text = list(input_text)

for x in input_text:
    if x in vowels:
        vowels_count = vowels_count + 1


print(vowels_count)