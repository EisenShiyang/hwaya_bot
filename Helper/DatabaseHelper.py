import pymongo
from Helper.DateHelper import *
from Utils import DBConstant
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

def AddFood(command):
    col = setFoodDB()
    food_dict = {
        "id": command.GetId(),
        "item": command.GetItem(),
        "date": CheckYear(command.GetDate()),
        "Location": command.GetLocation(),
        "insert_date": GetCurrentTime()
    }
    col.insert_one(food_dict)

def DeleteFood(command):
    col = setFoodDB()
    check_duplicated_name_dict = {
        "id": command.GetId(),
        "item": command.GetItem(),
        "Location": command.GetLocation(),
        "date": CheckYear(command.GetDate())
    }
    col.delete_one(check_duplicated_name_dict)

def LoadFood():
    col = setFoodDB()

def setUserDB():
    db = client[DBConstant.USER_DBNAME]
    col = db[DBConstant.USER_COLLECTION]
    return col

def setFoodDB():
    db = client[DBConstant.FOOD_DBNAME]
    col = db[DBConstant.FOOD_COLLECTION]
    return col