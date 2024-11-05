#Ex 1
import random

# Генеруємо 10 випадкових чисел в діапазоні від 1 до 20
numbers_list = [random.randint(1, 20) for _ in range(10)]

# Створюємо кортеж з отриманого списку
numbers_tuple = tuple(numbers_list)
print("Generated numbers:", numbers_tuple)

n = int(input("Enter n: "))
result = [num for num in numbers_tuple if num < n]

print("Numbers less than", n, ":", result)

#Ex 2

my_tuple = ("cat", "dog", "rabbit")

joined_string = ", ".join(my_tuple)

print("Connected lines:", joined_string)

#Ex 3

dictionary = {
    "Bib": ("Bob", 1987, 344),
    "Vivald": ("Xenia", 1922, 501),
    "Sonic: Big Round Wet Towel": ("DedilB", 2005, 29)
}

name_book = input("Book name:")

if name_book in dictionary:
    author, year, pages = dictionary[name_book]
    print(f"Author: {author} \nYear: {year} \nPages: {pages}")
else:
    print("Book not found in the library.")

# Ex 4

students = {
    "Kuktenko": (19, "Film art", 4.9),
    "Gonchar": (21, "Physical culture", 5),
    "Butnyk": (19, "Physics", 4.3),
    "Yarmolenko": (20, "Chemistry", 4.1)
}

surname = input("Enter the surname of the student: ")

if surname in students:
    age, faculty, grade = students[surname]
    print(f"Age: {age}, Faculty: {faculty}, Average Grade: {grade}")
else:
    print("Student not found in the database.")


#5
phone_book = {
    "Josh Washinghton": ["0971341363", "0678945678"],
    "Sam Giddings": ["88005553535", "0983457453"],
    "Mike Monroe": ["0443785634", "0634985761"],
    "Emily Davis": ["+338579346", "0984568731"],
    "Chris Bratley": ["0967586643", "0875562985"]
}

def add_phone_number(contact_name, new_number):
    if contact_name in phone_book:
        phone_book[contact_name].append(new_number)
        print(f"New phone number added for {contact_name}.")
    else:
        print(f"Contact {contact_name} not found in the phone book.")

contact_name = input("Enter the name of the contact: ")
new_number = input("Enter the new phone number: ")
add_phone_number(contact_name, new_number)

print("\nPhone numbers for all contacts:")
for name, numbers in phone_book.items():
    print(f"{name}: {', '.join(numbers)}")

