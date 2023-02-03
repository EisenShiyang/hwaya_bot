from datetime import datetime

today = datetime.strptime(datetime.today().strftime("%m/%d"), "%m/%d")
year_now = int(datetime.today().strftime("%Y"))

def CheckYear(date):
    # Check if the date is earlier than the current date
    # If yes, which means the food might expire next year
    global year_now
    print(year_now)
    if today > datetime.strptime(date, "%m/%d"):
        year_now = year_now + 1
    return str(year_now)+"/"+date

def GetCurrentTime():
    return datetime.now()
