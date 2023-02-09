import pymongo
import calendar
from Helper.DateHelper import *
from Utils import DBSecret
from datetime import datetime, timedelta, timezone

client = pymongo.MongoClient(DBSecret.DB_CONN)

def Register(id, name): 
    if CheckRegistered(id):
        return None
    
    col = setUserDB()
    user_dict = { "id":id, "name":name }
    return col.insert_one(user_dict)

def CheckRegistered(id):
    col = setUserDB()
    query = { "id" : id }
    return col.count_documents(query) > 0

def LoadUser():
    col = setUserDB()
    return col.find()      

def LoadFood(id):
    col = setFoodDB()
    query = { "id" : id }
    return col.count_documents(query), col.find(query).sort("date", 1)

def AddFood(command):
    col = setFoodDB()
    food_dict = {
        "id": command.GetId(),
        "item": command.GetItem(),
        "date": CheckYear(command.GetDate()),
        "location": command.GetLocation(),
        "insert_date": GetCurrentTime()
    }
    col.insert_one(food_dict)

def DeleteFood(command):
    col = setFoodDB()
    check_duplicated_name_dict = {
        "id": command.GetId(),
        "item": command.GetItem(),
        "location": command.GetLocation(),
        "date": CheckYear(command.GetDate())
    }
    return col.delete_one(check_duplicated_name_dict)

def GetTheDayFood(id):
    today = GetToday()
    today_object = datetime(today.year, today.month, today.day)
    col = setFoodDB()
    query = {"id": id, "date": today_object}
    return col.count_documents(query), col.find(query)

def GetThreeDaysFood(id):
    target_date = GetToday() + timedelta(days=3)
    target_date_object = datetime(target_date.year, target_date.month, target_date.day)
    today = GetToday()
    today_object = datetime(today.year, today.month, today.day)
    col = setFoodDB()
    query = {"id": id, "date": {"$gt":today_object,"$lte":target_date_object}}
    return col.count_documents(query), col.find(query).sort("date", 1)

def GetTheMonthFood(id):
    today = GetToday()
    today_object = datetime(today.year, today.month, today.day)
    last_day_date = calendar.monthrange(today.year, today.month)[1]
    last_day_date_object = datetime(today.year, today.month, last_day_date)
    col = setFoodDB()
    query = {"id": id, "date": {"$gte":today_object,"$lte":last_day_date_object}}
    return col.count_documents(query), col.find(query).sort("date", 1)

def RemoveTheDayFood(id, food):
    col = setFoodDB()
    query = {"id": id, "item": food.GetItem(), "date": food.GetDateObject(), "location": food.GetLocation()}
    col.delete_one(query)
    
def setUserDB():
    db = client[DBSecret.USER_DBNAME]
    col = db[DBSecret.USER_COLLECTION]
    return col

def setFoodDB():
    db = client[DBSecret.FOOD_DBNAME]
    col = db[DBSecret.FOOD_COLLECTION]
    return col