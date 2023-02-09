from datetime import datetime,timezone,timedelta

def CheckYear(date):
    # Check if the date is earlier than the current date
    # If yes, which means the food might expire next year
    formatted_date = datetime.strptime(date, "%m/%d")
    today = datetime.strptime(GetToday().strftime("%m/%d"), "%m/%d")
    year_now = GetCurrentYear()
    if today > formatted_date:
        year_now = year_now + 1
    return datetime(year_now, formatted_date.month, formatted_date.day)

def GetToday():
    time_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    time_in_taiwan = time_now.astimezone(timezone(timedelta(hours=8)))
    return time_in_taiwan

def GetCurrentYear():
    return int(GetToday().strftime("%Y"))

def GetCurrentTime():
    return datetime.now()
