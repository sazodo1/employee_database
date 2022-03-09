# Read number of the employees you need to enter

employee_count_str = input("Enter number of employees: ")

employee_count = int(employee_count_str)

# Define an empty dictionary

employee_ID = {}
first_name = {}
last_name = {}
birth_year = {}
birth_month = {}
birth_day = {}
position = {}
graduated = {}

# Loop through employees
for employee_index in range(employee_count):
    # Read ID, first name, last name, birth year, month and date, position and graduated or not.

    while True:
        try:
            employee_ID = int(input("Enter employee ID: "))
            break
        except ValueError:
            print("Enter an integer")
            continue

    while True:
        first_name = (input("Enter first name: "))
        if len(first_name.strip()) > 2:
            break

    while True:
        last_name = (input("Enter last name: "))
        if len(last_name.strip()) > 2:
            break

    while True:
        birth_year_str = (input("Enter birth year (yyyy): "))

        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            if (birth_year >= 1900) and (birth_year <= 2004):
                break
            else:
                print("Birth year should be between 1900 and 2004")
        else:
            print("Birth year should contain only digits")

    while True:
        birth_month_str = (input("Enter birth month (mm): "))

        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
            if (birth_month >= 1) and (birth_month <= 12):
                break
            else:
                print("Birth month should be between 01 and 12")
        else:
            print("Birth month should contain only digits")

    while True:
        birth_day_str = (input("Enter birth day (dd): "))

        if birth_day_str.isdigit():
            birth_day = int(birth_day_str)
            if (birth_day >= 1) and (birth_day <= 31):
                break
            else:
                print("Birth day should be between 01 and 12")
        else:
            print("Birth day should contain only digits")

    while True:
        position = (input("Enter position: "))
        if len(position.strip()) > 2:
            break

    while True:
        graduate = str(input("Did you graduate from university?(y/n): "))
        if (graduate == "y") or (graduate == "yes") or (graduate == "n") or (graduate == "no"):
            break
        else:
            print("Enter yes or no")

    print("Employee added: ")
    print("Full name: " + first_name.capitalize() + " " + last_name.capitalize() + ", " +
          "Birthday: " + str(birth_day) + "/" + str(birth_month) + "/" + str(birth_year) +
          ", " + "Position: " + position.capitalize() + ", " + "Graduated?: " + graduate.capitalize()
          )
