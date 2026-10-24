
# Project: Don't Forget Me — Stage 1: Basic Python and Date Calculation
# Learning reference: GeeksforGeeks, "Python input() Function"
# https://www.geeksforgeeks.org/python/python-input-function/
# I used this tutorial to learn how input() receives text from the user.

# Learning reference: GeeksforGeeks, "Python Program to Find Number of Days Between Two Given Dates"
# https://www.geeksforgeeks.org/python/python-program-to-find-number-of-days-between-two-given-dates/
# I used this example to understand date calculations and the .days attribute.



from datetime import datetime

while True:
    food_name = input("Enter food name: ")
    expiry_date = input("Enter expiry date (DD/MM/YYYY): ")

    # Convert the typed date from text into a Python date object.
    expiry = datetime.strptime(expiry_date, "%d/%m/%Y").date()
    today = datetime.today().date()

    # Subtract today's date from the expiry date to calculate the days remaining.
    days_left = (expiry - today).days


    # Display the result in the Python terminal.
    print("Food:", food_name)
    print("Expiry date:", expiry_date)
    print("Days left:", days_left)
    

