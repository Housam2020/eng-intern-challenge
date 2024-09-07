import sys

# Define Braille to English and English to Braille mappings
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 
    'OO..O.': 'm', 'OO.O.O': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOO.O': 'q', 'O.OOO.': 'r', 
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OO..O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z', '......': ' ', '.....O': 'capital', '.O.OOO': 'number'
}

# Define the numbers, using the same Braille symbols as letters 'a' to 'j'
braille_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# Reverse map from English to Braille for letters, numbers, and symbols
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.O.O', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOO.O', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OO..O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 'A': '.....O' + 'O.....', 'B': '.....O' + 'O.O...', 
    'C': '.....O' + 'OO....', 'D': '.....O' + 'OO.O..', 'E': '.....O' + 'O..O..', 
    'F': '.....O' + 'OOO...', 'G': '.....O' + 'OOOO..', 'H': '.....O' + 'O.OO..', 
    'I': '.....O' + '.OO...', 'J': '.....O' + '.OOO..', '1':  'O.....', 
    '2':  'O.O...', '3':  'OO....', '4':  'OO.O..', 
    '5':  'O..O..', '6':  'OOO...', '7':  'OOOO..', 
    '8':  'O.OO..', '9':  '.OO...', '0':  '.OOO..'
}

def is_braille(text):
    return all(char in 'O.' for char in text)

def braille_to_text(braille):
    result = []
    capital_flag = False
    number_flag = False
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    
    for char_braille in braille_chars:
        if char_braille == '.....O':  # Capital follows symbol
            capital_flag = True
            continue
        if char_braille == '.O.OOO':  # Number follows symbol
            number_flag = True
            continue
        # space = end of number
        if number_flag and char_braille == '......':
            number_flag = False
            result.append(' ')
            continue
        if number_flag:
            english_char = braille_numbers.get(char_braille, '?')  # Use number map
            if english_char == '?':  # Handle invalid number characters
                result.append('?')
            else:
                result.append(english_char)
        else:
            english_char = braille_to_english.get(char_braille, '?')  # Use regular map
            if capital_flag:
                english_char = english_char.upper()
                capital_flag = False
            result.append(english_char)
    return ''.join(result)

def text_to_braille(text):
    result = []
    number_flag = False
    for char in text:
        if char == ' ' and number_flag == True:
            number_flag == False
            result.append('......')
            continue
        if char.isupper():
            result.append('.....O')  # Capital follows symbol
            result.append(english_to_braille[char.lower()])
        elif char.isdigit():
            if number_flag == False:
                result.append('.O.OOO')  # Number follows symbol
                number_flag = True
            result.append(english_to_braille[char])
        elif char in english_to_braille:
            result.append(english_to_braille[char])
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        return
    
    input_str = " ".join(sys.argv[1:])
    
    if is_braille(input_str):
        print(braille_to_text(input_str))
    else:
        print(text_to_braille(input_str))

if __name__ == "__main__":
    main()
