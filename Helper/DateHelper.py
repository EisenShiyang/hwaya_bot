from datetime import datetime

today = datetime.strptime(datetime.today().strftime("%m/%d"), "%m/%d")
year_now = int(datetime.today().strftime("%Y"))

def CheckYear(date):
    # Check if the date is earlier than the current date
    # If yes, which means the food might expire next year
    formatted_date = datetime.strptime(date, "%m/%d")
    global year_now
    if today > formatted_date:
        year_now = year_now + 1
    return datetime(year_now, formatted_date.month, formatted_date.day)

def GetCurrentTime():
    return datetime.now()
