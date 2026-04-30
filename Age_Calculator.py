from dateutil.relativedelta import relativedelta
from datetime import datetime, date

def calculate_age(birth_date):
    today = date.today()
    age = relativedelta(today, birth_date)
    return age.years, age.months, age.days

# input
dob_input = input("Enter your birth date (DD-MM-YYYY): ")

# Convert string to date (strptime)
birth_date = datetime.strptime(dob_input, "%d-%m-%Y").date()

# Calculate age
years, months, days = calculate_age(birth_date)

print(f"Age: {years} years, {months} months, {days} days")