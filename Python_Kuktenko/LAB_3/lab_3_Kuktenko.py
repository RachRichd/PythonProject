import math
#1

def gauss_function(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mean) / std_dev) ** 2)

x = 1.0    
mean = 0.0  
std_dev = 1.0  

result = gauss_function(x, mean, std_dev)
print(f"Value of Gaussian function for x={x}, mean={mean}, std_dev={std_dev}: {result}")


#2

john = 3   
mary = 5   
adam = 6  

print(f"{john}, {mary}, {adam}")

total_apples = john + mary + adam
print(total_apples)

print(f"Total number of apples: {total_apples}")

#3

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#4

x = input("Enter a value for x: ")
x = float(x) 

y = 3 * (x ** 3) - 2 * (x ** 2) + 3 ** x - 1

print("y =", y)

#5
# This program computes the number of seconds in a given number of hours

# Number of hours for which we want to calculate the total number of seconds
hours = 2

# Number of seconds in one hour
seconds_per_hour = 3600

# Print the number of hours
print("Hours:", hours)

# Compute and print the number of seconds in the given number of hours
print("Seconds in", hours, "hours:", hours * seconds_per_hour)

# End of the program
print("Bye")

#6

a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))


print("Choose an arithmetic operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter the number of the operation (1/2/3/4): ")
if operation == '1':
    print("Addition:", a + b)
elif operation == '2':
    print("Subtraction:", a - b)
elif operation == '3':
    print("Multiplication:", a * b)
elif operation == '4':
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Cannot divide by zero")
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")

print("\nThat's all, folks!")

#7

x = float(input("Enter value for x: "))

inner4 = x + 1 / x
inner3 = x + 1 / inner4
inner2 = x + 1 / inner3
inner1 = x + 1 / inner2
y = 1 / inner1

print("y =", y)

#8

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

total_minutes = hour * 60 + mins + duration

end_hour = (total_minutes // 60) % 24 
end_minute = total_minutes % 60

print(f"End time: {end_hour:02}:{end_minute:02}")