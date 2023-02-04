import pymongo
from Helper.DateHelper import *
from Utils import DBConstant
from datetime import datetime, timedelta

client = pymongo.MongoClient(DBConstant.DB_CONN)

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
    return col.find(query).sort("date", 1)  

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
    col.delete_one(check_duplicated_name_dict)

def GetTheDayFood(id):
    today = datetime.today()
    today_object = datetime(today.year, today.month, today.day)
    col = setFoodDB()
    query = {"id": id, "date": today_object}
    return col.count_documents(query), col.find(query)

def GetThreeDaysFood(id):
    target_date = datetime.today() + timedelta(days=3)
    target_date_object = datetime(target_date.year, target_date.month, target_date.day)
    today = datetime.today()
    today_object = datetime(today.year, today.month, today.day)
    col = setFoodDB()
    query = {"id": id, "date": {"$gt":today_object,"$lte":target_date_object}}
    return col.count_documents(query), col.find(query).sort("date", 1)

def RemoveTheDayFood(id, food):
    col = setFoodDB()
    query = {"id": id, "item": food.GetItem(), "date": food.GetDateObject(), "location": food.GetLocation()}
    col.delete_one(query)
    
def setUserDB():
    db = client[DBConstant.USER_DBNAME]
    col = db[DBConstant.USER_COLLECTION]
    return col

def setFoodDB():
    db = client[DBConstant.FOOD_DBNAME]
    col = db[DBConstant.FOOD_COLLECTION]
    return col