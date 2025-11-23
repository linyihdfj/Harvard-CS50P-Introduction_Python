def main():
    print(get_date())

def valid_date(month, day, year):
    return 1 <= month <= 12 and 1 <= day <= 31 and year >= 0

def get_date():
    valid_months = [
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
        "December"
    ]

    while True:
        try:
            # pay attention to the lifecircle of date
            date = input("Date: ")
            month, day, year = map(int, date.split("/"))
            if valid_date(month, day, year):
                return f"{year:04}-{month:02}-{day:02}"
        except ValueError:
            month, day, year = date.split()
            day = day.removesuffix(",")
            if month in valid_months:
                month_index = valid_months.index(month) + 1
                day = int(day)
                year = int(year)
                if valid_date(month_index, day, year):
                    return f"{year:04}-{month_index:02}-{day:02}"
main()