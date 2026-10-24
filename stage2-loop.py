# Project: Don't Forget Me — Stage 2: Repeating Food Input with a Loop
# Learning reference: GeeksforGeeks, "How to Use while True in Python"
# https://www.geeksforgeeks.org/python/how-to-use-while-true-in-python/
# I used this tutorial to understand how while True repeats a block of code.

# Learning reference: GeeksforGeeks, "Python Break Statement"
# https://www.geeksforgeeks.org/python/python-break-statement/
# I used this tutorial to understand how break exits a loop when the user enters "q".

# Learning reference: GeeksforGeeks, "Python Program to Find Number of Days Between Two Given Dates"
# https://www.geeksforgeeks.org/python/python-program-to-find-number-of-days-between-two-given-dates/
# I used this example to calculate the number of days between two dates.





from datetime import datetime

while True:
    food_name = input("Enter food name (q to quit): ")

    # Stop the loop when the user enters q.
    if food_name == "q":
        break

    expiry_date = input("Enter expiry date (DD/MM/YYYY): ")
    
    # Convert the entered date text into a date object.
    expiry = datetime.strptime(expiry_date, "%d/%m/%Y").date()
    today = datetime.today().date()
    
    # Calculate how many days remain until the expiry date.
    days_left = (expiry - today).days

    print("Food:", food_name)
    print("Expiry date:", expiry_date)
    print("Days left:", days_left)
    print("----------------")
    
