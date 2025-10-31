start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))
leap_years_list = []

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        leap_years_list.append(year)

if leap_years_list:
    print(f"Leap years from {start_year} to {end_year}: {leap_years_list}")
else:
    print(f"No leap years between {start_year} and {end_year}.")
