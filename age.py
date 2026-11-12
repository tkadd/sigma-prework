import datetime as dt

def years_since_date(date: str):

    start = dt.date.strptime(date, "%d-%m-%Y")
    today = dt.date.today()

    years = today.year - start.year

    return (years) if (dt.date(today.year, start.month, start.day) < today) else (years - 1)

if __name__ == "__main__":
    date = "01-01-1990"
    print(years_since_date(date))
