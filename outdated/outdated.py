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
    "December"
]

while True:
    try:
        raw_date = input("Date: ")
        if "/" in raw_date:
            mm, dd, yy = raw_date.split("/")
            mm, dd, yy = int(mm), int(dd), int(yy)
            if (mm <= 12) and (dd <= 31):
                print(f"{yy}-{mm:02}-{dd:02}")
                break
        elif "," in raw_date:
            mm, dd, yy = raw_date.split()
            mm = (months.index(mm))+1
            dd, yy = int(dd.removesuffix(",")), int(yy)
            if (mm <= 12) and (dd <= 31):
                print(f"{yy}-{mm:02}-{dd:02}")
                break
    except ValueError:
        pass






