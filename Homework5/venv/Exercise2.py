text = input()

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
consonants = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
              "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"}
whitespaces = [" "]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

vowel_count = 0
consonant_count = 0
whitespace_count = 0
digits_count = 0

for letter in text:
    if letter in vowels:
        vowel_count+=1

    if letter in consonants:
        consonant_count+=1

    if letter in whitespaces:
        whitespace_count+=1

    if letter in digits:
        digits_count+=1

print("Vowels: " + str(vowel_count))
print("Consonant: " + str(consonant_count))
print("Whitespace: " + str(whitespace_count))
print("Digit: " + str(digits_count))