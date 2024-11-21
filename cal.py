# Python code to print Calendar
# Without use of Calendar module 

# Get user input for the year, layout preference, and month option
yy = int(input("Enter the year: "))
layout = input("Do you want to print the calendar in row-wise or column-wise layout? (row/column): ").strip().lower()

# Ask if the user wants to print all months or one month at a time
choice = input("Do you want to print all months or one month at a time? (all/one): ").strip().lower()

month = {
    1: 'January', 2: 'February', 3: 'March', 
    4: 'April', 5: 'May', 6: 'June', 7: 'July', 
    8: 'August', 9: 'September', 10: 'October', 
    11: 'November', 12: 'December'
}

# Code below for calculation of odd days
def calculate_day_of_week(year, month):
    day = (year - 1) % 400
    day = (day // 100) * 5 + ((day % 100) - (day % 100) // 4) + ((day % 100) // 4) * 2
    day = day % 7

    nly = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    s = 0

    if year % 4 == 0:
        for i in range(month - 1): 
            s += ly[i]
    else:
        for i in range(month - 1): 
            s += nly[i] 

    day += s % 7
    return day % 7

# Function to print the calendar of a specific month
def print_month_calendar(month_num, year, day, layout):
    space = '  '  # Two spaces for alignment
    
    print(month[month_num], year)
    print('Su Mo Tu We Th Fr Sa')

    nly = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year % 4 == 0:
        days_in_month = ly[month_num - 1]
    else:
        days_in_month = nly[month_num - 1]
    
    # Start printing the calendar, handling the day of the week
    calendar = ['  '] * day  # Start with empty spaces

    for i in range(1, days_in_month + 1):
        calendar.append("{:02d}".format(i))

    # Print the calendar in a row-wise or column-wise layout
    if layout == 'row':
        for i in range(0, len(calendar), 7):
            print(" ".join(calendar[i:i+7]))
    elif layout == 'column':
        for i in range(0, len(calendar), 7):
            for j in range(7):
                if i + j < len(calendar):
                    print(calendar[i + j], end=' ')
            print()
    else:
        print("Invalid layout choice. Please choose 'row' or 'column'.")

# Code logic for printing all months or just one
if choice == 'all':
    for mm in range(1, 13):
        day_of_week = calculate_day_of_week(yy, mm)
        print_month_calendar(mm, yy, day_of_week, layout)
        print("\n")  # Adding extra space between months
elif choice == 'one':
    mm = int(input("Enter the month number (1-12): "))
    day_of_week = calculate_day_of_week(yy, mm)
    print_month_calendar(mm, yy, day_of_week, layout)
else:
    print("Invalid choice! Please enter 'all' or 'one'.")
