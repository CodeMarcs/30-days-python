# simple welcome bot

import time
import datetime

print("Hello, I am CodeMarcs -- this is day 4")
print("I am a simple welcome bot!")
time.sleep(1)
name = input("Enter your name: ")
print(f"Hello, {name}! Nice to meet you!")
time.sleep(1)   
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"The current date and time is: {current_time}")
time.sleep(1)
print("Welcome to Day 4 -- Simple Welcome Bot")