import sys
import time
import winsound

def encode(text):
    morse_code_dictionary = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
                       'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-',
                       'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
                       'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
                       'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-', ' ': '/'}

    encoded = ""
    for letter in text:
        encoded += morse_code_dictionary.get(letter)
        encoded +=" "

    return encoded


def generate_beep(duration):
    frequency = 550
    winsound.Beep(frequency, duration)


def morse_code_sound(morse_code):
    for x in morse_code:
        if x == '.':
            generate_beep(100)
        elif x == '-':
            generate_beep(330)
        elif x == ' ':
            time.sleep(0.15)
        elif x == '/':
            time.sleep(0.20)


print("Do you want to enter text from a file or from console?")
print("Enter 1 for console.")
print("Enter 2 for file.")

choice = input()

if int(choice) == 1:
    print("Enter text")
    text = input()
    print(encode(text))
    morse_code_sound(encode(text))

elif int(choice) == 2:
    print("Enter full path of file")
    file_path_input = input()
    text_file = open(file_path_input, "r")
    words_array = text_file.readlines()
    text = ' '.join(words_array)
    print(encode(text))
    morse_code_sound(encode(str(text)))

else:
    print("Invalid operation you can enter only 1 or 2.")
    sys.exit(1)

