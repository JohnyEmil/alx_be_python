from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Fix: use datetime.now() instead of date.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

def calculate_future_date(days):
    current_date = date.today()  # Fix: use date.today() instead of date.now()
    future_date = current_date + timedelta(days=days)
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted}")

display_current_datetime()

days = int(input("Enter the number of days to add to the current date: "))  # Fix: added colon and space

calculate_future_date(days)



