import calendar
if __name__ == "__main__":
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year (e.g., 2023): "))
    cal=calendar.month(year, month)
    print(cal)