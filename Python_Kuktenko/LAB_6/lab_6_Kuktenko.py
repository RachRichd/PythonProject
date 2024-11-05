#1

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    year = test_data[i]
    print(year, "->", end = " ")
    result = is_year_leap(year)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

        
#2

        def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    days_in_months = [
        31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30, 
        31, 31, 30, 31, 30, 31
    ]
    return days_in_months[month - 1]

test_years = [1900, 2000, 2016, 1987, 2024, 2100, 2021, 3456, 1001]
test_months = [2, 2, 1, 11, 2, 2, 6, 13, 0]
test_results = [28, 29, 31, 30, 29, 28, 30, 32, 1]

for i in range(len(test_years)):
    year = test_years[i]
    month = test_months[i]
    print(year, month, "->", end = " ")
    result = days_in_month(year, month)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

        
#3

def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
        
    days_in_months = [
        31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]
    return days_in_months[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1:
        return None

    days_in_current_month = days_in_month(year, month)
    if days_in_current_month is None or day > days_in_current_month:
        return None

    day_number = 0
    for m in range(1, month):
        day_number += days_in_month(year, m)
    day_number += day
    return day_number
 
print(day_of_year(2001, 3, 1))   
print(day_of_year(2022, 2, 24))
print(day_of_year(2004, 12, 31)) 
print(day_of_year(2019, 2, 29))   
print(day_of_year(2021, 6, 15))  
print(day_of_year(2024, 1, 1))    
print(day_of_year(1900, 2, 32)) 
print(day_of_year(1900, 2, 0))


#4

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


#5

def liters_100km_to_miles_gallon(liters):
    miles_per_100km = 100 * 0.621371  
    gallons = liters * 0.264172  
    return miles_per_100km / gallons

def miles_gallon_to_liters_100km(miles):
    kilometers_per_gallon = miles * 1.60934  
    liters_per_100km = 100 / kilometers_per_gallon * 3.7854 
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))   
print(liters_100km_to_miles_gallon(7.5))   
print(liters_100km_to_miles_gallon(10.0))  

print(miles_gallon_to_liters_100km(60.3))  
print(miles_gallon_to_liters_100km(31.3)) 
print(miles_gallon_to_liters_100km(23.5)) 


#6

def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
        
print(is_a_triangle(7, 10, 5))  
print(is_a_triangle(1, 10, 12)) 
print(is_a_triangle(0, 0, 0))    
print(is_a_triangle(10, 10, 20))
print(is_a_triangle(1000, 1001, 1)) 
print(is_a_triangle(5.5, 4.2, 3.8))


#7

def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
        
    sides = sorted([a, b, c])  
    return sides[0]**2 + sides[1]**2 == sides[2]**2

print(is_a_triangle(7, 10, 5))  
print(is_a_triangle(1, 10, 12)) 
print(is_a_triangle(0, 0, 0))    
print(is_a_triangle(10, 10, 20))
print(is_a_triangle(1000, 1001, 1)) 
print(is_a_triangle(5.5, 4.2, 3.8))