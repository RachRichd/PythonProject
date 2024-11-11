#1

def mysplit(string):
    list_split = []

    if string.isspace() or string == "":  
        return list_split

    word = ''
    for char in string:
        if char.isspace():
            if word:
                list_split.append(word)
                word = ''
        else:
            word += char
    
    if word:  
        list_split.append(word)
    
    return list_split

#Test
print(mysplit("abcabc  "))          
print(mysplit("abc, abc"))        
print(mysplit("abc abc,abc"))               
print(mysplit(""))                        
print(mysplit("    "))                    

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))


#2

number_dict = {
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '0': ('###', '# #', '# #', '# #', '###')
}

def display_number(num):
    if num < 0:
        print("The number must be non-negative")
        return

    num_str = str(num)

    for level in range(5):
        for digit in num_str:
            print(number_dict[digit][level], end=' ')
        print()

number_input = input('Enter an integer: ')

try:
    number = int(number_input)
    display_number(number)
except ValueError:
    print("Please, enter a valid integer: ")

    
#Task 1

def caesar_cipher(text, shift):
    cipher = ''
    for char in text:
        if char.isalpha():
            code = ord(char) + shift
            if char.isupper():
                if code > ord('Z'):
                    code -= 26
                elif code < ord('A'):
                    code += 26
            elif char.islower():
                if code > ord('z'):
                    code -= 26
                elif code < ord('a'):
                    code += 26
            cipher += chr(code)
        else:
            cipher += char
    return cipher

def main():
    text = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if shift < 1 or shift > 25:
                raise ValueError
            break
        except ValueError:
            print("Invalid shift value. Please enter an integer between 1 and 25.")
            
    encoded_text = caesar_cipher(text, shift)
    print("Encoded message:", encoded_text)

main()