def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
        print(f"Yes the given {year} is Leap year")
    else:
        print(f"No the given {year} is Leap year")
year=int(input("Enter a year: "))
print(leap_year(year))
