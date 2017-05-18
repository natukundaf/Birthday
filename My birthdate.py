from datetime import date
import calendar
age = int(input("Enter your age\t"))
year = int(input("Current Year\t"))

dob = int(input("Date Of Birth(1-31)\t"))
month = int(input("Month(1-12)\t"))
b = year-age-1
birthday = date(b, month, dob)

print(birthday.strftime("You were born on %d %A %b %Y"))

input("Press enter")
                  
