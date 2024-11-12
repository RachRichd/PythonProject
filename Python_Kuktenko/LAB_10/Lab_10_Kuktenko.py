#Task 1

def hidden_word(word, text):
    index = 0
    for char in word:
        index = text.find(char, index) 
        if index == -1:  
            return "NO"
        index += 1 
    return "YES"

print(hidden_word("dog", "vcxzxduybfdsobywuefgas"))  
print(hidden_word("dog", "vcxzxdcybfdstbywuefsas")) 

#Task 2

def hidden_word_text(word, text):
    try:
        index = 0
        for char in word:
            index = text.find(char, index)  
            if index == -1:  
                return "NO"
            index += 1  
        return "YES"
    except Exception as e:
        return f"ERROR: {e}"

# Тест з коректними даними
print(hidden_word_text("dog", "vcxzxduybfdsobywuefgas"))  
print(hidden_word_text("dog", "vcxzxdcybfdstbywuefsas"))  

# Тест з некоректними даним
print(hidden_word_text("dog", None)) 
print(hidden_word_text(None, "vcxzxduybfdsobywuefgas")) 


#Task 3

def get_integer(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
            else:
                return value
        except ValueError:
            print("Error: wrong input")
            
min_value = 10
max_value = 100
prompt = f"Please enter an integer between {min_value} and {max_value}: "

result = get_integer(prompt, min_value, max_value)
print(f"Valid input received: {result}")