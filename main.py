import dash
from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

current_datetime = datetime.now()
print(calculate_salary(), current_datetime.date())
print(get_employees(), current_datetime.date())
