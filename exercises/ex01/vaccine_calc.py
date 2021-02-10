"""A vaccination calculator."""

__author__ = "730135317"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population: int = int(input("Population: "))
Doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent_vaccinated: int = int(input("Target percent vaccinated: "))
target_amount_vaccinated: float = target_percent_vaccinated / 100 
percentage = "{:.0%}".format(target_amount_vaccinated)

already_vaccinated: float = (((Doses_administered) / 2) / (population)) * 100
percentage_to_go: float = target_percent_vaccinated - already_vaccinated
number_of_people_needed_to_reach_target: float = (percentage_to_go / 100) * population
doses_needed: float = number_of_people_needed_to_reach_target * 2
how_many_days = round(doses_needed / doses_per_day)

today: datetime = datetime.today()
future_day: timedelta = timedelta(how_many_days)
money_day: datetime = today + future_day

date_of_target_amount_vaccinated: str = str(money_day.strftime("%B %d, %Y"))

x = "We will reach "
y = "% vaccination in "
z = " days, which falls on "

a = x + str(target_percent_vaccinated) + y + str(how_many_days) + z + str(date_of_target_amount_vaccinated) + "."

print(a)