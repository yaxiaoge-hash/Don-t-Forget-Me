from datetime import datetime

while True:
    food_name = input("Enter food name: ")
    expiry_date = input("Enter expiry date (DD/MM/YYYY): ")

    expiry = datetime.strptime(expiry_date, "%d/%m/%Y").date()
    today = datetime.today().date()

    days_left = (expiry - today).days

    print("Food:", food_name)
    print("Expiry date:", expiry_date)
    print("Days left:", days_left)
    

