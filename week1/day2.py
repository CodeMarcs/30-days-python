from datetime import date

def calculate_age(day, month, year):
    today = date.today() 
    birth_date = date(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    return age
    
print("Welcome to Day 2 -- Basic User Age Calculator")

name = input("Enter your name: ")
birthdate = date(int(input("Enter your birth year (YYYY): ")), int(input("Enter your birth month (MM): ")), int(input("Enter your birth day (DD): ")))

print(f"Hello, {name}! You are {calculate_age(birthdate.day, birthdate.month, birthdate.year)} years old.")

# day 2
