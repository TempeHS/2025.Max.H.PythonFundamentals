months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def validate_date(date_str):
    try:
        if "/" in date_str:
            month, day, year = date_str.split("/")
        else:
            month, day, year = date_str.split()
            month = months.index(month) + 1  # Get the numerical value of the month
        month = int(month)
        day = int(day)
        year = int(year)
        if month < 1 or month > 12 or day < 1 or day > 31 or year < 1:
            raise ValueError("Invalid date")
        return f"{year:04d}-{month:02d}-{day:02d}"
    except (ValueError, IndexError):
        return None


def main():
    while True:
        date_input = input("Enter a date (in format 'M/D/YYYY' or 'Month Day, YYYY'): ")
        formatted_date = validate_date(date_input)
        if formatted_date:
            print("Date in YYYY-MM-DD format:", formatted_date)
            break
        else:
            print("Invalid date format. Please try again.")


if __name__ == "__main__":
    main()
